import cv2
 
def showImage(good, bad) # список по 4 координаты свободных и занятых мест, формат : [x1, y1, x2, y2]
	image = cv2.imread('/Users/vasiliyisaev/bonch_hack/car_detector2/cat.png')
	print (type(image))
	 
	cv2.imshow('Test image',image)
		for tmp in good:
			image = cv2.rectangle(image, (tmp[1], tmp[0]), (tmp[3], tmp[2]), (0, 255, 0), thickness) 
		for tmp in bad:
			image = cv2.rectangle(image, (tmp[1], tmp[0]), (tmp[3], tmp[2]), (255, 0, 0), thickness) 
	cv2.waitKey(0)
	cv2.destroyAllWindows()