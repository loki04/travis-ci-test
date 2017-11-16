import platform
import psutil
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    out = "Basic APP deployed by Travis CI!<br />\n"
    out += platform.platform() + "<br />\n"
    out += str(psutil.virtual_memory()) + "<br />\n"
    f = os.statvfs(".")
    out += str(f.f_frsize * f.f_bavail) + "<br />\n"
    return out

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
