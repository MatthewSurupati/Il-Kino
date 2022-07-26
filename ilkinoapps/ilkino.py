import random as rd
from abc import abstractmethod
from datetime import datetime as dt


class IlKino:
    def __init__(self, generated, printer):
        # {} sebagai dict_keys
        self.booker = {} # booker number as key, booked seats as value
        self.seats = [] # list of seats

        # -----------------------------------
        #  untuk test
        # -----------------------------------

        # self.reports = {"9:00": 2, .....}
        self.reports = {} # key as time group value as number of bookings
        # self.r1 = rd.sample(range(1, 37, 2),5)
        # self.r2 = rd.sample(range(0, 37, 2),5)
        self.all_r = generated
        self.printer = printer

    def setup(self, gift_ :list):
        # gift_ = gift_ * 2
        for number in range(1, 37):
            if number in self.all_r:
                self.seats.append(SpecialSeat(number, gift_))
            else:
                self.seats.append(Seat(number))

        # test bener gk jumlah kursinya 26 dan special seatnya 10
        # print(self.seats)


    def booking(self, name , seats):
        # str_seat = '_'.join([str(elem) for elem in seats])
        # str_seat1 = ','.join([str(elem) for elem in seats])
        temp_success_seats = [None, None, None]
        # booked = False
        # seat_number membagi input menjadi satu: [2],[3],[4]
        # karena sejak awal set up self.seats = (self.is_occupied = False), kalau sudah ada maka akan ketahuan

        for seat_number in seats:
            if seat_number < 37:
                #  - 1 karena index dimuali dari 0 hingga 35
                if self.seats[seat_number - 1].is_occupied == True:
                    print('sudah di book')
                    # untuk test
                    # raise Exception('eror')
                else:
                    # dimasukan list baru
                    temp_success_seats.append(seat_number)
                    # diganti sudah occupied
                    self.seats[seat_number - 1].is_occupied = True
            else:
                print('input the right number!!')
                # untuk test
                # raise Exception('eror')
        #  dict .keys untuk mengecek apakah nama ada di  tempat A dan seterusnya {"A":__,"B":__ }
        #  Dictionary = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

        if name in list(self.booker.keys()): # kondisi ketika nama sudah booking melakukan booking lagi
            #  nama di list( self.booker = {'nama': 'seats'}) maka jika ada nama di list ditambahkan di list tsb
            #  temp_success_seats menambahkan di self.booker {'nama': '2,5'}
            self.booker[name] += temp_success_seats
        # jika belum ada namanya berarti membuat dict baru
        else: #kondisi ketika orang pertama kali book
            self.booker[name] = temp_success_seats

        now = dt.now()
        current_time = now.strftime("%H:00")
        # current_time = "9:00"
        # misal: self.reports = {"9:00": 2, .....}
        if current_time in list(self.reports.keys()):
            # kondisi time sudah ada
            # len untuk menghitung jumlah seat yg dipesan pada jam itu
            self.reports[current_time] += len(temp_success_seats)
        #  belum ada current_time di list self.report
        # misal: self.reports = {}
        else: # kondisi saat time baru
            self.reports[current_time] = len(temp_success_seats)
        #  print seluruh dict booker: {"F": 2, .....}
        print("booker:", self.booker)
        # cek udah keisi belum
        # misal: temp_success_seats = {"A":2}
        # self.seats[1] dicek dan berhasil diisi
        for seat_number in temp_success_seats:
            if self.seats[seat_number-1].is_occupied == True:
                print(seat_number, "Occupy")
            else:
                print(seat_number, 'Occupied')

        if any(i in self.all_r for i in seats):
            self.printer.print_ticket_special(name, seats)
        #     with open(f'{number.capitalize()}_{str_seat}', 'w') as f:
        #         f.write(f'Name        : {number}\n'
        #                 f'Seats Number: {str_seat1}\n'
        #                 f'Please check below your seat!!\n'
        #                 'Please arrive 15 minutes before')
        #
        else:
            self.printer.print_ticket(name, seats)
        #     with open(f'{number.capitalize()}_{str_seat}', 'w') as f:
        #         f.write(f'Name        : {number}\n'
        #                 f'Seats Number: {str_seat1}\n'
        #                 'Please arrive 15 minutes before')
        booked = True
        return booked

    def find_by_name(self, find_):
        #  key di dict {"KEY" : VALUE,...}
        if find_ in list(self.booker.keys()):
            #  self.booker[find_] untuk cek value di dalam Keynya
            print(find_, "has booked seat", self.booker[find_])
        else:
            print(find_, "hasn't booked any seat yet")

    def get_booked_by_hour(self, hour):
        if hour in list(self.reports.keys()):
            print(hour, 'there are seats that have been reserved', self.reports[hour])
        else:
            print(hour, "no seats reserved")


    def GUI(self):
        print("=" * 44)
        print('||' + "IlKino".center(40) + '||')
        print('||' + "Nansenstrasse 22".center(40) + '||')
        print('||' + "12047 Berlin".center(40) + '||')
        print("=" * 44, '\n')
        print("SCREEN".center(44, '='),'\n')
        print(f'   [1]   [3]   [5]       [2]   [4]   [6]')
        print(f'   [7]   [9]   [11]      [8]   [10]  [12]')
        print(f'   [13]  [15]  [17]      [12]  [14]  [16]')
        print(f'   [19]  [21]  [23]      [18]  [20]  [22]')
        print(f'   [25]  [27]  [29]      [24]  [26]  [28]')
        print(f'   [31]  [33]  [35]      [32]  [34]  [36]\n')
        print('=' * 26)
        print('||' + 'MENU'.center(22) + '||')
        print('=' * 26)
        print('||' + '1' + '||' + 'Seat Booking'.rjust(1) + '\t||')
        print('=' * 26)
        print('||' + '2' + '||' + 'Find By Name'.rjust(1) + '\t||')
        print('=' * 26)
        print('||' + '3' + '||' + 'Report'.rjust(1) + '\t\t||')
        print('=' * 26)
        print('||' + '4' + '||' + 'Exit'.rjust(1) + '\t\t||')
        print('=' * 26, '\n')


    def run(self):
        Done = False
        while not Done:
            self.GUI()
            try:
                inp = int(input('What will you choose: '))
                if inp == 1:
                    name = str(input('\nName: ').upper())
                    seats = list(map(int, input('\nSeat: ').split(",")))
                    self.booking(name,seats)
                elif inp == 2:
                    find_ = input('siapa yang dicari: ').upper()
                    self.find_by_name(find_)
                elif inp == 3:
                    print(self.report())
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

    def get_all_distributed_gift(self):
        gift_seat = []
        for obj in self.seats:
            if obj.number is self.all_r:
                # if obj.is_occupied() == True:
                gift_seat.append([obj.number, obj.get_gift])
        for i, j in gift_seat:
            print(f'{i}-{j}')
        return len(gift_seat)


    def report(self):
        return self.reports, self.get_all_distributed_gift()


class Seat:
    def __init__(self, number):
        self.is_occupied = False
        self.number = number

    def add_person(self):
        if self.is_occupied == True:
            print("is occupied")
        else:
            self.is_occupied = True

    def remove_person(self):
        if self.is_occupied == False:
            print("empty seat")
        else:
            self.is_occupied = False


class SpecialSeat(Seat):
    def __init__(self, gift_, number):
        super().__init__(number)
        self.gift = gift_

    def get_gift(self):
        return self.gift

class Generator:
    @abstractmethod
    def generate():
        return []

class MockGenerator(Generator):
    def generate():
        return [1,3,5]

class RealGenerator(Generator):
    def generate():
        return rd.sample(range(0, 37, 2),5) + rd.sample(range(1, 37, 2),5)


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

def resize(array_2d):
    baris = len(array_2d)
    kolom = len(array_2d[0])
    new = kolom * baris
    for index in range(baris):
        array_2d[index] = array_2d[index] + [None] * new
    return array_2d

if __name__ == '__main__':
    l1 = [4, 3, 2, 1]
    my_one = l1.pop(1)
