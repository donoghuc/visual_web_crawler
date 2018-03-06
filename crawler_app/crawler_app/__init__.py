# from pyramid.config import Configurator


# def main(global_config, **settings):
#     """ This function returns a Pyramid WSGI application.
#     """
#     config = Configurator(settings=settings)
#     config.include('pyramid_chameleon')
#     config.add_static_view('static', 'static', cache_max_age=3600)
#     config.add_route('home', '/')
#     config.scan()
#     return config.make_wsgi_app()

import sys
import os
import datetime
import pkg_resources
from pyramid.config import Configurator

import crawler_app
import crawler_app.controllers.home_controller as home

from crawler_app.data.dbsession import DbSessionFactory

import crawler_app.controllers.search_controller as search
import crawler_app.controllers.demo_controller as demo

# from crawler_app.services.log_service import LogService

dev_mode = False


def main(_, **settings):
    '''pull in configuration settings, initialize and fire off app server'''
    config = Configurator(settings=settings)

    # init_logging(config)  # runs first
    init_mode(config)
    init_includes(config)
    init_routing(config)
    init_db(config)

    return config.make_wsgi_app()


# def init_logging(config):
#     ''' specify loggin infor mation '''
#     settings = config.get_settings()
#     log_level = settings.get('log_level')
#     log_filename = settings.get('log_filename')

#     LogService.global_init(log_level, log_filename)

#     log_package_versions()


def init_db(_):
    top_folder = os.path.dirname(crawler_app.__file__)
    rel_folder = os.path.join('db', 'crawler.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def init_mode(config):
    ''' dev mode for verbose output and stack tracing, prod for running on server'''
    global dev_mode
    settings = config.get_settings()
    dev_mode = settings.get('mode') == 'dev'
    print('Running in {} mode.'.format('dev' if dev_mode else 'prod'))


def init_routing(config):
    ''' declare routing information to map MVC'''
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_handler('root', '/', handler=home.HomeController, action='index')
    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, search.SearchController, 'search')
    # add_controller_routes(config, demo.DemoController, 'demo')
    config.add_handler('demo','demo',handler=demo.DemoController,action="index")
    config.add_handler('node0','demo/node0',handler=demo.DemoController,action="node0")
    config.add_handler('node1','demo/node0/node1',handler=demo.DemoController,action="node1")
    # config.add_handler('node1','demo/node0/node1',handler=demo.DemoController,action='node1')
    config.scan()


def add_controller_routes(config, ctrl, prefix):
    ''' deal with case of trailing / and different routes. '''
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl) # possibly remove this as no login yet


def init_includes(config):
    ''' using chameleon template and pyramid handlers'''
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
