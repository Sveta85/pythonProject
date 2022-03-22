#1------------------------------
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

print(card_hide('3512387413355523'))

#2------------------------------
def check_palindrome(string):

    reversed_string = string[::-1]
    if string == reversed_string:
        print(string, "полиндром")
    else:
        print(string, "не полиндром")


if __name__ == '__main__':
    check_palindrome("радар")
    check_palindrome("помидор")


#3-----------------------------
class Tomato:

    states = {0:'seed', 1:'flower', 2:'green', 3:'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник работает...")
        self._plant.grow_all()
        print("Садовник закончил")

    def harvest(self):
        print("Садовник собирает урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор урожая завершен")
        else:
            print("Слишком рано! Ваше растение не созрело")


    @staticmethod
    def knowledge_base():
        print('''Кусты томатов необходимо регулярно пропалывать.
        Лучше всего проводить полив во второй половине дня. 
        Вода должна быть прогретой.''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Виктор', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
