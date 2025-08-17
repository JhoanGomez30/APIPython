from flask import Flask
from controllers.Controller_Task import task_bp
from errors.handlers import register_error_handlers

app = Flask(__name__)
app.register_blueprint(task_bp)

register_error_handlers(app)

if __name__ == "__main__":
    app.run(debug=True)
