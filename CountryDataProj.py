countries = []
with open("CountryData.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()
    for line in all_lines[1:]:
        data = line.strip().split("*")
        current_country ={} # make a dictionary
        current_country["name"] = data[1]
        current_country["pop2026"] = data[2]
        current_country["pop_change_percent"] = data[3]
        current_country["pop_change_num"] = data[4]
        current_country["pop_density"] = data[5]
        current_country["fertility_rate"] = data[8]
        current_country["median_age"] = data[9]
        countries.append(current_country)

while True:
    print("""
[1] Find largest Population increase
[2] Find 'largest' population decrease 
[3] Find countries with a young median population
[4] Find growing Countries
[5] quit
    """)
    choice = input("Enter your choice:")
    if choice == "1":
        largest_so_far = countries[0]
        for current_country in countries:
            current_pop_change = int(current_country["pop_change_num"])
            largest_change_so_far= int(largest_so_far["pop_change_num"])
            if current_pop_change > largest_change_so_far:
                largest_so_far = current_country
        print(f"{largest_so_far['name']} grew by {largest_so_far['pop_change_num']}  ")

    elif choice == "2":
        smallest_so_far = countries[0]
        for current_country in countries:
            current_pop_change = int(current_country["pop_change_num"])
            biggest_loss = int(smallest_so_far["pop_change_num"])
            if current_pop_change < biggest_loss:
                smallest_so_far = current_country
        print(f"{smallest_so_far['name']} shrank by {smallest_so_far['pop_change_num']}  ")
    elif choice == "3":
        how_many = 0
        for current_country in countries:
            current_country_age = float(current_country['median_age'])
            if current_country_age < 25:
                how_many += 1
                print(f"{current_country['name']} is a young country with half the people younger than {current_country['median_age']}  ")
        print(f"There were {how_many} young countries with a lots of people in them")
    elif choice == "4":
        pass
    elif choice == "5":
        break
    else:
        print("Please enter a valid choice")

