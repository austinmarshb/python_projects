def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    truelove = ['T', 'R', 'U', 'E', 'L', 'O', 'V', 'E']
    for items in truelove:
        values = name1.count(items.lower()) + name2.count(items.lower())
        print(f"{items.upper()} occurs {values} times.")
    
calculate_love_score("TRUE", "love")
