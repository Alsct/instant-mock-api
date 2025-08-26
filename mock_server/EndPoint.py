class EndPoint:
    path: str
    method: str
    response: dict

    def __init__(self, endpoint):
        self.path = endpoint['path']
        self.method = endpoint['method']
        self.response = endpoint['response']

    def __repr__(self):
        return f"Endpoint(path='{self.path}', method='{self.method}', response={self.response})"
    
    async def get_response(self):
        return self.response