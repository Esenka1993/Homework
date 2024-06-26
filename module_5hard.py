class UrTube:
    def __init__(self, current_user):
        self.users = []
        self.videos = []
        self.current_user = current_user
    def log_in(self, login, password):
        if self.users[login] == password:
            self.current_user = User
    def register(self, nickname, password, age):
        if nickname != nickname:
            self.users.append(User)
        else:
            print(f'Пользователь {nickname} уже существует')
    def log_out(self):
        self.current_user = None



class Video:
    import time
    def __init__(self, title: str, duration, time_now, adult_mode: bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now = 0
        self.adult_mode = adult_mode = False

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __hash__(self):
        return hash(self.password)