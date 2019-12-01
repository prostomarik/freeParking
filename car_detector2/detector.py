import numpy as np
import cv2
import mrcnn.config
import mrcnn.utils

from mrcnn.model import MaskRCNN

from utils import *
from parkingPlaceDetector import *

# Конфигурация, которую будет использовать библиотека Mask-RCNN.
class MaskRCNNConfig(mrcnn.config.Config):
    NAME = "coco_pretrained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 1 + 80  # в датасете COCO находится 80 классов + 1 фоновый класс.
    DETECTION_MIN_CONFIDENCE = 0.8


# Фильтруем список результатов распознавания, чтобы остались только автомобили.
def get_car_boxes(boxes, class_ids):
    car_boxes = []

    for i, box in enumerate(boxes):
        # Если найденный объект не автомобиль, то пропускаем его.
        if class_ids[i] in [3, 8, 6]:
            car_boxes.append(box)

    return np.array(car_boxes)

# !!для теста!! получаем координаты машины на первой картинке видео
def get_cars(frame, model):
   

	rgb_image = frame[:, :, ::-1]
    
	results = model.detect([rgb_image], verbose=0)

	r = results[0]

	car_boxes = get_car_boxes(r['rois'], r['class_ids'])


	return car_boxes

def load_model():
	# Загружаем датасет COCO при необходимости.
	if not COCO_MODEL_PATH.exists():
	    mrcnn.utils.download_trained_weights(COCO_MODEL_PATH)


	# Видеофайл или камера для обработки — вставьте значение 0, если нужно использовать камеру, а не видеофайл.
	VIDEO_SOURCE =  "tests/testData/test1_1.mp4"

	# Создаём модель Mask-RCNN в режиме вывода.
	model = MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=MaskRCNNConfig())

	# Загружаем предобученную модель.
	model.load_weights(str(COCO_MODEL_PATH), by_name=True)

	# Загружаем видеофайл, для которого хотим запустить распознавание.
	video_capture = cv2.VideoCapture(VIDEO_SOURCE)
	return video_capture, model

def clear(video_capture):
	video_capture.release()
	cv2.destroyAllWindows()

def action():
	# Проходимся в цикле по каждому кадру.
	video_capture, model = load_model()

	while video_capture.isOpened():

		success, frame = video_capture.read()

		if not success:
			break

		car_boxes = get_cars(frame, model)
		return car_boxes

	clear(video_capture)
def start_action():
	# Проходимся в цикле по каждому кадру.
	video_capture, model = load_model()

	success, frame = video_capture.read()

	if success:
		

		car_boxes = get_cars(frame, model)

		get_user_parking(frame, car_boxes)
		
		clear(video_capture)
	else:
		print("error video loading")

	return car_boxes

	
