import os

class VehiclesShop:
    def __init__(self, stock):
        self.stock = stock

    def InventoryVehicles(self, S, Q):
        self.stock = self.stock-Q
        print("Total Vehicle:", self.stock)
        print("Vehicles Type:", S)

    def customers(self, CN, CP, CE, CL):
        self.CName = CN
        self.CPhone = CP
        self.CEmail = CE
        print("\n\n\tCustomerName:\tCustomerPhone:\tCustomerEmail:")
        print(CL)

    def rentals(self, CN, RD, VT, RBL):
        self.CName = CN
        self.RentalDate = RD
        self.VehicleType = VT
        print("\n\n\tCustomerName:\tRentalDate:\tVehicalType:")
        print(RBL)

S = {'Bike': 2, 'Cycle': 3, 'Car': 1, 'Boat': 2}
CL = ""
RBL = ""
N = 0

while True:
    obj = VehiclesShop(8)
    K = int(input('''
1 Add Customers
2 Add Rental Booking
3 See Customer List
4 See Rental Booking List
5 See Inventory of Vehicles Available
6 Clear Screen
7 EXIT
                '''))
    if K == 1:
        try:
            CN = str(input("CustomerName:"))
            CP = int(input("CustomerPhone:"))
            CE = str(input("CustomerEmail:"))
            CL += f'\n\n\t{CN}\t\t{CP}\t\t{CE}'
            print("\nYou have successfully added customer.")
        except:
            print("\nInvalid customer details")
        #obj.customers(CN,CP,CE)
    elif K == 2:
        try:
            CN = str(input("CustomerName:"))
            RD = str(input("RentalDate:"))
            VT = str(input("VehicalType:"))
            if S[VT] > 0:
                RBL += f'\n\n\t{CN}\t\t{RD}\t\t{VT}'
                if VT in S:
                    S[VT] = S[VT]-1
                    N += 1
                    print("\nYou have Successfully booked")
                    print("\nRemaining vehicales type:",S)
            else:
                print("\n",VT,"cannot be rented as it is already booked")
                print("\nBecause\nRemaining vehicales type:",S)
        except:
            print("\nInvalid rental details")
        #obj.rentals(CN,RD,VT)
    elif K == 3:
        try:
            obj.customers(CN, CP, CE, CL)
        except:
            print("\nNo any customer yet.")
    elif K == 4:
        if N > 0:
            obj.rentals(CN, RD, VT, RBL)
        else:
            print("\nNo any rental booking yet.")
    elif K == 5:
        obj.InventoryVehicles(S, N)
    elif K == 6:
        os.system('cls')
    elif K == 7:
        break
    else:
        print("You have enter invalid key.")
        
