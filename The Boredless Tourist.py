# Tien Phan
# The Boredless Tourist Project

# definitions
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]
attractions = [[] for destination in destinations]

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


def add_attraction(destination, attraction):
    # this stores the index of the destination to destination index
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        return print("The destination is not in the list")

    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)

    return attractions_for_destination

# function testers
#test_destination_index = get_traveler_location(test_traveler)
#print(get_destination_index("Hyderabad, India"))
#print(test_destination_index)
#print(attractions)
print(add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]]))
#print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)