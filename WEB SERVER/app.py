from flask import Flask

from routes.manage import manage_route
from routes.teacher import teacher_route
from routes.login import login_route
from routes.student import std_route
from config import Config
app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(manage_route)
app.register_blueprint(teacher_route)
app.register_blueprint(login_route)
app.register_blueprint(std_route)

if __name__ == "__main__":
    app.run(debug=True,port=4000)#,host='0.0.0.0')