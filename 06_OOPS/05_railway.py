'''
class Train:

    def __init__(self,name,noofseats,fare):
        self.name=name
        self.noofseats=noofseats
        self.fare=fare
        self.seats=list(range(1,noofseats+1))

    def getInfo(self):
        print(f'name of train is: {self.name}')
        print(f'The no. of seats are : {self.noofseats}')
        print(f'fare is : {self.fare}')
        print(f'the seats are : {self.seats}')

    def bookASeat(self,no):
        if no>len(self.seats):
            print(f"seats are not available {no - len(self.seats)}")
        elif no<1:
            print()
        else:
            for i in range(no):
                self.seats.pop(0)
            print(f'{no} seats are booked')

    def cancelSeat(self,seatno):
        if seatno<1 or seatno>len(self.seats):
            print("print valid seatno")
        elif seatno in self.seats:
            print(f'the {seatno} is not alloacated yet')
        else:
            self.seats.append(seatno)
            self.seats.sort()
            print(f'the seats available are : {self.seats}')



t1=Train("RE",5,50)
t1.getInfo()
t1.bookASeat(1)
t1.getInfo()
t1.cancelSeat(1)
t1.getInfo()

'''