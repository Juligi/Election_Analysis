print("hello world")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Then, Turn on the AC.")
# else:
#     print("Then, Open the windows.")
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])
# for county in counties_dict.keys():
#     print(county)
# for key, value in counties_dict.items():
#     print(key, value)
# for county, voters in counties_dict.items():
#     print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

for i in range(len(voting_data)):

    print(voting_data[i]['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
