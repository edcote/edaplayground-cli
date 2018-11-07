class CLI:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        print("connected!")
