import random

class Garage:

    def __init__(self, tickets = ["ticket1", "ticket2", "ticket3", "ticket4", "ticket5"], parkingSpaces = [101, 102, 103, 104, 105], currentTicket = {}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets:
            ticket_number = f"a{random.randint(1000, 9999)}"
            self.currentTicket[ticket_number] = {
                'ticket': self.tickets.pop(0),
                'parkingSpace': self.parkingSpaces.pop(0),
                'amountPaid': 0,
                'paid': False
            }
            return f"Your ticket number is {ticket_number}"
        else:
            return "Sorry! Parking Garage is full."
    

    def payForParking(self):
        while True:
            ticket_number = input('Please enter your ticket number')
            if ticket_number in self.currentTicket:
                while True:
                    try:
                        paymentInput = int(input('Please pay $10 for parking'))
                        if paymentInput == 10:
                            print("Ticket has been paid and please leave garage within 15 minutes.")
                            break
                    except:
                        print("Enter amount in digits.")
                self.currentTicket[ticket_number]['amountPaid'] = paymentInput
                self.currentTicket[ticket_number]['paid'] = True
                break
            else:
                print("Invalid Ticket Number. Please try again.")

    def leaveGarage(self):
        while True:
            ticket_number = input('Please enter your ticket number')
            if ticket_number in self.currentTicket:
                if self.currentTicket[ticket_number]['paid'] == True:
                    print("Thank You, have a nice day!")
                # ELSE:  if 'paid' == False:
                else:
                    while True:
                        try:
                            paymentInput = int(input('Please pay $10 for parking'))
                            if paymentInput == 10:
                                print("Ticket has been paid. Thank You, have a nice day!")
                                break
                        except:
                            print("Enter amount in digits.")
                    self.currentTicket[ticket_number]['amountPaid'] = paymentInput
                    self.currentTicket[ticket_number]['paid'] = True
                    
                self.tickets.append(self.currentTicket[ticket_number]['ticket'])
                self.parkingSpaces.append(self.currentTicket[ticket_number]['parkingSpace'])
                break
            else:
                print("Invalid Ticket Number. Please try again.")

    def driver(self):
        while True:
            # Take Ticket, Pay For Parking, Leave Garage, Quit
            print("Type\nT to Take Ticket\nP to Pay for Parking\nL to Leave Garage\nQ to Quit.")
            
            input_driver = input("What would you like to do? ").lower()

            if input_driver == 't':
                print(self.takeTicket())

            elif input_driver == 'p':
                self.payForParking()

            elif input_driver == 'l':
                self.leaveGarage()

            elif input_driver == 'q':
                break

            else:
                print("Invalid input. Please try again.")