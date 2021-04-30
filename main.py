"""Arquivio main da API"""
import firebase_admin
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from views.top_heroes import TopHeroesHandler
from views.heroes_search import HeroesSearchHandler
from views.heroes import HeroesHandler, HeroHandler

app = Flask(__name__)
CORS(app)
API = Api(app)

# Iniciando o firebase com as credenciais que você salvou na raiz da aplicação no passo 3.1 Não se esqueça de colocar
# o nome do arquivo que você salvou, no meu caso esta com o nome de
# "tour-of-heroes-firebase-adminsdk-gds0n-14ebf97e39.json"

cred = firebase_admin.credentials.Certificate(
    './angular-heroes-julia-firebase-adminsdk-b67w3-6d842ba9a6.json')

firebase_admin.initialize_app(credential=cred)


@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothing at this URL.', 404


# Nossa classe principal
class Index(Resource):
    """class return API index"""

    def get(self):
        """return API"""
        return {"API": "Heroes"}


# Nossa primeira url
API.add_resource(Index, '/', endpoint='index')
API.add_resource(HeroesHandler, '/heroes', endpoint='heroes')
API.add_resource(HeroHandler, '/hero/<hero_id>', endpoint='hero')
API.add_resource(TopHeroesHandler, '/top-heroes', endpoint='top-heroes')
API.add_resource(HeroesSearchHandler, '/search', endpoint='search')

if __name__ == '__main__':
    # Isso é utilizado somente para executar a aplicação local. Quando
    # realizarmos o deploy para o Google App Engine, o webserver deles ira
    # iniciar a aplicação de outra forma
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
