from abc import abstractmethod
import random as rd


class Generator:
    @abstractmethod
    def generate():
        return []


class MockGenerator(Generator):
    def generate():
        return [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


class RealGenerator(Generator):
    def generate():
        return rd.sample(range(0, 37, 2), 5) + rd.sample(range(1, 37, 2), 5)


class Printer:
    @abstractmethod
    def print_ticket_special(self):
        pass

    def print_ticket(self):
        pass


class MockPrinter(Printer):
    def print_ticket_special(self, name, seats):
        booker = name
        seat = seats
        return [booker, seat]

    def print_ticket(self, name, seats):
        booker = name
        seat = seats
        return [booker, seat]

class RealPrinter(Printer):
    def print_ticket_special(self, name, seats):
        str_seat = '_'.join([str(elem) for elem in seats])
        str_seat1 = ','.join([str(elem) for elem in seats])
        with open(f'{name.capitalize()}_{str_seat}', 'w') as f:
            f.write(f'Name        : {name}\n'
                    f'Seats Number: {str_seat1}\n'
                    f'Please check below your seat!!\n'
                    'Please arrive 15 minutes before')

    def print_ticket(self, name, seats):
        str_seat = '_'.join([str(elem) for elem in seats])
        str_seat1 = ','.join([str(elem) for elem in seats])
        with open(f'{name.capitalize()}_{str_seat}', 'w') as f:
            f.write(f'Name        : {name}\n'
                    f'Seats Number: {str_seat1}\n'
                    'Please arrive 15 minutes before')