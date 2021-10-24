import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    IDsize = 1000 #Size of ID vector
    ID = [random.choice([-1,1]) for i in range(IDsize)]
    # print(ID)
    # ID = list(map(ID, lambda:str))
    # print(ID)
    return " ".join(map(str, ID))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)