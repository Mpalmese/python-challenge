import os
import csv

total_votes = 0
candidate_set = set()
count0 = 0
count1 = 0
count2 = 0
count3 = 0

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        if int(row[0]) >= 0:
            total_votes = total_votes + 1
            candidate_set.add(row[2])
        candidate_list = list(candidate_set)
        candidate_list.sort()
        
        if row[2] == candidate_list[0]:
            count0 = count0 + 1
        elif row[2] == candidate_list[1]:
            count1 = count1 + 1
        elif row[2] == candidate_list[2]:
            count2 = count2 + 1
        elif row[2] == candidate_list[3]:
            count3 = count3 + 1

    candidate_votes = [count0, count1, count2, count3]
    
    candidate_percent0 = round(count0 / total_votes * 100,3)
    candidate_percent1 = round(count1 / total_votes * 100,3)
    candidate_percent2 = round(count2 / total_votes * 100,3)
    candidate_percent3 = round(count3 / total_votes * 100,3)

    winner_votes = max(candidate_votes)

    if winner_votes == count0:
        winner = candidate_list[0] 
    elif winner_votes == count1:
        winner = candidate_list[1] 
    elif winner_votes == count2:
        winner = candidate_list[2] 
    elif winner_votes == count3:
        winner = candidate_list[3] 
    

    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    print(f"{candidate_list[1]}: {candidate_percent1}% ({candidate_votes[1]})") 
    print(f"{candidate_list[0]}: {candidate_percent0}% ({candidate_votes[0]})") 
    print(f"{candidate_list[2]}: {candidate_percent2}% ({candidate_votes[2]})") 
    print(f"{candidate_list[3]}: {candidate_percent3}% ({candidate_votes[3]})") 
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")
    
    output_file = os.path.join("Election Results.txts")

    with open(output_file,'w') as text:

        text.write("Election Results\n")
        text.write("---------------------\n")
        text.write(f"Total Votes: {total_votes}\n")
        text.write("---------------------\n")
        text.write(f"{candidate_list[1]}: {candidate_percent1}% ({candidate_votes[1]})\n") 
        text.write(f"{candidate_list[0]}: {candidate_percent0}% ({candidate_votes[0]})\n") 
        text.write(f"{candidate_list[2]}: {candidate_percent2}% ({candidate_votes[2]})\n") 
        text.write(f"{candidate_list[3]}: {candidate_percent3}% ({candidate_votes[3]})\n") 
        text.write("---------------------\n")
        text.write(f"Winner: {winner}\n")
        text.write("---------------------\n")
         



    
            
    

