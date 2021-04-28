"""Top heroes handler"""
from models.hero import Hero
from flask_restful import Resource

from random import shuffle


class TopHeroesHandler(Resource):
    """Top heroes handler"""

    @staticmethod
    def get():
        """Get top heroes"""
        try:
            heroes = Hero.get_top_heroes()
            heroes_dict = []
            for hero in heroes:
                heroes_dict.append(hero.to_dict())

            shuffle(heroes_dict)

            return {'heroes': heroes_dict[:4]}

        except Exception as error:
            return {
                       'message': 'Error on get top heroes',
                       'details': str(error)
                   }, 500