# class SeatDTO:
#     def __init__(self, number):
#         self.is_occupied = False
#         self.number = number
#
#
# class SpecialSeatDTO(SeatDTO):
#     def __init__(self):
#         super().__init__(number)
#         self.gift = None

class SeatDTO:
    def __init__(self):
        self.number = None
        self.is_occupied = None
        self.is_special = None
        self.gift = None