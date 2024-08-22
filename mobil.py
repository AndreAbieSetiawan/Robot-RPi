import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)

motorkiri1 = 27
motorkiri2 = 22
motorkanan1 = 23
motorkanan2 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorkiri1, GPIO.OUT)
GPIO.setup(motorkiri2, GPIO.OUT)
GPIO.setup(motorkanan1, GPIO.OUT)
GPIO.setup(motorkanan2, GPIO.OUT)

@app.route('/')
def index():
	return render_template('mobil.html')

@app.route('/maju')
def maju():
	GPIO.output(motorkiri1, GPIO.HIGH)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.HIGH)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html')

@app.route('/kiri')
def kiri():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.HIGH)
	GPIO.output(motorkanan1, GPIO.HIGH)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html')

@app.route('/kanan')
def kanan():
	GPIO.output(motorkiri1, GPIO.HIGH)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.HIGH)
	return render_template('mobil.html')

@app.route('/mundur')
def mundur():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.HIGH)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.HIGH)
	return render_template('mobil.html')

@app.route('/berhenti')
def berhenti():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html')

if __name__ == '__main__':
	app.run(debug=True,host ='0.0.0.0',port='5000')
