import random
import requests
import numpy as np
from flask import Flask, request, render_template

ID_SIZE = 1000 #Size of ID vector
ID = [random.choice([-1,1]) for i in range(ID_SIZE)]

app = Flask(__name__)

"""
Sends data to the pub/sub server hosted at URL: localhost:7001/sendData
The pub/sub server stores the sent data in memory inside a hashtable
"""
def sendToPublishServer(encodedData):
    url = "http://localhost:7001/sendData"
    myData = {'2': encodedData}
    print(encodedData[16:26])
    x = requests.post(url, json=myData)
    print(x)

@app.route("/publishData")
def publishData():
    dataString = request.args.get("clientData", "")
    if dataString:
        dataBinaryarr = ''.join(format(ord(x), '08b') for x in dataString)
        #Converting user data to binary vector
        dataBinary = np.zeros(ID_SIZE,)
        for i in range(len(dataBinaryarr)):
            dataBinary[i] = int(dataBinaryarr[i])
        #Converting user data to bipolar vector
        dataBipolar = dataBinary
        dataBipolar[np.isclose(dataBipolar, 0)] = -1

        #embedding ID into data
        Result = np.multiply(ID, dataBinary) + ID

        sendToPublishServer(Result.tolist())

    return render_template('form.html')
  

@app.route("/")
def index():
    
    # print(ID)
    #Creating user data
    dataString = "Hola, This is a secret msg, It is about what we discussed last time, u see the problem is that whenever that happened It crea" #data
    
    # sendToPublishServer(" ".join(map(str, ID)))
    return " ".join(map(str, ID))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)