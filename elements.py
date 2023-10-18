people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
 
youngest_age = 99
youngest_name = ""

for individuals in people:
    individuals = individuals.split()

    name = individuals[0]
    age = int(individuals[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The youngest pesron is {youngest_name} with an age of {youngest_age}")
