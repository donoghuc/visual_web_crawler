import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.services.account_service import AccountService
from crawler_app.viewmodels.crawl_new_vm import NewCrawl
from crawler_app.services.spider import Spider
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
        print(vm.url)
        print(vm.search_type)
        print(vm.depth)
        # time.sleep(5)
        crawl_obj = Spider(vm.url, vm.search_type,vm.depth)
        crawl_obj.print_data()
        build_frame = dict(node_id=[],node_depth=[],parent_node=[],domain=[],url=[])
        for i in crawl_obj.graph.nodes:
            build_frame['node_id'].append(i.id)
            build_frame['node_depth'].append(i.node_depth)
            build_frame['parent_node'].append(i.parent_node)
            build_frame['domain'].append(i.domain)
            build_frame['url'].append(i.url)
        df = pd.DataFrame(build_frame)
        del crawl_obj
        del build_frame

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


        # graph = """{"url": "https://www.cas-donoghue.org/", "domain": "www.cas-donoghue.org", "children": [{"url": "https://www.linkedin.com/in/casadilla", "domain": "www.linkedin.com"}, {"url": "https://github.com/donoghuc/casadilla_web", "domain": "github.com", "children": [{"url": "https://help.github.com", "domain": "help.github.com"}, {"url": "https://shop.github.com", "domain": "shop.github.com"}, {"url": "https://github.com", "domain": "github.com"}, {"url": "https://help.github.com/articles/which-remote-url-should-i-use", "domain": "help.github.com"}, {"url": "https://training.github.com", "domain": "training.github.com"}, {"url": "https://github.com/about", "domain": "github.com"}, {"url": "https://help.github.com/articles/github-terms-of-service/", "domain": "help.github.com"}, {"url": "https://github.com/blog", "domain": "github.com"}, {"url": "https://status.github.com/", "domain": "status.github.com"}, {"url": "https://github.com/site/privacy", "domain": "github.com"}, {"url": "https://help.github.com/articles/github-security/", "domain": "help.github.com"}, {"url": "https://github.com/", "domain": "github.com"}, {"url": "https://developer.github.com", "domain": "developer.github.com"}, {"url": "https://github.com/contact", "domain": "github.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}]}, {"url": "https://github.com/donoghuc", "domain": "github.com", "children": [{"url": "https://help.github.com/categories/setting-up-and-managing-your-github-profile", "domain": "help.github.com"}, {"url": "https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile", "domain": "help.github.com"}]}, {"url": "https://twitter.com/mkennedy", "domain": "twitter.com", "children": [{"url": "https://t.co/m4AkQtKgnq", "domain": "t.co"}, {"url": "https://t.co/VMKcuZdpnM", "domain": "t.co"}, {"url": "https://dev.twitter.com/overview/terms/agreement", "domain": "dev.twitter.com"}, {"url": "https://dev.twitter.com/overview/terms/policy", "domain": "dev.twitter.com"}, {"url": "https://dev.twitter.com/web/embedded-tweets", "domain": "dev.twitter.com"}, {"url": "https://t.co/V7ueFhogSm", "domain": "t.co"}]}, {"url": "https://talkpython.fm", "domain": "talkpython.fm"}, {"url": "https://donoghuc.github.io", "domain": "donoghuc.github.io"}]}"""
        return {'crawl_result': graph}

        # return self.redirect('/home')
        # return self.redirect('/home')


