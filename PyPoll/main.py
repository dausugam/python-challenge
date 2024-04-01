# Import Modules
import os
import csv

# Define the file path name
file_path = os.path.join("Resources","election_data.csv")

# Open CSV File
with open(file_path, mode = "r", encoding = "UTF-8") as csv_file:
    
    # Define reader variable
    reader = csv.reader(csv_file)

    # Skip the first row (header data)
    data_header = next(reader)

    # Stored the cvs file data into lists
    voters_id = []
    counties = []
    candidates = []
    for row in reader:
        voters_id.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# Define the total number of votes
total_votes = len(voters_id)


# Define the vote results:

vote_results = {"Candidates": [], "Votes": [], "Votes %": []}

for item in candidates:
    if item not in vote_results["Candidates"]:
        vote_results["Candidates"].append(item)

for i in range(len(vote_results["Candidates"])):
    vote_results["Votes"].append(int(0))
    for candidate in candidates:
        if vote_results["Candidates"][i] == candidate:
            vote_results["Votes"][i] += 1

for votes in vote_results["Votes"]:
    vote_results["Votes %"].append(round((votes/total_votes)*100,3))


# Print the Summary of the Elections

print(
    "Election Results \n"
    "----------------------------------------- \n"
    f"Total Votes: {total_votes} \n"
    "-----------------------------------------"
)

for i in range(len(vote_results["Candidates"])):
    print(f"{vote_results['Candidates'][i]}: {vote_results['Votes %'][i]}% ({vote_results['Votes'][i]})")

print(
    "----------------------------------------- \n"
    f"Winner: {vote_results['Candidates'][vote_results['Votes'].index(max(vote_results['Votes']))]} \n"
    "-----------------------------------------"
)


# Summary of Election Results in Text File
txt_file_path = os.path.join("analysis", "results.txt")
with open(txt_file_path, "w") as txt_file:
    txt_file.write(
        "Election Results \n"
        "----------------------------------------- \n"
        f"Total Votes: {total_votes} \n"
        "----------------------------------------- \n"
    )

    for i in range(len(vote_results["Candidates"])):
        txt_file.write(f"{vote_results['Candidates'][i]}: {vote_results['Votes %'][i]}% ({vote_results['Votes'][i]}) \n")

    txt_file.write(
        "----------------------------------------- \n"
        f"Winner: {vote_results['Candidates'][vote_results['Votes'].index(max(vote_results['Votes']))]} \n"
        "-----------------------------------------"
    )