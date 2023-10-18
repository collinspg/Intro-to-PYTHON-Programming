with open("life-expectancy.csv") as data_file:
    next(data_file)
    
    lowest_life_expectancy = float(9999999)
    highest_life_expectancy = float(-1)

    for information in data_file:
        information = information.split(",")

        life_expectancy = float(information[3])
        
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

print(f"Highest value for Life expectancy: {highest_life_expectancy}")
print(f"Lowest value for Life expectancy: {lowest_life_expectancy}")

