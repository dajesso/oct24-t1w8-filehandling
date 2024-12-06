import csv

total_goals = 0

with open('euro_cup_matches.csv') as file:
    # read the headings

    content = csv.DictReader(file)
 
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])

print(f'Total goals in tournament so far: {total_goals}')    

    #headings = file.readline().strip()
    #columns = headings.split(',')
    #print(columns)