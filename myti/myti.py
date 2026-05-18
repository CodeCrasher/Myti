def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Book a new trip")
        print("2. Add a new destination")
        print("3. Display all existing customers")
        print("4. Display all existing customers with membership")
        print("5. Display all valid destinations with their prices")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("You selected Option One.")
            book_new_trip()
        elif choice == '2':
            print("You selected Option Two.")
        elif choice == '3':
            print("You selected Option Three.")
        elif choice == '4':
            print("You selected Option Four.")
        elif choice == '5':
            print("You selected Option Five.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def book_new_trip():

    memberList = {}
    destination_list = ["a", "b", "c", "d", "e"]
    customerName=input("Enter your name:")

    destination_name=input("Enter your destination:")

    if destination_name not in destination_list:
        print("Invalid destination. Please choose from the following options: " + str(destination_list))
        destination_name=input("Enter your destination:")
    memberList.update({customerName: [destination_name]})

 
    try:
        tickets=int(input("Enter number of tickets:"))
        if tickets <= 0:
            print("Invalid number cannot be negative or zero:")
            tickets=input("Enter number of tickets:")
    except ValueError:
        print("Invalid integer")
        tickets=input("Enter number of tickets:")

    tickets=float(tickets)


    unitPrice = float(5)

    member = input("Are you a member? (yes/no):")
    if member.lower() == "yes" or member.lower() == "y" or member.lower() == "no" or member.lower() == "n":
        if member.lower() == "yes" or member.lower() == "y":
            memberList[customerName] = True
            memberList.update({customerName: [destination_name, member]})
        else:
            print("You are not a member. Do you want to become a member?")
            member = input("Enter yes or no:")
            if member.lower() == "yes" or member.lower() == "y":
                memberList[customerName] = True
            memberList.update({customerName: [destination_name, member]})
    else:
        print("Invalid input. Please enter yes or no.")
        member = input("Are you a member? (yes/no):")

    totalPrice = float(unitPrice * tickets)

    member = memberList[customerName][1]

    if customerName in memberList and member.lower() == "yes":
        totalPrice = totalPrice - (5/100*totalPrice)
        print(f"{customerName} books {str(float(tickets))} tickets to {destination_name}.")
        print(f"{customerName} gets a discount of 5%.")
        print("Unit price: " + str(unitPrice) + " AUD")
        print("Total price: " + str(totalPrice) + " AUD")
    else:
        print("Customer is not a member, no discount applied.")
        print(customerName + " books " + str(float(tickets)) + " tickets to " + destination_name + ".")
        print("Unit price: " + str(unitPrice) + " AUD")
        print("Total price: " + str(totalPrice) + " AUD")


    print("Thank you for booking with MyTi!" + str(memberList))
    
main_menu()