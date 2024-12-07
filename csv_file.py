import csv

total_goals = 0

matches = [
    {
        "Team A": "Felicis",
        "Team B": "Jesso",
        "Score A": 100,
        "Score B": 100,
        "Date": "2024-04-21"
    },
    {
        "Team A": "Obama",
        "Team B": "Trump",
        "Score A": 100,
        "Score B": 100,
        "Date": "2024-04-26"
    }
]


with open('euro_cup_matches.csv') as file:
    # read the headings

    content = csv.DictReader(file)
 
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])

print(f'Total goals in tournament so far: {total_goals}')    

    #headings = file.readline().strip()
    #columns = headings.split(',')
    #print(columns)



with open('new_matches.csv', 'w') as file:
    writer = csv.DictWriter(file, ['Team A', 'Team B', 'Score A', 'Score B', 'Date'])
    writer.writeheader()
    #writer.writerow({'Team A': 'Portugal',
    #                'Team B': 'Felicis',
    #                'Score A': 1,
   #                 'Score B': 1,
    #                'Date': '2024-04-15'}
    #)
    writer.writerows(matches)