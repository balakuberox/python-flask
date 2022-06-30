from flask import Flask,request ,redirect
from decouple import config
from datetime import date
import json
import socket   

app = Flask(__name__)
@app.route('/') 
def home():
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print("Your Computer Name is:"+hostname)
    print("Your Computer IP Address is:"+IPAddr)
    today = date.today()
    today=today.strftime("%d%m%Y")
    data={"ip_address":IPAddr, "port":config('PORT'), "hostname":hostname, "date":today}
    # jdata = json.loads(data)
    json_object = json.dumps(data)
    return json_object
@app.route('/ip')
def ip():
    ip_address = request.remote_addr
    return "Requester IP: " + ip_address 


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
    print(app)