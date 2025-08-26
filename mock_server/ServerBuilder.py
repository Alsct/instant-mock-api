from fastapi import FastAPI
class ServerBuilder:

    def __init__(self, endpoints):
        self.endpoints = endpoints
    
    def build(self):
        app = FastAPI()
 
        for endpoint in self.endpoints:

            app.add_api_route(
                endpoint.path,
                endpoint.get_response,
                methods=[endpoint.method]
            )
        return app
    
        