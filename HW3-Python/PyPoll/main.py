from __future__ import division
# https://stackoverflow.com/questions/10768724/why-does-python-return-0-for-simple-division-calculation
import csv


def analyze():
    """
        Task:
        
        The total number of votes cast
        A complete list of candidates who received votes
        The percentage of votes each candidate won
        The total number of votes each candidate won
        The winner of the election based on popular vote.
        
        Sample output to screen AND text file: 
        
        Election Results
        -------------------------
        Total Votes: 3521001
        -------------------------
        Khan: 63.000% (2218231)
        Correy: 20.000% (704200)
        Li: 14.000% (492940)
        O'Tooley: 3.000% (105630)
        -------------------------
        Winner: Khan
        -------------------------
    """
    f = open('election_data.csv')
    reader = csv.DictReader(f)
    total_votes = 0 # used to track total votes
    candidates = {} # used to track candidate information
    for row in reader:
        # Each row contains Voter ID, County and Candidate as dictionary keys
        # We ignore County because the exercise doesn't ask for anything with County
        c = row['Candidate']
        v = row['Voter ID']
        
        if c in candidates:
            candidates[c]['votes'] += 1
        else:
            candidates[c] = {'votes' : 1}
        
        # Keep track of total vote
        total_votes += 1
        
    # Close file since we don't need it any more
    f.close()
        
    # Let's now figure out percentages and add the value to the same dictionary
    for c, v in candidates.items():
        v['percentage'] = v['votes'] / total_votes * 100
        
    # Sort candidates by votes
    # For reference: https://stackoverflow.com/questions/5601909/sorting-a-dict-by-values-inside-an-inner-dict-in-python
    # By default, sort is ascending, we want descending to get highest value first
    # sorted_candidates will be a list of tuples
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1]['votes'], reverse=True)
        
    # Print to screen
    output = ''
    output += 'Election results\n'
    output += '-------------------------\n'
    output += 'Total Votes: ' + str(total_votes) + '\n'
    output += '-------------------------\n'
    
    for c in sorted_candidates:
        # sorted_candidates is a list that looks like this:
        """
            [
                ('Khan', {'votes': 2218231, 'percentage': 63.00001050837531}), 
                ("O'Tooley", {'votes': 105630, 'percentage': 2.999999147969569}), 
                ('Correy', {'votes': 704200, 'percentage': 19.999994319797125}), 
                ('Li', {'votes': 492940, 'percentage': 13.999996023857989})
            ]
        """
        output += c[0] + ': ' + '{:.3f}'.format(c[1]['percentage']) + '% (' + str(c[1]['votes']) + ')\n'
    
    output += '-------------------------\n'
    output += 'Winner: ' + sorted_candidates[0][0] + '\n' # Winner is first tuple in list. And we want first value in tuple i.e. name
    output += "-------------------------\n"
    
    print output
    
    # Write to file
    text_file = open('election_results.txt', 'w')
    text_file.write(output)
    text_file.close()
        
    
if __name__ == '__main__':
    analyze()