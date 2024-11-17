class TestController:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        #To test the application conn.
        @self.app.route('/ping', methods=['GET'])
        def ping_pong():
            return 'pong'