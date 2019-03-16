
import pandas as pd
import numpy as np
import os

file = 'resources/election_data.csv'
original = pd.read_csv(file)
original.head(10)

#count votes by original voterIDs
votecount = original['Voter ID'].count()

#count votes by candidates, results to dataframe, add column named Votes
candidatevotes = original['Candidate'].value_counts()
candidates = pd.DataFrame(candidatevotes)
candidates.columns=['Votes']


#candidates to list, index
candidates_list = candidates.index.tolist()
votesbycandidate = candidates.iloc[:, 0].tolist()


#calculate percent, add column with results to candidates
percent = ((candidates/votecount)*100).round(2)
candidates['Percent'] = percent

#make list using just the percent values for each candidate
percent_list = candidates.iloc[:, 1].tolist()

#cast all three lists to dataframe
election = pd.DataFrame({
    'Candidate': candidates_list,
    'Votes': votesbycandidate,
    'Percent': percent_list
})

#use dataframe from above to index by number of votes, grab the candidate with the highest votes
#assign that candidates name to var winner
winner_df = election.set_index('Votes')
winner_votes = max(votesbycandidate)
winner = winner_df.loc[winner_votes].Candidate

#print results in strings to check progress
print('Election Results')
print('--------------------------')
print('Total votes: ' + str(votecount))
print('--------------------------')
print(str(election))
print('--------------------------')
print('Winner: ' + str(winner))


#write to txt file
txt = open('Hanson_polls.txt', 'w')

txt.write('Election Results' + '\n')
txt.write('--------------------------' + '\n')
txt.write('Total Votes: ' + str(votecount) + '\n')
txt.write('--------------------------' + '\n')
txt.write(str(election) + '\n')
txt.write('--------------------------' + '\n')
txt.write('Winner: ' + str(winner))

