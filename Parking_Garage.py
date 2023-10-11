class Garage():
    """
    Create a parking garage that has the following methods: 
    --takeTicket: 
    -decrease amount of tickets available by 1, 
    -decrease amount of parkingSpaces by 1
    --payForParking: 
    -display an input that waits for an amount from the user and stores it in a 
    variable, 
    -if the payment variable is empty (meaning the ticket has been paid) -> 
    display a message to the user that their ticket has been paid and they have 
    15 mins to leave
    -This should update the "currentTicket" dictionary key "paid" to True
    --leaveGarage:
    -if the ticket has been paid, display a message of "Thank You, have a nice 
    day"
    -if the ticket has not been paid, display an input prompt for payment
    -Once paid, display message "Thank you, have a nice day!"
    -Update parkingSpaces list to increase by 1 (meaning add to the 
    parkingSpaces list)

    attributes: tickets (list), parkingSpaces (list), currentTicket (dictionary)
    """

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        # decrease amount of tickets available by 1
        self.tickets.pop()
        # decrease amount of parking spaces by 1
        self.parkingSpaces.pop()

    def payForParking(self):
        # display input for amount from user and store in variable
        parking_fee = int(input("The hourly rate for parking is $5/hour. For how many hours were you parked here? ")) * 5
        # display amount user owes and ask how much they would like to pay
        print("You owe $" + str(parking_fee) + ".")
        amount_paid = int(input("Please enter how much you will pay now: "))
        if amount_paid == parking_fee or parking_fee == 0:
            print("Your ticket has been paid. You have 15 minutes to exit the garage.")
            self.currentTicket['paid'] = True
            self.leaveGarage()
        else:
            print("You must pay the full amount. Please try again.")
            self.payForParking()
    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you; have a nice day.")
            # 1 parking space has been freed up and added back to list
            self.parkingSpaces.append(len(self.parkingSpaces) + 1)
            # reassign flag as False for next user
            parkingGarage.currentTicket['paid'] = False
        else:
            # if unpaid, send back to payment prompt
            self.payForParking()

tickets = []
parkingSpaces = []
currentTicket = {}
parkingGarage = Garage([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], {'paid': False})

def run():
    while True:
        response = input("What would you like to do? Enter/Pay/Leave/Quit ")

        if response.lower() == 'quit':
            break
        elif response.lower() == 'enter':
            parkingGarage.takeTicket()
        elif response.lower() == 'pay':
            parkingGarage.payForParking()
        elif response.lower() == 'leave':
            parkingGarage.leaveGarage()
        else:
            print("Please choose one of the given options.")
            continue
            
run()