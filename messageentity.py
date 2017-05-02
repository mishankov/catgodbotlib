import user

class MessageEntity:
    def __init__(self, json):
        self.type = json['type']
        self.offset = json['offset']
        self.length = json['length']

        if 'url' in json.keys():
            self.url = json['url']
        else:
            self.url = ''

        if 'user' in json.keys():
            self.user = user.User(json['user'])
        else:
            self.user = ''
