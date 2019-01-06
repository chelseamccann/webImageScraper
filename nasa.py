import requests
from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)

r = requests.get('https://api.nasa.gov/planetary/apod?api_key=YmTVTq0O6kVTUJI4hGlVECLuDzbHoTqE5coobWPP')

@app.route('/')
def get_image():
     imge = r.json()
     user_image = imge['hdurl']
     return render_template("index.html", img=user_image)


    #filename='%s.jpg'
    #return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()