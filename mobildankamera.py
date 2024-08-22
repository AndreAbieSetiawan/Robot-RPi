from flask import Flask, render_template, jsonify
import subprocess
import netifaces as ni
import RPi.GPIO as GPIO

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

app = Flask(__name__)

# Setup camera streaming
subprocess.Popen(["mjpg_streamer", "-i", "input_uvc.so -r 540x320 -d /dev/video0 -f 10 -q 20", "-o", "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"])

# GPIO setup
motorkiri1 = 22
motorkiri2 = 27
motorkanan1 = 23
motorkanan2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorkiri1, GPIO.OUT)
GPIO.setup(motorkiri2, GPIO.OUT)
GPIO.setup(motorkanan1, GPIO.OUT)
GPIO.setup(motorkanan2, GPIO.OUT)

@app.route('/')
def index():
    return render_template('mobildankamera.html', ip=ip)

@app.route('/maju')
def maju():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.HIGH)
    GPIO.output(motorkanan1, GPIO.HIGH)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")

@app.route('/kiri')
def kiri():
    GPIO.output(motorkiri1, GPIO.HIGH)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.HIGH)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")

@app.route('/kanan')
def kanan():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.HIGH)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.HIGH)
    return jsonify(status="ok")

@app.route('/mundur')
def mundur():
    GPIO.output(motorkiri1, GPIO.HIGH)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.HIGH)
    return jsonify(status="ok")

@app.route('/berhenti')
def berhenti():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


