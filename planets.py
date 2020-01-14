# Use append() to add Jupiter and Saturn at the end of the list.
planet_list = ["Mercury", "Mars"]
# planet_list.append("Jupiter")
# planet_list.append("Saturn")


# Use the extend() method to add another list of the last two planets in our solar system to the end of the list
planet_list2 = ["Saturn", "Jupiter"]
planet_list.extend(planet_list2)

# Use insert() to add Earth, and Venus in the correct order
planet_list.insert(0, "Earth")
planet_list.insert(5, "Venus")
print(planet_list)


# Use append() again to add Pluto to the end of the list
planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets
rocky_planets = slice(1,3,5)
print(planet_list[rocky_planets])

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
planet_list = ["Earth", "Mercury", "Mars", "Saturn", "Jupiter", "Venus", "Pluto" ]
del planet_list[6]
print(planet_list)

