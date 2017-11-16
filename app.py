import platform
import psutil
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def index():
    p=""
    m=""
    s=""
    try:
        p = platform.platform()
        v = str(psutil.virtual_memory())
        fs = os.statvfs(".")
        f = str(fs.f_frsize * fs.f_bavail)
    except:
        p = 'error'
    return render_template('index.html', platform = p, virtmem = v, freespace = f)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    Bootstrap(app)
    app.run(host='0.0.0.0', port=port)
