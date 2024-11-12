from flask import Flask
import os
from datetime import datetime
import subprocess
import platform
import pwd

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Prahan Alaparthi"
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Handled situation of both windows system and Linux/Unix(github codespaces)
    # as my system is windows

    if platform.system() == "Windows":
        # Windows specific
        username = os.getlogin()
        top_output = subprocess.check_output("tasklist", shell=True).decode("utf-8")
    else:
        # Linux specific
        username = os.getenv("USER") or pwd.getpwuid(os.getuid()).pw_name
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    return f"<h1>Name: {name}</h1><h2>Username: {username}</h2><h3>Server Time: {server_time}</h3><pre>{top_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
