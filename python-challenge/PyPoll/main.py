import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

def write_output_data_to_csv(paramlist, param2, param3):
	output_path = os.path.join(".", "output", "poll_data_analysis.txt")
	with open(output_path, 'a') as txtfile:
    	# Initialize csv.writer
		#csvwriter = csv.writer(csvfile, lineterminator='\n')
		txtfile.write("Election Results" + "\n")
		txtfile.write ("--------------------------------------" + "\n")
		txtfile.write ("Total Votes : {}" . format(paramlist['total_votes']) + "\n")
		txtfile.write ("--------------------------------------" + "\n")
		for i in param2:
			txtfile.write ("{} : {} ({:3.2f}%)". format(i, param2[i], param3[i]) + "\n")
		txtfile.write ("--------------------------------------" + "\n")
		txtfile.write("Winner {}" . format(paramlist['winner']) + "\n")
		txtfile.write ("--------------------------------------" + "\n")


def print_output_to_screen(paramlist, param2, param3):
	print ("Election Results")
	print ("--------------------------------------")
	print ("Total Votes : {}" . format(paramlist['total_votes']))
	print ("--------------------------------------")
	for i in param2:
		print ("{} : {} ({:3.2f}%)". format(i, param2[i], param3[i]))
	print ("--------------------------------------")
	print ("Winner {}" . format(paramlist['winner']))
	print ("--------------------------------------")

def percentage(count, all):
	return (count * 100) / all

# variables
votes_dict = {'Candidate' : []}
candidates = {}
vote_count_dict = {}
votes_percent = {}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and ignore
    csv_header = next(csvreader)

    # iterate over file and collect dates in a list
    for row in csvreader:
    	votes_dict['Candidate'].append(row[2])

vote_count_dict['total_votes'] = len(votes_dict['Candidate'])
# count votes for each candidate
candidate_list = list(set(votes_dict['Candidate']))
for c in candidate_list:
	clist = [candidate for candidate in votes_dict['Candidate'] if candidate == c]
	total_no_votes_candidate = len(clist)
	percent = percentage(total_no_votes_candidate, len(votes_dict['Candidate']))
	candidates[c] = total_no_votes_candidate
	votes_percent[c] = percent

max_votes = max(candidates.values())
winner_name = (list(candidates.keys())[list(candidates.values()).index(max_votes)])
vote_count_dict['winner'] = winner_name

# process data for reports
print_output_to_screen(vote_count_dict, candidates, votes_percent)
write_output_data_to_csv(vote_count_dict, candidates, votes_percent)