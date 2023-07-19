stats=[
    
    {"Name": "virat kohli",
    "Number of centuries": 75,
    "Half centuries": 161,
    "Wicket taken": 8,
    "Hat-tricks wickets": 1,
    "Top batting score": [102,110,128,104,127]},
        
    {"Name": "Ben stroke",
    "Number of centuries": 69,
    "Half centuries": 144,
    "Wicket taken":7,
    "Hat-tricks wickets": 2,
    "Top batting score": [105,111,144,100,108]},
        
    {"Name": "steve smith",
    "Number of centuries": 68,
    "Half centuries": 147,
    "Wicket taken": 6,
    "Hat-tricks wickets": 1,
    "Top batting score": [101,104,148,109,100]},
        
    {"Name": "sahir naqash",
    "Number of centuries": 8,
    "Half centuries": 3,
    "Wicket taken": 8,
    "Hat-tricks wickets": 2,
    "Top batting score": [103,101,134,110,118]},
        
    {"Name": "mohit panchal",
    "Number of centuries": 6,
    "Half centuries": 2,
    "Wicket taken": 5,
    "Hat-tricks wickets": 1,
    "Top batting score": [105,131,164,130,128]}
    ]

'''for i in stats:
    centuries=int(i["Number of centuries"])
    if centuries>10:
        name=i["Name"]
        print(name)'''


'''for i in stats:
    Hat_tricks=(i["Hat-tricks wickets"])
    if Hat_tricks>5:
        name=i["Name"]
        print(name)'''


def batting_score():
    for i in stats:
        print(stats[i]["Top batting score"])
        





