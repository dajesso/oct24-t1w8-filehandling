# JSON - Javascript Object Notiation

import json

matches = [
    {
        'Team A': 'Felicis',
        'Team B': 'Jesso',
        'Score A': 100,
        'Score B': 100,
        'Date': '2024-04-21'
    },
    {
        'Team A': 'Obama',
        'Team B': 'Trump',
        'Score A': 100,
        'Score B': 100,
        'Date': '2024-04-26'
    }

]

with open('matches.json', 'w') as file:
    json.dump(matches, file, indent = 4)