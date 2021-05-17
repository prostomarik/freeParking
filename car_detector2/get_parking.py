from detector import *
from tests.test import *
import json
import time

#detected_cars = action()
#print(test1(detected_cars, '/correct/test1.json'))
#video_capture, model = load_model()
#places, frame = start_action()
#
def get_jsons(mode):

	(free_places, bisy_places) = action(places)
	
	if mode == 1:
		if len(free_places) == 0:
			return 0

		out = "{ \"free_places\":[ "
		for tmp in free_places:
			out += str(tmp) + ", "
		out = out[:-2]
		out += "]}"

	elif mode == 0:
		if len(bisy_places) == 0:
			return 0
		out = "{ \"bisy_places\":[ "
		for tmp in bisy_places:
			out += str(tmp) + ", "
		out = out[:-2]
		out += "]}"
	return out

if __name__ == "__main__":
	while(1):
		#places, frame = start_action()
		s1 = get_jsons(1)
		s0 = get_jsons(0)
		text_file = open("good.txt", "w")
		n = text_file.write(s1)
		text_file.close()
		text_file = open("bad.txt", "w")
		n = text_file.write(s0)
		text_file.close()
		time.sleep(60*5)  

