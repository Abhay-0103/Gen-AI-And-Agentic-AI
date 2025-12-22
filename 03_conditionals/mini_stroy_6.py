seat_type = input("Enter seat types (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat selected. Price: 50rs")
    case "ac":
        print("AC seat selected. Price: 100rs")
    case "general":
        print("General seat selected. Price: 30rs")
    case "luxury":
        print("Luxury seat selected. Price: 200rs")
    case _:
        print("Invalid seat type selected.")
