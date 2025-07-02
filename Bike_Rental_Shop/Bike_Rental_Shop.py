import datetime
from datetime import datetime, timedelta
    
class BikeRental:

    DailyBikesRented = int(0)
    DailyRevenueCollected = float(0)
    
    def __init__(self,MountainStock=0, RoadStock=0, TouringStock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.MountainStock = MountainStock 
        self.RoadStock = RoadStock
        self.TouringStock = TouringStock
        


    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("We have currently {} Mountain bikes available to     rent.".format(self.MountainStock))
        print("We have currently {} Road bikes available to         rent.".format(self.RoadStock))
        print("We have currently {} Touring bikes available to      rent.".format(self.TouringStock))
        return self.MountainStock, self.RoadStock, self.TouringStock

    def rentBikeOnHourlyBasis(self, n, BikeType):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        if BikeType != "Mountain" and BikeType != "Road" and BikeType != "Touring":
            print("Bike type entered must be Mountain, Road or Touring")
            return None

        # Check if Mountain bike

        if BikeType == "Mountain":
            if n > self.MountainStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} Mountain bike(s) on hourly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $5 for each hour per bike.")
                print("We hope that you enjoy our service.")
                self.MountainStock -= n
                self.DailyBikesRented += n
                return now    
        
        # Check if Road bike
        if BikeType == "Road":
            if n > self.RoadStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} road bike(s) on hourly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $5 for each hour per bike.")
                print("We hope that you enjoy our service.")
                self.RoadStock -= n
                self.DailyBikesRented += n
                return now    

        # Check if Touring Bike
        if BikeType == "Touring":
            if n > self.TouringStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} touring bike(s) on hourly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $5 for each hour per bike.")
                print("We hope that you enjoy our service.")
                self.TouringStock -= n
                self.DailyBikesRented += n
                return now    
        

                      
     
    def rentBikeOnDailyBasis(self, n, BikeType):
        """
        Rents a bike on daily basis to a customer.
        """
          # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        if BikeType != "Mountain" and BikeType != "Road" and BikeType != "Touring":
            print("Bike type entered must be Mountain, Road or Touring")
            return None

        # Check if Mountain bike

        if BikeType == "Mountain":
            if n > self.MountainStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} Mountain bike(s) on daily basis today at {} hours.".format(n,now.hour))
                print("You will be charged $20 for each day per bike.")
                print("We hope that you enjoy our service.")
                self.MountainStock -= n
                self.DailyBikesRented += n
                return now   
        
         # Check if Road bike
        if BikeType == "Road":
            if n > self.RoadStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} road bike(s) on daily basis today at {} hours.".format(n,now.hour))
                print("You will be charged $20 for each day per bike.")
                print("We hope that you enjoy our service.")
                self.RoadStock -= n
                self.DailyBikesRented += n
                return now    

        # Check if Touring Bike
        if BikeType == "Touring":
            if n > self.TouringStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} touring bike(s) on daily basis today at {} hours.".format(n,now.hour))
                print("You will be charged $20 for each day per bike.")
                print("We hope that you enjoy our service.")
                self.TouringStock -= n
                self.DailyBikesRented += n
                return now    
      
    
      
        
    def rentBikeOnWeeklyBasis(self, n, BikeType):
        """
        Rents a bike on weekly basis to a customer.
        """
          # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        if BikeType != "Mountain" and BikeType != "Road" and BikeType != "Touring":
            print("Bike type entered must be Mountain, Road or Touring")
            return None

        # Check if Mountain bike

        if BikeType == "Mountain":
            if n > self.MountainStock:
                print("Sorry! We have currently {} mountain bikes available to rent.".format(self.MountainStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} Mountain bike(s) on weekly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $60 for each week per bike.")
                print("We hope that you enjoy our service.")
                self.MountainStock -= n
                self.DailyBikesRented += n
                return now   

         # Check if Road bike
        if BikeType == "Road":
            if n > self.RoadStock:
                print("Sorry! We have currently {} road bikes available to rent.".format(self.RoadStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} road bike(s) on weekly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $60 for each week per bike.")
                print("We hope that you enjoy our service.")
                self.RoadStock -= n
                self.DailyBikesRented += n
                return now    

        # Check if Touring Bike
        if BikeType == "Touring":
            if n > self.TouringStock:
                print("Sorry! We have currently {} touring bikes available to rent.".format(self.TouringStock))
                return None
            else:
                now = datetime.now()                      
                print("You have rented a {} touring bike(s) on weekly basis today at {} hours.".format(n,now.hour))
                print("You will be charged $60 for each week per bike.")
                print("We hope that you enjoy our service.")
                self.TouringStock -= n
                self.DailyBikesRented += n
                return now    
        
    
    def returnBike(self, request, BikeType, DiscountCoupon):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        billBeforeDiscount = 0
        TotalDiscount = 0
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            if BikeType == "Mountain":
                self.MountainStock += numOfBikes
            elif BikeType == "Road":
                self.RoadStock += numOfBikes
            elif BikeType == "Touring":
                self.TouringStock += numOfBikes
            now = datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
               
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
                
            billBeforeDiscount = bill
            # Discount Coupon
            if DiscountCoupon == "Y":
                print("your coupon is valid for a 10% discount")
                bill = bill * 0.9
                TotalDiscount = "10%"
            else:
                print("Your coupon is invalid and will not affect final rental cost")

            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
                TotalDiscount = "30%"
               
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            self.DailyRevenueCollected += bill
            return bill
        
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    def __init__(self, strFirstName, strLastName, strIDNumber):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.strFirstName = strFirstName
        self.strLastName = strLastName
        self.strIDNumber = strIDNumber
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.biketype = ""
        self.discountcoupon = ""
        self.bill = 0
        self.billBeforeDiscount = 0
        self.TotalDiscount = 0
    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
        


# Navigational Menu
Customers = []
strInputValidated = bool(False)
# Establishes shop name and inventory of each type of bike
while strInputValidated is bool(False):
    Shop = str(input("Please enter the name of your Bike Shop: "))
    if Shop == "":
        print("Must enter shop name")
    else:
        strInputValidated = bool(True)

strInputValidated = bool(False)

while strInputValidated is bool(False):
    Mountain = input("Enter mountain bike inventory: ")
    try:
        Mountain = int(Mountain)
        if Mountain >= 0:
            strInputValidated = bool(True)
        else:
            print("Number must be greater than or equal to 0")
            strInputValidated = bool(False)
    except ValueError:
        print("Must enter a numerical value")
        strInputValidated = bool(False)

strInputValidated = bool(False)
while strInputValidated is bool(False):
    Road = input("Enter road bike inventory: ")
    try:
        Road = int(Road)
        if Road >= 0:
            strInputValidated = bool(True)
        else:
            print("Number must be greater than or equal to 0")
            strInputValidated = bool(False)
    except ValueError:
        print("Must enter a numerical value")
        strInputValidated = bool(False)
strInputValidated = bool(False)
while strInputValidated is bool(False):
    Touring = input("Enter Touring bike inventory: ")
    try:
        Touring = int(Touring)
        if Touring >= 0:
            strInputValidated = bool(True)
        else:
            print("Number must be greater than or equal to 0")
            strInputValidated = bool(False)
    except ValueError:
        print("Must enter a numerical value")
        strInputValidated = bool(False)

Shop = BikeRental(Mountain, Road, Touring)

endprogram = bool(False)
IDNumber = int(-1)
while endprogram is bool(False):
    strInputValidated = bool(False)
 # Navigational Selection
    while strInputValidated is bool(False):
       Direction = input("Select one of the following options to proceed.  New Customer Rental(1), Rental Return(2), Show Inventory(3), End of Day(4), or Exit Program(5): ")
       if Direction != "1" and Direction != "2" and Direction != "3" and Direction != "4" and Direction != "5":
           print("Must enter within the options of 1,2,3,4, or 5")
           strInputValidated = bool(False)
       else:
           strInputValidated = bool(True)

    strInputValidated = bool(False)

    intCustomerCount = int(0)
    
# New Customer Rental Navigation
    if Direction == "1":
        while strInputValidated is bool(False):
            FirstName = str(input("Please enter First Name: "))
            if FirstName == "":
                print("Must enter first name")
                strInputValidated = bool(False)
            else:
                strInputValidated = bool(True)
        strInputValidated = bool(False)
        while strInputValidated is bool(False):
            LastName = str(input("Please enter Last Name: "))
            if LastName == "":
                print("Must enter last name")
                strInputValidated = bool(False)
            else:
                strInputValidated = bool(True)
        
        DiscountCoupon = str(input("Enter Discount Coupon Code for to receive 10% of total rental: "))
        strInputValidated = bool(False)
        while strInputValidated is False:
            RentalBasis = input("Please enter the rental basis for your order, options are hourly(1), daily(2) or weekly(3).  Enter the number corresponding to your answer: ")
            if RentalBasis != "1" and RentalBasis != "2" and RentalBasis != "3":
                print("Must enter 1, 2 or 3 for rental options")
            else:
                strInputValidated = bool(True)

        strInputValidated = bool(False)

        while strInputValidated is bool(False):
            BikeType = str(input("What type of bike would you like to rent? Options are Mountain, Road or Touring: "))
            if BikeType != "Mountain" and BikeType != "Road" and BikeType != "Touring":
                print("Must enter Mountain, Road or Touring for bike type.")
            else:
                strInputValidated = bool(True)

        strInputValidated = bool(False)
        while strInputValidated is bool(False):
            NumberOfBikes = int(input("How many bikes would you like to rent? "))
    
            if RentalBasis == "1":
                if Shop.rentBikeOnHourlyBasis(NumberOfBikes, BikeType) == None:
                    strInputValidated = bool(False)
                else:
                    strInputValidated = bool(True)
            elif RentalBasis == "2":
                if Shop.rentBikeOnDailyBasis(NumberOfBikes, BikeType) == None:
                    strInputValidated = bool(False)
                else:
                    strInputValidated = bool(True)
            elif RentalBasis == "3":
                if Shop.rentBikeOnWeeklyBasis(NumberOfBikes, BikeType) == None:
                    strInputValidated = bool(False)
                else:
                    strInputValidated = bool(True)
        IDNumber += 1
    

# Sets the name, Id number, rental basis and time
        customer = Customer(FirstName, LastName, IDNumber)
        customer.bikes = NumberOfBikes
        customer.rentalBasis = RentalBasis
        customer.rentalTime = datetime.now()
        customer.strFirstName = FirstName
        customer.strLastName = LastName
        customer.strIDNumber = IDNumber
        customer.biketype = BikeType
    

# Determines if coupon is valid
        ending = DiscountCoupon[-3:]
        if ending == "BBP":
            customer.discountcoupon = "Y"
        else:
            customer.discountcoupon = "N"

        NewCustomer = [customer.biketype, customer.bikes, customer.rentalBasis, customer.discountcoupon]

       
        Customers.append(Customer(customer.strFirstName, customer.strLastName, customer.strIDNumber))
        endprogram = bool(False)
        
   

 #   Customers.append(FirstName, LastName, IDNumber, Customers.biketype, Customers.bikes, RentalBasis, Customers.rentalTime, Customers.discountcoupon )

# Rental Return Navigation
    Index = int(0)
    if Direction == "2":
       # print(Customers[0])
       # print(Customers[1])
        strInputValidated = bool(False)
        while strInputValidated is bool(False):
            ID = input("Provide customer ID to view specific rental details.  ID starts at 0 for the first customer and increments by 1 for every new customer throughtout the day: ")
            try:
                ID = int(ID)
                if ID >= 0:
                    strInputValidated = bool(True)
                else:
                    print("ID must be greater than or equal to 0")
                    strInputValidated = bool(False)
            except ValueError:
                print("Must enter a numerical value")
                strInputValidated = bool(False)
            request5 = customer.returnBike()
            if Shop.returnBike(request5, customer.biketype, customer.discountcoupon) == None:
                strInputValidated = bool(False)
            else:
                print("")
                print("Return details")
                print("")
                print("Customer Name: ", Customers[ID].strFirstName, ", ", Customers[ID].strLastName)
                print("Number of bikes rented: ", customer.bikes)
                print("Bike Type: ", customer.biketype)
        
                print("Total Before Discount: ", customer.billBeforeDiscount)
        
    if Direction == "3":
        print("")
        print("Bike Shop Inventory")
        print("")
        print(Shop.displaystock())

    if Direction == "4":
        print("")
        print("Total Bikes Rented for the Day: ", Shop.DailyBikesRented)
        print("Total Revenue Collected for Day: ", Shop.DailyRevenueCollected)
        print("")

    if Direction == "5":
        endprogram = bool(True)
        
