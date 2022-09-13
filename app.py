from flask import Flask
from models import db
from routes import api
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\Yoselin\\Desktop\\Back\\base.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"
db.init_app(app)
CORS(app)
jwt = JWTManager(app)
Migrate(app, db)
app.register_blueprint(api, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True)