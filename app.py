from flask import Flask
import numpy as np 
app = Flask(__name__)


@app.route('/')
def hello_world():
    arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
    return 'Hello World!',arr.size


if __name__ == '__main__':
    app.run()