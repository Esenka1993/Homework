from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemy_amount = 100
        fight_days = 0
        print(f'{self.name}, на нас напали!')
        while enemy_amount > 0:
            enemy_amount -= self.power
            sleep(1)
            fight_days += 1
            print(f'{self.name} сражается {fight_days} дней, осталось {enemy_amount} воинов \n')
        print(f'{self.name} одержал победу спустя {fight_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')