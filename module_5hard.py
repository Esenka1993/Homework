import time

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'



class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title



class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


    def log_out(self):
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *videos):
        for video in videos:
            for i in self.videos:
                if video.title not in i.title:
                    self.videos.append(video)

    def get_videos(self, search_word: str):
        results = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                results.append(video.title)
        return results

     def watch_video(self, movie: str):
        if self.current_user:
            for video in self.videos:
                if movie in video.title:
                    if not video.adult_mode:
                        for i in range(1, video.duration+1):
                            print(i)
                            video.time_now += i
                            time.sleep(1)
                            video.time_now = 0
                        print('Конец видео')
                    if video.adult_mode and self.current_user.age > 18:
                        for i in range(1, video.duration+1):
                            print(i)
                            video.time_now += i
                            time.sleep(1)
                            video.time_now = 0
                        print('Конец видео')
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')


