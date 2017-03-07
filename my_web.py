from flask import Flask, render_template, request
import weather_web
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	forecast = None
	if address:
		forecast = weather_web.get_weather(address)
	return render_template('index.html', forecast=forecast)

@app.route("/about")
def about():
	return render_template('my_about.html')

if __name__ == "__main__":
	app.run()