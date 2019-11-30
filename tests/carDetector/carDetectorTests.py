import json

def test1(cars):
	with open('correct/test1.json') as json_file:
		json_cars = json.load(json_file)
	return (json_cars == cars)
	
print(test1([1, 2]))