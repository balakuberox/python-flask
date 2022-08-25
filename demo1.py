from flask import Flask,request ,redirect ,render_template,url_for
from decouple import config
from datetime import date
import json
import socket   
import os

IMAGE_FOLDER = os.path.join('static',"imgs")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
app._static_folder = './templates/static/'
@app.route('/') 
def home():
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print("Your Computer Name is:"+hostname)
    print("Your Computer IP Address is:"+IPAddr)
    today = date.today()
    today=today.strftime("%d%m%Y")
    data={"ip_address":IPAddr, "port":config('PORT'), "hostname":hostname, "date":today, "authoris":"bala"}
    # jdata = json.loads(data)
    json_object = json.dumps(data)
    return json_object
@app.route('/about')
def ip():
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1304.jpg')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1309.jpg')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1305.jpg')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1306.jpg')
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1307.jpg')
    # img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    
    # img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("./about.html",user_img1 = img1,user_img2 = img2,user_img3 = img3,user_img4 = img4,user_img5 = img5)


@app.route('/status/<URL>')
def urlredirect(URL):
    if len(URL) > 2:
        encoded_url=URL.replace("_", ".")
        end_url = "https://"+ encoded_url
        return redirect(end_url,307)
    else:
        return "invald URL request"
    
if __name__ == '__main__':
    # app.run()
    print("this is the line before the app.run command")
    app.run(host=config('HOST'), port=config('PORT'))
