from flask import Flask
from database import db
from user.blueprint import user_blueprint, basic_info_blueprint
from config import DevConfig
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_blueprint)
app.register_blueprint(basic_info_blueprint)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=2020, debug=True)
