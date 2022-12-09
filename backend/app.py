from flask import Flask, jsonify
from flask_restful import Api

from flask_jwt_extended import JWTManager

from flasklib.settings import Settings

# from blacklist import BLACKLIST

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = Settings.JWT_SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco_escola.create_all()


# @jwt.token_in_blocklist_loader
# def verificar_blacklist(self, token):
#     return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify(
        {'message': 'You have been logged out.'}), 401  # unauthorized


if __name__ == '__main__':
    from sql_alchemy import banco, banco_escola

    banco.init_app(app)
    app.run(debug=True)
