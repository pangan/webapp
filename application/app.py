import os
from flask import Flask
app = Flask(__name__)

pid = os.getpid()
op = open("/var/webapp.pid","w")
op.write("%s" % pid)
op.close()


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)