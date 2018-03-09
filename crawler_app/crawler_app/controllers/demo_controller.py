import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.infrastructure.supressor import suppress
# prefix = "http://localhost:6543"
prefix = "https://www.caelum.site"

class DemoController(BaseController):

    @pyramid_handlers.action(renderer='templates/demo/index.pt')
    def index(self):

        return {"value": "demo"}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node0")
    def node_0(self):
        return {'value': 'cyan', 'links': [prefix + '/demo/node1',
                       prefix + '/demo/node2',prefix + '/demo/node3']}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node1")
    def node_1(self):
        return {'value': 'blue', 'links': []}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node2")
    def node_2(self):
        return {'value': 'red', 'links': [prefix + '/demo/node4',
                                          prefix + '/demo/node5']}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node3")
    def node_3(self):
        return {'value': 'yellow', 'links': [prefix + '/demo/node6']}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node4")
    def node_4(self):
        return {'value': 'green', 'links': []}

    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node5")
    def node_5(self):
        return {'value': 'purple', 'links': []}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node6")
    def node_6(self):
        return {'value': 'grey', 'links': [prefix + '/demo/node7',
            prefix + '/demo/node8',prefix + '/demo/node9']}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node7")
    def node_7(self):
        return {'value': 'pink', 'links': []}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node8")
    def node_8(self):
        return {'value': 'black', 'links': [prefix + '/demo/node10']}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node9")
    def node_9(self):
        return {'value': 'white', 'links': []}


    @pyramid_handlers.action(renderer='templates/demo/node.pt',
                             name="node10")
    def node_10(self):
        return {'value': 'brown', 'links': []}