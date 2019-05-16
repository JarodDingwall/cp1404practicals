from prac_8.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Good", 100, 50)
    bad_car = UnreliableCar("Bad", 100, 30)

    print("{} drove {}km".format(good_car.name, good_car.drive(5)))
    print("{} drove {}km".format(bad_car.name, bad_car.drive(5)))

    print(good_car)
    print(bad_car)


main()
