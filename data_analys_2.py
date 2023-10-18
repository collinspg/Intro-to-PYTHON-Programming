with open("life-expectancy.csv") as data_file:
    lines = data_file.readlines()[1:]
    
    lowest_life_expectancy = float(9999999)
    highest_life_expectancy = float(-1)
    lowest_country = ""
    highest_country = ""
   
    for information in lines:
        information = information.split(",")

        life_expectancy = float(information[3])
        country = information[0]
        year = information[2]
        
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_country = country
            lowest_year = year

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_country = country
            highest_year = year
    
    print()
    year_of_interest = input("Enter the year of interest: ")
    life_expectancies = []
    countries = []
    year_found = False

    for information in lines:
        information = information.split(",")

        life_expectancy = float(information[3])
        country = information[0]
        year = information[2]

        if year == year_of_interest:
            life_expectancies.append(life_expectancy)
            countries.append(country)
            year_found = True

    if year_found:
        average_life_expectancy = sum(life_expectancies) / len(life_expectancies)
        max_index = life_expectancies.index(max(life_expectancies))
        min_index = life_expectancies.index(min(life_expectancies))

        # Showing Creativity and Exceeding Requirements codes

        largest_drop = float(-1)
        largest_country_drop = ""
        largest_year_drop = ""

        for i in range(1, len(lines)):
            current_information = lines[i].split(",")
            previous_information = lines[i - 1].split(",")

            current_life_expectancy = float(current_information[3])
            previous_life_expectancy = float(previous_information[3])
            current_country = current_information[0]
            current_year = current_information[2]
            previous_year = previous_information[2]

            drop = current_life_expectancy - previous_life_expectancy

            if drop < largest_drop:
                largest_drop = drop
                largest_drop_year = current_year
                largest_drop_country = current_country
        # End of Showing Creativity and Exceeding Requirements codes

        print()        
        print(f"The overall max life expectancy is: {highest_life_expectancy} from {highest_country} in {highest_year}")
        print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_country} in {lowest_year}")
        print()
        print(f"For the year {year_of_interest}:\nThe average life expectancy across all countries was {average_life_expectancy:.2f}")
        print(f"The max life expectancy was in {countries[max_index]} with {max(life_expectancies)}")
        print(f"The min life expectancy was in {countries[min_index]} with {min(life_expectancies)}")
        
        # print Showing Creativity and Exceeding Requirements codes
        # The abs() function shows the drop as a positive number regardless of whether it is negative or positive.
        print()
        print(f"The largest drop was in {largest_drop_country} in {largest_drop_year} with a drop of {abs(largest_drop):.2f} years")  
    else:
        print(f"There are no available data for the year {year_of_interest}.")