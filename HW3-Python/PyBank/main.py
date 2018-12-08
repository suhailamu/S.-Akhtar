from __future__ import division
# https://stackoverflow.com/questions/10768724/why-does-python-return-0-for-simple-division-calculation
import csv


def analyze():
    """
        Task:
        
        The total number of months included in the dataset
        The total net amount of "Profit/Losses" over the entire period
        The average change in "Profit/Losses" between months over the entire period
        The greatest increase in profits (date and amount) over the entire period
        The greatest decrease in losses (date and amount) over the entire period
        
        Sample output to screen AND text file: 
        
        Financial Analysis
        ----------------------------
        Total Months: 86
        Total: $38382578
        Average  Change: $-2315.12
        Greatest Increase in Profits: Feb-2012 ($1926159)
        Greatest Decrease in Profits: Sep-2013 ($-2196167)

    """
    f = open('budget_data.csv')
    reader = csv.DictReader(f)
    total_months = 0 # used to track total months
    net_amount = 0 # used to track net amount
    amounts = []
    months = []
    for row in reader:
        # Each row contains Date and Profit/Losses as dictionary keys
        amounts.append(int(row['Profit/Losses']))
        months.append(row['Date'])
        
    # Close file since we don't need it any more
    f.close()
    
    total_months = len(months)
    net_amount = sum(amounts)
    
    # Calculate changes month over month
    changes = []
    prev_amount = 0
    for a in amounts:
        if prev_amount: # This will exclude the first month from consideration
            changes.append(a - prev_amount)
        prev_amount = a
        
    average_change = sum(changes) / len(changes)
    # "Greatest increase/decrease" here is really just another way of saying 
    # "find highest/lowest value in the changes list"
    # Python has min() and max() functions for that
    greatest_increase = max(changes)
    # We need month name as well. This is a bit tricky.
    # First, we get the position of the amount in the changes list
    pos = changes.index(greatest_increase)
    # Then we use the position to grab the month from the months list
    greatest_increase_month = months[pos + 1] # We have to add 1 because the months list is larger than changes list (line 49)
    
    # Repeat for decrease, except use min()
    greatest_decrease = min(changes)
    pos = changes.index(greatest_decrease)
    greatest_decrease_month = months[pos + 1]
    
    # Print to screen
    output = ''
    output += 'Financial analysis\n'
    output += '-------------------------\n'
    output += 'Total Months: ' + str(total_months) + '\n'
    output += 'Total: $' + str(net_amount) + '\n'
    output += 'Average  Change: ${:.2f}'.format(average_change) + '\n'
    output += 'Greatest Increase in Profits: ' + str(greatest_increase_month) + ' ($' + str(greatest_increase) + ')\n'
    output += 'Greatest Decrease in Profits: ' + str(greatest_decrease_month) + ' ($' + str(greatest_decrease) + ')\n'
    
    print output
    
    # Write to file
    text_file = open('financial_analysis.txt', 'w')
    text_file.write(output)
    text_file.close()
        
    
if __name__ == '__main__':
    analyze()