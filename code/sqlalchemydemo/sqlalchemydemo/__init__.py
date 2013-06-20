import transaction

from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError
from model import DBSession, Base, Article


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('article_list', '/')
    config.add_route('show_article', '/article/{article}')
    config.add_route('add_article', '/add_article')
    config.scan()

    # SQL Alchemy stuff.
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    try:
        Base.metadata.create_all(engine)
        with transaction.manager:
            article = Article(title='Test article', body="Test test test")
            DBSession.add(article)
    except IntegrityError:
        print "Skipping creating, integrity error was thrown"

    return config.make_wsgi_app()
