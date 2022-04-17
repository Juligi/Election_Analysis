# In this project, our final Python script will need to be able to deliver the following information when the script is run:
# • Total number of votes cast
# • A complete list of candidates who received votes
# • Total number of votes each candidate received
# • Percentage of votes each candidate won
# The winner of the election based on popular vote

# this was part of the module excersie in 3.4.1
# import datetime
# now = datetime.datetime.now()
# print("the exact time right now is", now)


import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# below is prior coding from lessons

# file_to_load = "Election_Analysis\Resources\election_results.csv"
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')


# Close the file.
# election_data.close()

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()
# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #     # Write some data to the file.
#     #     txt_file.write("Hi World. ")
#     #    # Write three counties to the file.
#     #     txt_file.write("Arapahoe, ")
#     #     txt_file.write("Denver, ")
#     #     txt_file.write("Jefferson")
#    # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:

 # To do: read and analyze the data here.
  # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#  # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

 # Print the header row.
    headers = next(file_reader)
    print(headers)
