from flask import Flask, request
import socket   

app = Flask(__name__)

@app.route('/')
def home():
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print("Your Computer Name is:"+hostname)
    print("Your Computer IP Address is:"+IPAddr)
    return hostname + IPAddr
@app.route('/ip')
def ip():
    ip_address = request.remote_addr
    return "Requester IP: " + ip_address
if __name__ == '__main__':
    app.run()
