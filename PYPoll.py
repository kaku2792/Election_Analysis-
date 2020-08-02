file_to_load = 'Resources/election_result.csv'
election_data = open(file_to_load, 'r')

with open(file_to_load) as election_data:
    print(election_data)
import csv
import os
dir(os)
os.path.join("Resources", "election_result.csv")
file_to_load = os.path.join("Resources", "election_result.csv")
with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")
outfile.close()
    
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
headers = next(file_reader)
print(headers)