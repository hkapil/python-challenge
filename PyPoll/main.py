# Import Resources
import os
import csv

#Set File Path
csvpath = os.path.join( 'Resources', 'election_data.csv')

#Open 
with open(csvpath, newline='') as csvfile:

# Read File
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #Set initial values in variable before file read loop
    candidate_tot_won=[]
    candidate_list=[]
    voter_count = 0
    
    # Read each row of data after the header
    for row in csvreader:
        # Calculate total voters
        voter_count += 1
        
        candidate = row[2]
        if candidate in candidate_list:
            candidate_tot_won[candidate_list.index(candidate)] += 1
        else:
            candidate_list.append(candidate)
            candidate_tot_won.append(1)


  # Get Total Votes and find Winner Loop
    prev_candidate_won = 0
    #tot_votes=0
    for i in range (0,len(candidate_list)):
       
    #    tot_votes = tot_votes + candidate_tot_won[i]
        if candidate_tot_won[i] > prev_candidate_won:
            candidate_won_index = i
            prev_candidate_won = candidate_tot_won[i]

    #Print on screen and file
    prints = 0
    while prints < 2:
        if prints == 1:
            import sys
            f = open('PyPoll_summary.txt', 'w')
            sys.stdout = f
        
        print ("Election Results")
        print ("___________________________________")
        print(f"Total Voters :  {str(voter_count)}")
        print ("___________________________________")
    
    # loop to print candidates, percentage won and total votes

        for i in range(0,len(candidate_list)):
            per_won = "{:.0%}".format((candidate_tot_won[i]/voter_count))

            print(f" {candidate_list[i]} : {per_won}  ({candidate_tot_won[i]})")
       
        print ("___________________________________")
        print ("")
        print(f"Winner : {candidate_list[candidate_won_index]}")
        print ("___________________________________")
        prints += 1

