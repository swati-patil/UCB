# import required modules

import os
import csv

def write_output_data_to_csv(paramlist):
	output_path = os.path.join(".", "output", "output_budget_data.txt")
	with open(output_path, 'a') as txtfile:
    	# Initialize csv.writer
		#csvwriter = csv.writer(csvfile, lineterminator='\n')
		txtfile.write("Financial Analysis" + "\n")
		txtfile.write ("--------------------------------------" + "\n")
		txtfile.write ("Total Months : {}" . format(paramlist['total_months']) + "\n")
		txtfile.write ("Total Amount : $ {}" . format(paramlist['total_amount']) + "\n")
		txtfile.write ("Average Change : $ {0:10.2f}" . format(paramlist['avg_change']) + "\n")
		txtfile.write ("Greatest Decrease in Profits : ${} ({})" . format(paramlist['max_dec'], paramlist['max_dec_month']) + "\n")
		txtfile.write ("Greatest Increase in Profits : ${} ({})" . format(paramlist['min_dec'], paramlist['min_dec_month']) + "\n")
	

def print_output_to_screen(paramlist):
	print ("Financial Analysis")
	print ("--------------------------------------")
	print ("Total Months : {}" . format(paramlist['total_months']))
	print ("Total Amount : $ {}" . format(paramlist['total_amount']))
	print ("Average Change : $ {0:10.2f}" . format(paramlist['avg_change']))
	print ("Greatest Decrease in Profits : ${} ({})" . format(paramlist['max_dec'], paramlist['max_dec_month']))
	print ("Greatest Increase in Profits : ${} ({})" . format(paramlist['min_dec'], paramlist['min_dec_month']))


# variables
ind = 0;
budget_dict = {'Dates' : [], 'Amount' : []}
profit = {}
output_dict = {}

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and ignore
    csv_header = next(csvreader)

    # iterate over file and collect dates in a list
    for row in csvreader:
    	budget_dict['Dates'].append(row[0])
    	amount = int(row[1])
    	budget_dict['Amount'].append(amount)
    	if (ind > 0):
    		profit[row[0]] = budget_dict['Amount'][ind-1] - amount
    	ind = ind + 1

# process data for reports
avg = float(sum(profit.values())) / max(len(profit.values()), 1)
profit_values = list(profit.values())
profit_keys  = list(profit.keys())
max_value_ind = profit_values.index(max(profit_values))
min_value_ind = profit_values.index(min(profit_values))
output_dict['total_months'] = len(budget_dict['Dates'])
output_dict['total_amount'] = sum(budget_dict['Amount'])
output_dict['avg_change'] = avg
output_dict['max_dec'] = max(profit_values)
output_dict['max_dec_month'] = profit_keys[max_value_ind]
output_dict['min_dec'] = min(profit_values)
output_dict['min_dec_month'] = profit_keys[min_value_ind]
print_output_to_screen(output_dict)
write_output_data_to_csv(output_dict)