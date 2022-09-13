from flask import jsonify, request, Blueprint
from models import db, User, InfoLadingPage
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import json

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])  #el register, es la ruta para registrar un nuevo ususario.
def register():
    body = request.get_json()    
    newUser = User(
        name=body["name"],           #bodyname son los datos que vienn del fron end, los datos del formulario viajan  y llegan al bacj(ruta register)
        email=body["email"],           
        password = body["password"]
    )
    db.session.add(newUser)      #session.add guardo los datos ingresados del nuevo usuario
    db.session.commit()          #sessioncommit va en union con el add.
    response_body = {
        "message": "El usuario se creo exitosamente"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])   #aqui me puedo logear como ususario.
def login():
    body = request.get_json()
    email = body["email"]          
    password = body["password"]
 #
    usuario = User.query.filter_by(email=email, password=password).first()      #aqui busco los datos del ususario, mail y password, verifico que los datos existan y mo se logee cualquier ususario.
    if usuario is None:     #si usuario no existe, en via mensaje incorrecto y si existe envia token y datos del usuario.
        response_body = {
            "mensaje": 'El correo o la clave incorrecta.' 
        }
    else:
        token = create_access_token(identity=usuario.id)   #aqui se crea el token, es un link largo, cada usuario debe tener su token, (su identidad)
        response_body = {
            "user": usuario.serialize(),
            "token": token
        }

    return jsonify(response_body), 200

@api.route('/getladingpage', methods=['GET'])  #obtener la lista de todas las paginas ya creadas.(tipo array)
def getladingpage():
    informationPage = InfoLadingPage.query.all()  # aqui me traigo la tabla, all traigo toda la info
   
   
    informationPage = list(map(lambda info: info.serialize(),informationPage)) #aqui guardo toda la info de la lista guardada, luego toda esta info estara en mi fron end y postman

    return jsonify(informationPage), 200
    

@api.route('/createPage', methods=['POST'])  #para crear una nueva pagina.
def createPage():

    body = request.get_json()
    informationPage = InfoLadingPage(
        image_1=body["image_1"],
        image_2=body["image_2"],
        image_3=body["image_3"],
        info_1=body["info_1"],
        info_2=body["info_2"],
        info_3=body["info_3"],
        titulo=body["titulo"],
        Subtitulo=body["Subtitulo"],
        video=body["video"],
        tips_1=body["tips_1"],
        tips_2=body["tips_2"],
        tips_3=body["tips_3"],
        tips_4=body["tips_4"],
        tips_5=body["tips_5"],
        tips_6=body["tips_6"],
        
    
    )
    db.session.add(informationPage)  #siempre para agregar add y commit
    db.session.commit()
    response_body = {
        "message": "La informacion se agrego exitosamente"
    }

    return jsonify(response_body), 200


@api.route('/updatePage/<int:id>', methods=['PUT']) #par amodificar la pagina segun el id. (segun el id que mande)
def updatePage(id): 

    body = request.get_json()
    image_1=body["image_1"]
    image_2=body["image_2"]
    image_3=body["image_3"]
    info_1=body["info_1"]
    info_2=body["info_2"]
    info_3=body["info_3"]
    titulo=body["titulo"]
    Subtitulo=body["Subtitulo"]
    video=body["video"]
    tips_1=body["tips_1"]
    tips_2=body["tips_2"]
    tips_3=body["tips_3"]
    tips_4=body["tips_4"]
    tips_5=body["tips_5"]
    tips_6=body["tips_6"]
    infopage = InfoLadingPage.query.get(id)
    infopage.image_1 = image_1
    infopage.image_2 = image_2
    infopage.image_3 = image_3
    infopage.info_1 = info_1
    infopage.info_2 = info_2
    infopage.info_3 = info_3
    infopage.titulo = titulo
    infopage.Subtitulo = Subtitulo
    infopage.video = video
    infopage.tips_1 = tips_1
    infopage.tips_2 = tips_2
    infopage.tips_3 = tips_3
    infopage.tips_4 = tips_4
    infopage.tips_5 = tips_5
    infopage.tips_6 = tips_6
    db.session.commit()

    
    
    return jsonify(infopage.serialize()), 200


@api.route('/deletepage/<int:id>', methods=['DELETE'])  #se elimina una pagina segun el id que se enviee.
def deletepage(id): 
    infopage = InfoLadingPage.query.get(id)
    db.session.delete(infopage)  #aqui cambio el add por el delite
    db.session.commit()
    informationPage = InfoLadingPage.query.all()  
   
   
    informationPage = list(map(lambda info: info.serialize(),informationPage))

    return jsonify(informationPage), 200

@api.route('/showlading', methods=['GET'])  #trae la info que se visualiza en la pg principal.
def showlading():
    infoPage = InfoLadingPage.query.filter_by(show=True).first()
    
    response_body = {
        "info": infoPage.serialize()
    }

    return jsonify(response_body), 200

@api.route('/updateShowlading/<int:id>', methods=['PUT']) #para  modificar SEGUN ID, que se mostrara en la pg principal 
def updateShowlading(id):
    infopage = InfoLadingPage.query.get(id)
    infopage.show = True
    db.session.commit()
    return jsonify(infopage.serialize()), 200

    #estoo es el detalle del CRUD realizado.
  