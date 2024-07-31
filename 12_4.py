import logging
import unittest


class Runner:

    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info(f'test_walk" выполнен успешно, скорость {first.name}')
            return first.speed >= 0
        except ValueError:
            logging.warning(f'Неверная скорость для Runner, сейчас {first.speed}')


    def test_run(self):
        try:
            logging.info(f'test_run" выполнен успешно, имя {first.name}')
            return first.name == "Леша"
        except TypeError:
            logging.warning(f'Неверный тип данных для Runner, сейчас {first.name}')

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                            format='%(levelname)s | %(messege)s')


first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

t = Tournament(101, first)
print(t.start())
