import json
import unittest
def test1(cars, correct):
	cars_ = cars.tolist()
	with open(correct) as json_file:
		json_cars = json.load(json_file)
	#unittest.TestCase.assertEqual(json_cars, cars)
	correct_detected = 0
	min_len = min(len(json_cars['cars']), len(cars_))
	for i in range(min_len):
		if json_cars['cars'][i] == cars_[i]:
			correct_detected += 1
	return (correct_detected / (int(min_len) + 0.000001)) # to not get "division by zero" exception
	
#print(test1([[ 320 , 655 , 397 , 782 ],[ 259 , 540 , 324 , 668 ], [1,1,1,1]], 'correct/test1.json'))