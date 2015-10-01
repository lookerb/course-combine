from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from os import urandom


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory(
        urandom(64),
        secure=True
        httponly=True # hides cookie from Javascript
        )
    
    config = Configurator(
        session_factory=session_factory,
        settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('/', '/')
    config.add_route('logout', '/logout')
    config.add_route('login', '/login')
    config.add_route('select-semester','/select-semester')
    config.add_route('request', '/request')
    config.add_route('check', '/check')
    config.add_route('confirmation', '/confirmation')
    config.scan()
    return config.make_wsgi_app()
