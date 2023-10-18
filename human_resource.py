with open("hr_system.txt") as human_resource_file:
    for information in human_resource_file:
        information = information.split(" ")

        print(f"Name: {information[0]}, Title: {information[2]}")

# # or 
# with open("hr_system.txt") as human_resource_file:
#     for information in human_resource_file:
#         information = information.split(" ")

#         name = information[0]
#         title= information[2]

#         print(f"Name: {name}, Title: {title}")

# stretch  challenge
with open("hr_system.txt") as human_resource_file:

    for information in human_resource_file:
        information = information.strip()
        information = information.split(" ")

        name = information[0]
        id = information[1]
        title = information[2]
        salary = float(information[3])

        pay_amount = salary/24
        if title.lower() == "engineer":
           pay_amount += 1000



        print(f"Name: {name} (ID: {id}), {title} - ${pay_amount:.2f}")







        
