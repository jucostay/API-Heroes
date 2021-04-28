from flask_restful import Resource
from flask import request

from models.hero import Hero
from modules.hero import HeroModule


class HeroesHandler(Resource):
    """Heroes handler"""

    def get(self):
        """Get heroes"""
        try:
            # Fazendo a consulta no banco de dados
            heroes = Hero.get_heroes()

            # Montando a resposta, por enquanto iremos deixar o cursor vazio
            response = {
                'cursor': None,
                'heroes': []
            }
            # Vamos percorer os herois e transformar em json
            for hero in heroes:
                response['heroes'].append(hero.to_dict())

            return response

        except Exception as error:
            return {
                       'message': 'Error on get heroes',
                       'details': str(error)
                   }, 500

    def post(self):
        """Create a new hero"""
        try:
            if not request.is_json or 'hero' not in request.json:
                return {'message': 'Bad request'}, 400

            hero = HeroModule.create(request.json['hero'])
            return hero.to_dict()

        except Exception as error:
            return {
                       'message': 'Error on create a new hero',
                       'details': str(error)
                   }, 500


class HeroHandler(Resource):
    """Hero handler"""

    # Nessa variável vamos colocar o nome da coleção para ser salvo no banco de dados
    _collection_name = 'Hero'

    def get(self, hero_id):
        """Get hero"""
        try:
            hero = Hero.get_hero(hero_id)
            if hero:
                return hero.to_dict()
            return {'message': 'Hero not found'}, 404

        except Exception as error:
            return {
                       'message': 'Error on get hero',
                       'details': str(error)
                   }, 500

    def post(self, hero_id):
        """Update a hero"""
        try:
            hero = Hero.get_hero(hero_id)
            if not hero:
                return {'message': 'Hero not found'}, 404
            HeroModule.update(hero, request.json['hero'])
            return hero.to_dict()
        except Exception as error:
            return {
                       'message': 'Error on update hero',
                       'details': str(error)
                   }, 500

    def delete(self, hero_id):
        """Delete hero"""
        try:
            hero = Hero.delete(hero_id)
            if not hero:
                return {'message': 'Hero deleted'}, 200
            return {'message': 'Hero not found'}, 404

        except Exception as error:
            return {
                       'message': 'Error on delete hero',
                       'details': str(error)
                   }, 500
