from flask import Flask




app = Flask(__name__)

@app.route("/<username>", methods=['GET'])
def index(username):
	if username == "1":
		file = open("good.txt", "r") 
		out = ""
		for line in file:
			out += line
		return out
	elif username == "0":
		file = open("bad.txt", "r") 
		out = ""
		for line in file:
			out += line
		return out

	return "404"

if __name__ == "__main__":

	app.run(host='0.0.0.0', port=4567)
