class User:
    def __init__(self, json):
        self.id = json['id']
        self.first_name = json['first_name']

        if 'last_name' in json.keys():
            self.last_name = json['last_name']
        else:
            self.last_name = ''

        if 'username' in json.keys():
            self.username = json['username']
        else:
            self.username = ''
