from importlib.abc import Traversable

destinations = [
    'Paris, France',
    'Shanghai, China',
    'Los Angeles, USA',
    'São Paulo, Brazil',
    'Cairo, Egypt'
]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    # we model our example on test_traveler, as all will be formatted in the same way:
    traveler_destination = traveler[1] # traveler_destination = 'Shanghai, China'
    traveler_destination_index = get_destination_index(traveler_destination) # traveler_destination_index = get_destination_index('Shanghai, China') = destinations.index('Shanghai, China') = 1
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler) # = traveler_destination_index = 1

attractions = [[] for destination in destinations] # = [[], [], [], [], []]

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination) # lets say here destination_index = 2
    # we locate the attractions_for_destination as being in one list of the attractions list, located at the index previously mentionned:
    attractions_for_destination = attractions[destination_index] # = attractions[2]
    # we append to this new list placed at attractions[2], the attraction passed in arguments of add_attraction(destination, attraction)
    attractions_for_destination.append(attraction) 
    return attractions

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] + ": the "
    for traveler_attraction in traveler_attractions:
        interests_string += traveler_attraction
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]
)
print(smills_france)