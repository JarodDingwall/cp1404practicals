from prac_8.taxi import Taxi
from prac_8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"


def main():
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            taxi_number = 0
            for taxi in taxis:
                print("{} - {}".format(taxi_number, taxi))
                taxi_number += 1
            taxi_choice = int(input("Choose Taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(bill_to_date))
            print(MENU)
            menu_choice = input(">>> ").lower()
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            drive_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, drive_cost))
            bill_to_date += drive_cost
            print("Bill to date: ${:.2f}".format(bill_to_date))
            print(MENU)
            menu_choice = input(">>> ").lower()
        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(bill_to_date))
            print(MENU)
            menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    taxi_number = 0
    for taxi in taxis:
        print("{} - {}".format(taxi_number, taxi))
        taxi_number += 1


main()
