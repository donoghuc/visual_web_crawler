import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.infrastructure.supressor import suppress


class SearchController(BaseController):

    @pyramid_handlers.action(renderer='templates/search/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/home/signin')

        return {'previous_searches': [{'id': '12345', 'url': 'www.google.com'},
                                      {'id': '12346', 'url': 'www.yahoo.com'}]}
