from layeredilkino.dto import SeatDTO
from layeredilkino.utils import RealGenerator


class Seat:
    def __init__(self, number):
        self.is_occupied = False
        self.number = number


class SpecialSeat(Seat):
    def __init__(self, number, _gift):
        super().__init__(number)
        self.gift = _gift


class SeatRepository:
    def __init__(self, _generate: RealGenerator):
        self.seats = []
        self.all_r = _generate

    def setup(self, gift_: list):
        for number in range(1, 37):
            if number in self.all_r:
                self.seats.append(SpecialSeat(number, gift_))
            else:
                self.seats.append(Seat(number))

    def get_seats(self):
        returned_seat = []
        for seat in self.seats:
            dto = SeatDTO()
            dto.number = seat.number
            dto.is_occupied = seat.is_occupied
            if isinstance(seat, SpecialSeat):
                dto.gift = seat.gift
                dto.is_special = True
            returned_seat.append(dto)
        return returned_seat


class BookingRepository:
    def __init__(self):
        pass
