from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def _repr_(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class InfoLadingPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_1 = db.Column(db.String(120), unique=False, nullable=False)
    image_2 = db.Column(db.String(120), unique=False, nullable=False)
    image_3 = db.Column(db.String(120), unique=False, nullable=False)
    info_1 = db.Column(db.String(120), unique=False, nullable=False)
    info_2 = db.Column(db.String(120), unique=False, nullable=False)
    info_3 = db.Column(db.String(120), unique=False, nullable=False)
    titulo = db.Column(db.String(80), unique=False, nullable=False)
    Subtitulo = db.Column(db.String(80), unique=False, nullable=False)
    video = db.Column(db.String(80), unique=False, nullable=False)
    tips_1 = db.Column(db.String(80), unique=False, nullable=False)
    tips_2 = db.Column(db.String(80), unique=False, nullable=False)
    tips_3 = db.Column(db.String(80), unique=False, nullable=False)
    tips_4 = db.Column(db.String(80), unique=False, nullable=False)
    tips_5 = db.Column(db.String(80), unique=False, nullable=False)
    tips_6 = db.Column(db.String(80), unique=False, nullable=False)
    show = db.Column(db.Boolean, default=False)
    
    def _repr_(self):
        return f'<InfoLadingPage {self.titulo}>'

    def serialize(self):
        return {
            "id": self.id,
            "image_1": self.image_1,
            "image_2": self.image_2,
            "image_3": self.image_3,
            "info_1": self.info_1,
            "info_2": self.info_2,
            "info_3": self.info_3,
            "titulo": self.titulo,
            "Subtitulo": self.Subtitulo,
            "video": self.video,
            "tips_1": self.tips_1,
            "tips_2": self.tips_2,
            "tips_3": self.tips_3,
            "tips_4": self.tips_4,
            "tips_5": self.tips_5,
            "tips_6": self.tips_6,
            "show": self.show,
        }        