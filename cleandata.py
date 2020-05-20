import pandas as pd
import numpy as np


def load_personal_data():

    # Import Round Data
    round_data = pd.read_csv('./data/rounds.csv', usecols=["Name", "Date", "Course", "Course Rating"])
    round_data.columns = ['Rounds', 'Date', 'Course', 'Course Rating']
    round_data['Date'] = pd.to_datetime(round_data['Date'])

    # Import Hole Data
    hole_data = pd.read_csv('./data/holes.csv')
    hole_data['Greens'] = hole_data['Greens'].map({'checked': '1'})
    hole_data['Greens'] = hole_data['Greens'].astype('float64')
    hole_data['Sand'] = hole_data['Sand'].map({'Y': '1', 'N': '0'})
    hole_data['Sand'] = hole_data['Sand'].astype('float64')
    hole_data['Scrambling'] = hole_data['Scrambling'].map({'Y': '1', 'N': '0'})
    hole_data['Scrambling'] = hole_data['Scrambling'].astype('float64')
    hole_data['Fairways'] = hole_data['Fairways'].map({'Y': '1', 'N': '0'})
    hole_data['Fairways'] = hole_data['Fairways'].astype('float64')

    # Create Scores Summary Table
    scores_summary = hole_data.groupby(['Rounds'])[['Par', 'Score', 'Putts', 'Fairways', 'Greens']].sum()
    holes_played = hole_data['Rounds'].value_counts()
    relative_score = scores_summary.Score - scores_summary.Par
    relative_score.sort_index(inplace = True)
    relative_score.index = holes_played.index - 1
    holes_played.sort_index(inplace = True)
    holes_played.index = holes_played.index - 1
    scores_summary = round_data.merge(scores_summary, on='Rounds')
    scores_summary['Holes Played'] = holes_played
    scores_summary['Relative Score'] = relative_score

    #Remove records without stats tracked
    scores_summary.drop([3,5], inplace=True)
    scores_summary.reset_index(inplace=True)
    scores_summary.drop(['index','Rounds'], inplace=True, axis=1)

    #Combine 9 hole scores
    s1 = scores_summary.iloc[1,4:]
    s2 = scores_summary.iloc[11,4:]
    s2a = scores_summary.iloc[11,:4]
    s = s1 + s2
    scores_summary.iloc[11] = s2a.append(s)
    scores_summary.drop([1], inplace=True)

    # Add column for relative score given course difficulty
    scores_summary['Relative Score w/ Rating'] = scores_summary.Score.astype('float64') - scores_summary['Course Rating']

    #scores_summary.to_csv(r'./data/personal_scores.csv', index = False)

    return scores_summary




def load_pro_data():

    # Import PGA Tour Data
    data = pd.read_csv('./data/pgaTourData.csv')

    # Remove NA records.
    pro_data = data[data['gir'].notna()]

    # Remove unecessary features
    pro_data = pro_data[['gir','Average Putts','Average Score','Fairway Percentage']]

    # Convert average percentages per round into averages totals per round 
    pro_data['gir'] = (pro_data['gir']/100)*18
    pro_data['Fairway Percentage'] = (pro_data['Fairway Percentage']/100)*14
    pro_data['Holes Played'] = 18

    # Rename columns
    pro_data.columns = ['Greens','Putts','Score','Fairways','Holes Played']

    return pro_data
