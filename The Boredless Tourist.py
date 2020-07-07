# Tien Phan
# The Boredless Tourist Project

# definitions
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


def get_destination_index(destination):
    destination_index = ""
    try:
        destination_index = destinations.index(destination)
    except ValueError:
        print("The destination is not in the list")

    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = ""

    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(get_destination_index("Hyderabad, India"))
print(test_destination_index)

