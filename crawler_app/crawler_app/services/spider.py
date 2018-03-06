from crawler_app.services.graph import Graph, Page_Node
from crawler_app.services.helpers import *
from crawler_app.services.page import Page
import sys

# can set the max urls based on the depth chosen on website?
MAX_URLS = 100
        
class Spider:
    def __init__(self, seed_url, search_type, depth_limit, keyword=None):
        Page.__init__(self, seed_url)
        self.seed_url = complete_url(seed_url)
        self.search_type = search_type # 'BFS' or 'DFS'
        if keyword is not None:
            # change keyword to lowercase
            self.keyword = str(keyword).lower()
        else: self.keyword = keyword 
        self.count = 0 # track number of links crawled
        self.depth_limit = int(depth_limit) # max depth to crawl
        self.depth = 0 # current node depth
        self.to_visit = Page.to_visit # list of urls to crawl
        self.visited_set = Page.visited_set   # set of urls already crawled
        self.graph = Graph(list(),list()) # page nodes graph
        self.id = 0
        self.stop_crawl = bool() # track if stop keyword is found
        self.root_node = Page_Node(seed_url, None, 0, None, 0, False)
        self.start(self.search_type, self.root_node)
    
    #  start the crawling
    def start(self, search_type, node):
        # initialize data structures
        print('start')
        self.to_visit.clear()
        self.visited_set.clear()
        
        # keyword not found
        self.stop_crawl == False
        
        # add root node to list to crawl
        self.to_visit.append(node)
        
        if self.search_type == 'BFS':
            self.crawler('BFS', node)
        else:
            self.crawler('DFS', node)


    def crawler(self, search_type, node):

        while node is not None and not self.stop_crawl and self.count < MAX_URLS:
            print('crawling')
            # check if link has already been crawled
            crawled = node.url in self.visited_set
            if not crawled:
                self.graph.add_node(node, self.id)
                self.count += 1
                self.id += 1
                self.visited_set.add(node.url)
                if node.parents_list:
                    # get the node's parent node
                    source_node = node.parents_list.pop()
                    # update the node depth
                    node.node_depth = source_node.node_depth+1
                    if node.id is not None and source_node.id is not None:
                        # create an edge between the current node and its parent node
                        self.graph.add_edge(source_node.id, node.id)
                            # set node's parent node
                        node.parent_node = source_node.id
            
                # create new Page object
                pg = Page(node.url)
                
                # if depth limit has not been reached
                if node.node_depth < self.depth_limit:
                    print('parsing')
                    links = pg.get_links(node.url)
                    links = validate_url(links, self.count, MAX_URLS)
                    # remove any duplicate links present
                    links = remove_duplicates(links)
                    self.crawl_links(node, links)
                else: break  
        
            # check if stop keyword is found
            if self.keyword and pg.find_keyword(self.keyword):
                print('keyword found!')
                node.found = True
                self.stop_crawl = True
                break;

            node = self.get_next()

            # get next node to crawl
            
        self.end_crawl()
        return self.visited_set


    '''Urls are added to the right of the deque (append)
    Difference between the two algos BFS and DFS: how urls are popped off'''
    def crawl_links(self, current_url, links):
        for link in links:
            if link not in self.to_visit:
                current_node = Page_Node(link, [current_url], self.depth, self.keyword)
                # add url to end of list source nodes list
                current_node.parents_list.append(current_url)
                # add to the end of the to_visit list
                self.to_visit.append(current_node)
                print("added", current_url.url)
                print(len(self.to_visit))

    def get_next(self):
        if len(self.to_visit)>0 and self.count < MAX_URLS:
            # BFS: queue - url popped off from left; FIFO
            if self.search_type == 'BFS':
                next_node = self.to_visit.popleft()
                print("next node", next_node.url)
            # DFS: stack - url popped off from right; LIFO
            elif self.search_type == 'DFS':
                next_node = self.to_visit.pop()
            return next_node
        else:
            return None

    # #used for testing
    # def print_data(self):
    #     # print nodes dict
    #     print("\n--------Page Nodes--------" )
    #     for node in self.graph.nodes:
    #         node.printdict()
    #     # print the graph edges
    #     if self.graph.edges:
    #         print("\n-----Graph Edges-----")
    #         print("Parent ID ---> Target ID")
    #         edge_count = 0
    #         for edge in self.graph.edges:
    #             print(str(edge.parent) +" ----> " +  str(edge.target))
    #             edge_count += 1
    #         print("Number of edges: ", edge_count)

    def end_crawl(self):
        # self.print_data()
        
        # # exit if keyword is found
        # if self.stop_crawl:
        #     exit(0)
        pass

    # def __del__(self):
    #     print('deleting')
    #     self.graph = None

def main():
    if len(sys.argv) == 4:
        Spider(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        Spider(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
    main()
#run: python Spider.py http://www.etsy.com BFS 0 keyword
