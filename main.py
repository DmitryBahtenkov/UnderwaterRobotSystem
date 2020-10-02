from flask import Flask, render_template, Response
from camera import VideoCamera
from gpio import GPIO

app = Flask(__name__)
gpio = GPIO()

#при обращении функция вечно возвращает кадры в спец. формате
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#страничка панели управления
@app.route('/')
def index():
    return "Hello!"

#видео
@app.route('/video')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#команда "вперёд", например: 192.123.123.32/forward/0
@app.route('/forward/<time>')
def forward(time):
    return gpio.Forward(time)

#команда "назад", например: 192.123.123.32/backward/12
@app.route('/backward/<time>')
def backward(time):
    return gpio.Backward(time)

#команда "влево", например: 192.123.123.32/left/90
@app.route('/left/<angle>')
def left(angle):
    return gpio.Left(angle)

#команда "вправо", например: 192.123.123.32/right/90
@app.route('/right/<angle>')
def right(angle):
    return gpio.Right(angle)

#команда "стоп", например: 192.123.123.32/backward/12
@app.route('/stop')
def stop():
    return gpio.Stop()

if __name__ == '__main__':
    app.run(host='localhost')