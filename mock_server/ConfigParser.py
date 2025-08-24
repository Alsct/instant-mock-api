import yaml, EndPoint

class ConfigParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.endpoints = []

    def parse(self):
        with open(self.filepath, 'r') as file:
            config = yaml.safe_load(file)

        for endpoint in config['endpoints']:
            self.endpoints.append(EndPoint(endpoint))


parser = ConfigParser('api.yaml')
parser.parse()
print(parser.endpoints[0])