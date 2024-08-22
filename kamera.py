from flask import Flask, render_template
import subprocess
import netifaces as ni

# Ambil IP address dari interface 'wlo1'
ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

app = Flask(__name__)

# Jalankan mjpg_streamer
subprocess.Popen(["mjpg_streamer", "-i", "input_uvc.so -r 800x400 -d /dev/video0 -f 10 -q 20", "-o", "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"])

@app.route('/')
def index():
    return render_template('kamera.html', ip=ip)

try:
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
except KeyboardInterrupt:
    print("exit")
finally:
    print("done")
