import random
import requests
import numpy as np
from flask import Flask


app = Flask(__name__)
def sendToPublishServer(encodedData):
    url = "http://localhost:7001/sendData"
    # print(encodedData)
    # print(type(encodedData[0]))
    myData = {'1': encodedData}
    x = requests.post(url, json=myData)
    print(x)

@app.route("/")
def index():
    IDsize = 1000 #Size of ID vector
    ID = [random.choice([-1,1]) for i in range(IDsize)]
    # print(ID)
    #Creating user data
    dataString = "Hola, This is a secret msg, It is about what we discussed last time, u see the problem is that whenever that happened It crea" #data
    dataBinaryarr = ''.join(format(ord(x), '08b') for x in dataString)
    
    
    #Converting user data to binary vector
    dataBinary = np.zeros(IDsize,)
    for i in range(len(dataBinaryarr)):
        dataBinary[i] = int(dataBinaryarr[i])
    #Converting user data to bipolar vector
    dataBipolar = dataBinary
    dataBipolar[np.isclose(dataBipolar, 0)] = -1

    #embedding ID into data
    Result = np.multiply(ID, dataBinary) + ID

    sendToPublishServer(np.array2string(Result, separator=" "))
    # sendToPublishServer(" ".join(map(str, ID)))
    return " ".join(map(str, ID))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)