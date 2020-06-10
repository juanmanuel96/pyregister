from ..libraries import json, os

class RegisterConfig(object):
    def __init__(self):
        with open(os.path.abspath('./source') + '/register_config.json', 'r') as json_file:
            self.json_file = json_file.read()
        
        self.json_data = json.loads(self.json_file)
    
    def get_json_data(self):
        return self.json_data
    
    def mod_json_file(self):
        pass