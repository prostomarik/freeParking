from imageai.Detection import ObjectDetection


def detect_img(pict_name):
    detector = ObjectDetection()
    model_path = "/home/runner/work/freeParking/freeParking/simple_car_detectiong/models/yolo-tiny.h5"
    input_path = f"/home/runner/work/freeParking/freeParking/simple_car_detectiong/inputs/{pict_name}"
    output_path = "/home/runner/work/freeParking/freeParking/simple_car_detectiong/output/newimage.jpg"

    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detection = detector.detectObjectsFromImage(input_image=input_path,
                                                output_image_path=output_path,
                                                minimum_percentage_probability=15)

    for eachItem in detection:
        if eachItem["name"] == "car":
            print(eachItem)
        # print(eachItem["name"], " : ", eachItem["percentage_probability"])
    return detection

#
# detect_img("picture5.jpg")
