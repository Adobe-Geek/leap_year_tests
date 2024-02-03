def liters_100km_to_miles_gallon(liters):
    miles_to_gallon = (100 / liters) * (3.785411784 / 1.609344)
    return miles_to_gallon


def miles_gallon_to_liters_100km(miles):
    liters_100km = (1 / miles) * (3.785411784 / 0.01609344)
    return liters_100km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
