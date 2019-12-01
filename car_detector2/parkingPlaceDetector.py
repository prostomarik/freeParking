from detector import *
import cv2
import numpy as np
def get_user_parking(background, places):
	places_ = places.tolist()
	drawing = False # true if mouse is pressed

	ix,iy = -1,-1
	k = -1
	parkingPlaces = []
	def draw_parking(event,x,y,flags,param):
	    global ix,iy,drawing

	    if event == cv2.EVENT_LBUTTONDOWN:
	        drawing = True
	        ix,iy = x,y

	    elif event == cv2.EVENT_LBUTTONUP:
	        drawing = False
	        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
	        parkingPlaces.append([x,y,ix,iy]);
	        print("[{}, {}, {}, {}]".format(x,y,ix,iy));

	img = background#np.zeros((512,512,3), np.uint8)
	print(places_[0])
	for parking in places_:
		img = cv2.rectangle(img, (parking[1], parking[0]), (parking[3], parking[2]), (0,255,0), 2) 
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_parking)
	
	while(k != 27):
	    cv2.imshow('image',img)
	    k = cv2.waitKey(1) & 0xFF

	cv2.destroyAllWindows()
