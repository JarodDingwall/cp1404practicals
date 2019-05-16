from prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${}".format(taxi.gets_fare()))


main()
