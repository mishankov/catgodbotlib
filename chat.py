class Chat:
    def __init__(self, json):
        self.id = json['id']
        self.type = json['type']

        if 'title' in json.keys():
            self.title = json['title']
        else:
            self.title = ''

        if 'username' in json.keys():
            self.username = json['username']
        else:
            self.username = ''

        if 'first_name' in json.keys():
            self.first_name = json['first_name']
        else:
            self.first_name = ''

        if 'last_name' in json.keys():
            self.last_name = json['last_name']
        else:
            self.last_name = ''

        if 'all_members_are_administrators' in json.keys():
            self.all_members_are_administrators = json['all_members_are_administrators']
        else:
            self.all_members_are_administrators = ''
