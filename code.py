import datetime

# Greeting and name
name = input("Enter your name: ")

hour = datetime.datetime.now().hour
print("Time =", hour)

if 12 <= hour < 16:
    print("Good afternoon")
elif 6 <= hour < 12:
    print("Good morning")
elif 16 <= hour < 20:
    print("Good evening")
elif 20 <= hour <= 23:
    print("Good night sir")

print(f"Hello {name}, Thank you for coming to YELCHIKO HOTEL - BANARAS")
print("How may we assist you?")

class TotalCharges:
    def __init__(self, rate=0, roomRent=0, pool=0, gym=0, restaurant=0,
                 laundry=0, name="", address="", checkinDate="", checkoutDate="",
                 roomNum=426):
        print("\n\n$$$$WELCOME TO HOTEL Yelchiko$$$$\n\n")
        self.rate = rate
        self.roomRent = roomRent
        self.pool = pool
        self.restaurant = restaurant
        self.laundry = laundry
        self.name = name
        self.address = address
        self.checkinDate = checkinDate
        self.checkoutDate = checkoutDate
        self.roomNum = roomNum
        self.gym = gym

    def data_input(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.checkinDate = input("Enter your Check-in date: ")
        self.checkoutDate = input("Enter your Check-out date: ")

    def room_rent(self):
        print("Following are our available room types:-")
        print("1. Suite room is 3000 Rs per night")
        print("2. Super deluxe is 2500 Rs per night")
        print("3. Deluxe room is 1500 Rs per night")
        print("4. Dormitory is 600 Rs per night")
        print("5. Exit to Main Menu\n")

        while True:
            try:
                roomChoice = int(input("Please enter your choice of room: "))
                num_nights = int(input("Enter your stay duration (Number of nights): "))
                break
            except ValueError:
                print("Enter valid numbers for choice and nights.")

        if roomChoice == 1:
            print("You have selected the Suite room")
            self.roomRent = 3000 * num_nights
        elif roomChoice == 2:
            print("You have selected the Super deluxe room")
            self.roomRent = 2500 * num_nights
        elif roomChoice == 3:
            print("You have selected the Deluxe room")
            self.roomRent = 1500 * num_nights
        elif roomChoice == 4:
            print("You have selected the Dormitory")
            self.roomRent = 600 * num_nights
        elif roomChoice == 5:
            return
        else:
            print("Invalid choice. Returning to main menu.")
            return

        print(f"Your room rent is Rs.{self.roomRent}\n")

    def restaurant_bill(self):
        print("### Restaurant Menu ###")
        print("1) Water --- Rs.20")
        print("2) Tea --- Rs.10")
        print("3) Coffee --- Rs.15")
        print("4) Chinese Combo --- Rs.60")
        print("5) Lunch combo --- Rs.90")
        print("6) Dinner Combo --- Rs.110")
        print("7) Fasting combo --- Rs.75")
        print("8) Exit to main menu\n")

        while True:
            try:
                x = int(input("Enter your choice of menu: "))
            except ValueError:
                print("Invalid entry. Enter a number.")
                continue

            if x == 1:
                y = int(input("Enter the quantity: "))
                self.restaurant += 20 * y
            elif x == 2:
                y = int(input("Enter the quantity: "))
                self.restaurant += 10 * y
            elif x == 3:
                y = int(input("Enter the quantity: "))
                self.restaurant += 15 * y
            elif x == 4:
                y = int(input("Enter the quantity: "))
                self.restaurant += 60 * y
            elif x == 5:
                y = int(input("Enter the quantity: "))
                self.restaurant += 90 * y
            elif x == 6:
                y = int(input("Enter the quantity: "))
                self.restaurant += 110 * y
            elif x == 7:
                y = int(input("Enter the quantity: "))
                self.restaurant += 75 * y
            elif x == 8:
                break
            else:
                print("Invalid entry")
                continue

        print(f"Total restaurant bill is Rs.{self.restaurant}\n")

    def swimming_pool(self):
        print("Swimming Pool")
        print("Pool usage charges are per hour.")
        print("1) Adult --- 50 Rs")
        print("2) Children --- 20 Rs")
        print("3) Exit to main menu\n")

        while True:
            try:
                p = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid entry. Enter a number.")
                continue

            if p == 1:
                q = int(input("No. of hours: "))
                self.pool += 50 * q
            elif p == 2:
                q = int(input("No. of hours: "))
                self.pool += 20 * q
            elif p == 3:
                break
            else:
                print("Invalid entry")
                continue

        print(f"Total pool bill is Rs.{self.pool}\n")

    def laundry_bill(self):
        print("+++ LAUNDRY MENU +++")
        print("1) Pants/shirts --- Rs.10")
        print("2) 3-piece suit --- Rs.150")
        print("3) Saree --- Rs.20")
        print("4) Blazer --- Rs.100")
        print("5) Exit\n")

        while True:
            try:
                l = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid entry. Enter a number.")
                continue

            if l == 1:
                m = int(input("Enter the quantity: "))
                self.laundry += 10 * m
            elif l == 2:
                m = int(input("Enter the quantity: "))
                self.laundry += 150 * m
            elif l == 3:
                m = int(input("Enter the quantity: "))
                self.laundry += 20 * m
            elif l == 4:
                m = int(input("Enter the quantity: "))
                self.laundry += 100 * m
            elif l == 5:
                break
            else:
                print("Invalid entry")
        print(f"Total laundry cost is Rs.{self.laundry}\n")

    def gym_bill(self):
        print("GYM")
        print("Gym usage is charged per hour (max 2 hours per day)")
        while True:
            try:
                k = int(input("Enter the number of hours (0 to exit): "))
            except ValueError:
                print("Invalid entry. Enter a number.")
                continue

            if k == 0:
                break
            if k > 2:
                print("MAXIMUM time for workout is 2 hours")
            else:
                self.gym += 100 * k
                print(f"Gym charge added: Rs.{100 * k}")
                break

    def finalBill(self):
        print("\n--- HOTEL YELCHIKO ---")
        print("      --- BILL ---      ")
        print(f"Customer Name: {self.name}")
        print(f"Customer Address: {self.address}")
        print(f"Check-in date: {self.checkinDate}")
        print(f"Check-out date: {self.checkoutDate}")
        print(f"Room number: {self.roomNum}")
        print(f"Your room rent amount: Rs.{self.roomRent}")
        print(f"Your food bill amount: Rs.{self.restaurant}")
        print(f"Your pool usage charges: Rs.{self.pool}")
        print(f"Your gym usage charges: Rs.{self.gym}")
        print(f"Your laundry bill amount: Rs.{self.laundry}")
        self.rate = self.roomRent + self.restaurant + self.pool + self.laundry + self.gym
        print(f"Your total bill amount is: Rs.{self.rate}")
        gst = self.rate * 0.18
        print(f"GST charges of 18%: Rs.{gst}")
        print(f"Your grand total bill amount is Rs.{self.rate + gst}")
        self.roomNum += 1

def main():
    a = TotalCharges()
    while True:
        print("\n1. Enter Customer Details")
        print("2. Calculate room rent")
        print("3. Calculate restaurant bill")
        print("4. Calculate pool usage charges")
        print("5. Calculate laundry charges")
        print("6. Calculate gym usage charges")
        print("7. Show total charges")
        print("8. Exit")

        try:
            b = int(input("\nEnter your choice: "))
        except ValueError:
            print("Enter a valid choice (number).")
            continue
        if b == 1:
            a.data_input()
        elif b == 2:
            a.room_rent()
        elif b == 3:
            a.restaurant_bill()
        elif b == 4:
            a.swimming_pool()
        elif b == 5:
            a.laundry_bill()
        elif b == 6:
            a.gym_bill()
        elif b == 7:
            a.finalBill()
        elif b == 8:
            print("Thank you for visiting!")
            break
        else:
            print("Enter a valid menu option (1-8).")

main()
