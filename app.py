from flask import Flask, render_template, request, Response

app = Flask(__name__)

# یوزرنیم و پسورد برای دسترسی به سایت
USERNAME = 'admin'
PASSWORD = '123456'

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route("/")
def home():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return render_template("index.html")

if __name__ == "__main__":
    # فقط روی لوکال هاست ران میشه (فقط خودت می‌تونی ببینی)
    app.run(host="127.0.0.1", port=5000, debug=True)
