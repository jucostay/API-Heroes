import re
from models.hero import Hero


class HeroModule(object):
    """Hero module"""

    @staticmethod
    def create(params):
        """
        Create a new hero
        :param dict params: Request dict params
        :return Hero: Hero created
        """
        hero = Hero()
        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()
        return hero

    @staticmethod
    def update(hero, params):
        """Update hero"""
        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()

    @staticmethod
    def valid_hero_params(hero):
        """Valid hero params"""
        regex = re.search(
            """^[a-zA-Z0-9-_]+[:./\\]+([a-zA-Z0-9 -_./:=&"'?%+@#$!]+$""", hero.imageUrl)
        if not hero.name:
            raise Exception('Bad request, name is required')
        if not hero.universe == ("DC" or "MARVEL"):
            raise Exception("Bad request, invalid universe")
        if not regex:
            raise Exception("Bad request, invalid image url")

    @staticmethod
    def format_hero_params(hero):
        """Format hero params"""
        hero.name = hero.name.title().strip()
        hero.description = hero.description.strip().capitalize()