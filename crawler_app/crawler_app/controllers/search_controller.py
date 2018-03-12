import pyramid_handlers
from pyramid.httpexceptions import HTTPFound
from crawler_app.controllers.base_controller import BaseController
from crawler_app.viewmodels.crawl_new_vm import NewCrawl
from crawler_app.services.history_service import HistoryService
from crawler_app.services.crawl_service import CrawlService
from crawler_app.services.helpers import validate_seed


class SearchController(BaseController):
    @pyramid_handlers.action(renderer='templates/search/index.pt',
                             request_method='GET')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/home/signin')

        state = NewCrawl()
        state.previous_searches = HistoryService.get_history(self.logged_in_user_id)

        return state.to_dict()
    
    @pyramid_handlers.action(renderer='templates/search/error.pt',
                             name="error")
    def error(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/home/signin')
        return {'value': 'page_error'}

    @pyramid_handlers.action(renderer='templates/visualization/viz.pt',
                             request_method='POST',
                             name='results')
    def new_search_post(self):
        vm = NewCrawl()
        vm.from_dict(self.data_dict)

        if not (vm.archived or vm.new_from_archived):
            if validate_seed(vm.url):
                graph = CrawlService.kick_off_crawl(self.logged_in_user_id, vm.url, vm.search_type, vm.depth, vm.keyword)
                return {'crawl_result': graph}
            else:
                return self.redirect('error')

        if vm.new_from_archived:
            history = HistoryService.get_params_by_history_id(vm.new_from_archived)
            graph = CrawlService.kick_off_crawl(self.logged_in_user_id, history.get('url'), history.get('search_type'),
                                         history.get('search_limit'), history.get('keyword'))
            return {'crawl_result': graph}

        if vm.archived:
            graph = HistoryService.get_archived_graph_data(vm.archived)
            return {'crawl_result': graph}

    @pyramid_handlers.action(renderer='templates/visualization/viz.pt',
                             name='demo')
    def demo_graph_results(self):
        graph = '''{"found": "false", "children": [{"found": "false", "children": [{"found": "false", "url": "https://www.caelum.site/demo/node5", "domain": "www.caelum.site"}, {"found": "false", "url": "https://www.caelum.site/demo/node4", "domain": "www.caelum.site"}], "url": "https://www.caelum.site/demo/node2", "domain": "www.caelum.site"}, {"found": "false", "url": "https://www.caelum.site/demo/node1", "domain": "www.caelum.site"}, {"found": "false", "children": [{"found": "false", "children": [{"found": "false", "url": "https://www.caelum.site/demo/node9", "domain": "www.caelum.site"}, {"found": "false", "children": [{"found": "false", "url": "https://www.caelum.site/demo/node10", "domain": "www.caelum.site"}], "url": "https://www.caelum.site/demo/node8", "domain": "www.caelum.site"}, {"found": "false", "url": "https://www.caelum.site/demo/node7", "domain": "www.caelum.site"}], "url": "https://www.caelum.site/demo/node6", "domain": "www.caelum.site"}], "url": "https://www.caelum.site/demo/node3", "domain": "www.caelum.site"}], "url": "https://www.caelum.site/demo/node0", "domain": "www.caelum.site"}'''

        return {'crawl_result': graph}
