import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.services.account_service import AccountService
from crawler_app.viewmodels.crawl_new_vm import NewCrawl
from crawler_app.services.spider import Spider
from crawler_app.services.history_service import HistoryService
# from crawler_app.viewmodels.signin_viewmodel import SigninViewModel
# import crawler_app.infrastructure.cookie_auth as cookie_auth
import pandas as pd
import json

class SearchController(BaseController):

    @pyramid_handlers.action(renderer='templates/search/index.pt',
                             request_method='GET')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/home/signin')

        return NewCrawl().to_dict()

    @pyramid_handlers.action(renderer='templates/visualization/viz.pt',
                             request_method='POST',
                             name='results')
    def new_search_post(self):
        vm = NewCrawl()
        vm.from_dict(self.data_dict)

        crawl_obj = Spider(vm.url, vm.search_type,vm.depth)
        build_frame = dict(node_id=[],node_depth=[],parent_node=[],domain=[],url=[])
        for i in crawl_obj.graph.nodes:
            build_frame['node_id'].append(i.id)
            build_frame['node_depth'].append(i.node_depth)
            build_frame['parent_node'].append(i.parent_node)
            build_frame['domain'].append(i.domain)
            build_frame['url'].append(i.url)
            
        df = pd.DataFrame(build_frame)

        new_entry = HistoryService.add_history(self.logged_in_user_id, vm.url, vm.search_type)

        print("new entry", new_entry)
        def build_json_graph(df):
            '''build dictionary  to turn into JSON for D3 viz'''
            def make_graph(node_id, graph):
                '''recursively build a graph from nodes'''
                node = dict()
                if node_id in df['parent_node']:
                    child_list = list()
                    for idx,row in df.loc[df['parent_node'] == node_id].iterrows():
                        if node_id != row['node_id']:
                            child_list.append(make_graph(row['node_id'],node))
                    if len(child_list) > 0:
                        node['children'] = child_list
                    node['url'] = df.loc[df['node_id'] == node_id, 'url'].values[0]
                    node['domain'] = df.loc[df['node_id'] == node_id, 'domain'].values[0]
                    graph.update(node)
                return node

            graph = dict()
            make_graph(0,graph)
            start_node_children = [node for node in graph['children']]
            finalized_graph = dict(url=df.loc[df['node_id'] == 0, 'url'].values[0],
                                  domain=df.loc[df['node_id'] == 0, 'domain'].values[0],
                                  children=[node for node in graph['children']])
            return finalized_graph
            
        test = build_json_graph(df)
        graph = json.dumps(test)

        return {'crawl_result': graph}



