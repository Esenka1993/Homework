class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep and repeat'
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        cd = (super().x_distance, super().y_distance)
        return cd

    def voice(self):
        print(super().sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15) #почему эти цифры не отображаются при принте функции move и не наследуются в get_pos?
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice() #почему выводится только звук лошади?  и почему в задаче в ответе выводится только звук орла, если он наследуется вторым?
