def calculate_parking_charges(vehicle_type, hours):
    if vehicle_type == 't':
        charge = 20 * hours
    elif vehicle_type == 'c':
        charge = 10 * hours
    elif vehicle_type == 'b':
        charge = 5 * hours
    else:
        return "Invalid vehicle type"
    
    return charge

vehicle_type = input("Enter the type of vehicle (t for Truck/bus, c for Car, b for Cycle/Bike): ").lower()
hours = int(input("Enter the number of hours: "))

charges = calculate_parking_charges(vehicle_type, hours)
if isinstance(charges, int):
    print(f"The parking charges are: Rs.{charges}")
else:
    print(charges)
