print("Hello World")
print(type('True'))
num_canidates = 3
winning_percentage = 73.81
canidate = "Diane"
won_election = True
print("Counties")
Counties = ["Arapahoe" ,"Denver", "Jefferson"]
my_list = list(Counties)
print("Counties[0]")
print("Counties[2]")
print("Counties[-1]")
len(Counties)
Counties[0:2]
['Arapahoe', 'Denver']
Counties.append("El Paso")
Counties.insert(2, "El Paso")
Counties.remove("El Paso")
Counties
Counties_tuple = ("Arapahoe","Denver","Jefferson")
len(Counties_tuple)
Counties_tuple[1]
my_dictionary = dict()
Counties_dict = {}
Counties_dict["Arapahoe"] = 422829
Counties_dict["Denver"] = 463353
Counties_dict["Jefferson"] = 432438
len(Counties_dict)
Counties_dict.items()
Counties_dict.keys()
Counties_dict.values()
Counties_dict.get("Denver")
Counties_dict["Arapahoe"]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

Counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in Counties:
    print("El Paso is in the list of Counties.")
else:
    print("El Paso is not the list of Counties.")


if "Arapahoe" in Counties and "El Paso" in Counties:
    print("Arapahoe and El Paso are in the list of Counties.")
else:

    print("Arapahoe or El Paso is not in the list of Counties.")  
if "Arapahoe" in Counties or "El Paso" in Counties:
    print("Arapahoe or El Paso is in the list of Counties.")
else:
    print("Arapahoe and El Paso are not in the list of Counties.")


x = 0
while x <= 5:
    print(x)
    x = x + 1


for County in Counties:
  print(County)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)


for i in range(len(Counties)):
    print(Counties[i])

for county in Counties_dict.keys():
    print(County) 


for voters in Counties_dict.values():
    print(voters)

for County in Counties_dict:
    print(Counties_dict.get(County))

for County, voters in Counties_dict.items():
    print(County, voters)

voting_data = [{"County":"Arapahoe", "registered_voters": 422829},
                {"County":"Denver", "registered_voters": 463353},
                {"County":"Jefferson", "registered_voters": 432438}]

for County_dict in voting_data:
    print(County_dict)



for County_dict in voting_data:
    for value in County_dict.values():
        print(value) 


for County_dict in voting_data:
    print(County_dict['County'])


Counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for County, voters in Counties_dict.items():
    print(County + " County has " + str(voters) + " registered voters.")


for County, voters in Counties_dict.items():
    print(f"{County} County has {voters} registered voters.")



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")


