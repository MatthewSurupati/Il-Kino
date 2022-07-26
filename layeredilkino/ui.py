from layeredilkino.service import IlKinoService

class IlKinoUI:
    def __init__(self, _service: IlKinoService):
        self.service = _service

    def run(self):
        Done = False
        while not Done:
            try:
                inp = int(input('What will you choose: '))
                if inp == 1:
                    name = str(input('\nName: ').upper())
                    seats = list(map(int, input('\nSeat: ').split(",")))
                    self.service.booking(name, seats)
                elif inp == 2:
                    find_ = input('siapa yang dicari: ').upper()
                    self.service.find_by_name(find_)
                elif inp == 3:
                    print(self.service.report())
                elif inp == 4:
                    print('SAYOUNARA !!')
                    break
                elif inp == 5:
                    hour = input('masukkan jam: ')
                    self.get_booked_by_hour(hour)
                else:
                    print("pick from the chosen number !!")
            except ValueError:
                print("Please input use the representative number for the options\n")

