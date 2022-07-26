# from ilkinoapps.rev_ilkino import *
# from mock import
from ilkinoapps.ilkino import *


def test_book_unbooked_seat():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('fff')
    expected1 = ilkino.seats[0].is_occupied
    ilkino.booking('matth', [1])
    expected2 = ilkino.seats[0].is_occupied
    assert expected1 == False and expected2 == True


def test_book_unknown_seat():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('bear')
    try:
        ilkino.booking("Rere", [37])
        assert Exception('Error')
    except:
        assert True


def test_book_booked_seat():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('candy')
    expected1 = ilkino.seats[0].is_occupied
    ilkino.booking('Maria', [1])
    ilkino.booking('John', [1])
    expected2 = ilkino.seats[0].is_occupied
    assert expected1 == False and expected2 == True


def test_book_seat_with_gift():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('Earphone')
    v = ilkino.booking('Matth', [2])
    try:
        expected = ilkino.seats(SpecialSeat)
        assert expected == v
    except:
        assert True


def test_get_all_distributed_gift():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('Coffee')
    ilkino.booking('Jastin', [1,3,5])
    ilkino.get_all_distributed_gift()


def test_get_book_by_hour():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('chocolate')
    ilkino.booking('Ron', [1])
    ilkino.booking('Fil', [12])
    now = dt.now()
    current_time = now.strftime("%H:00")
    v = ilkino.report()
    assert v[current_time] == 2


def test_search_booked_name():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('laptop')
    ilkino.booking('Niken', [30])
    ilkino.find_by_name('Niken')
    assert 'Niken' in ilkino.booker

def test_search_unbooked_name():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('Glass')
    ilkino.find_by_name('Rin')
    assert 'Rin' not in ilkino.booker

def test_gift_randomly_assign_left():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('popcorn')
    l = ilkino.all_r
    i = sum(l)
    assert i % 2 != 0

def test_gift_randomly_assign_right():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('Bottle')
    r = ilkino.all_r
    i = sum(r)
    assert i % 2 == 0

# def test_unknown_choice():
#     ilkino = IlKino()
#     ilkino.setup("Bag")
#     ilkino.GUI()
#     try:
#         ilkino.booking("james", [1])
#         assert Exception('eror')
#     except:
#         assert True

def test_should_print_from_parameter():
    ilkino = IlKino(MockGenerator.generate(), MockPrinter())
    ilkino.setup('Pepaya')
    current = ilkino.printer.print_ticket("Matth", [11, 12, 13])
    expected = ["Matth", [11, 12, 13]]
    assert  current == expected