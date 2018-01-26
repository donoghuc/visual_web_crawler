import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.infrastructure.supressor import suppress


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'value': 'HOME'}