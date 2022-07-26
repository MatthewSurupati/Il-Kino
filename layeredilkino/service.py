from layeredilkino.repository import SeatRepository, BookingRepository
from layeredilkino.utils import RealPrinter

class IlKinoService:
    def __init__(self, _seat_repository: SeatRepository, _booking_repository: BookingRepository):
        self.seat_repository = _seat_repository
        self.booking_repository = _booking_repository

    def get_seats(self):
        return self.seat_repository.get_seats()

    def booking(self, name, seats):
        temp_success_seat = []
        for seat_number in seats:
            if seat_number < 37:
                if self.get_seats()[seat_number - 1].is_occupied == True:
                    print('Sudah di book')
                else:
                    temp_success_seat.append(seat_number)
                    self.get_seats[seat_number - 1].is_occupied = True
            else:
                print('input the right number!')

    def find_by_name(self, find_):
        if find_ in self.booking_repository:
            pass

    def get_book_by_hour(self, hour):
        if hour in self.booking_repository:
            print('at', hour, 'there are', bookig_repository[hour], 'has been booked')