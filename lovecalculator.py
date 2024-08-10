def calculate_love_score(name1, name2):
    total_love_score_name1 = 0
    total_love_score_name2 = 0
    name1 = name1.lower()
    name2 = name2.lower()
    true = ['T', 'R', 'U', 'E']
    love = ['L', 'O', 'V', 'E']
    for items in true:
        value1 = name1.count(items.lower())
        value2 = name2.count(items.lower())
        true_value = value1 + value2
        print(f"{items.upper()} occurs {true_value} times.")
        total_love_score_name1 += true_value
    for items in love:
        value3 = name1.count(items.lower())
        value4 = name2.count(items.lower())
        love_value = value3 + value4
        print(f"{items.upper()} occurs {love_value} times.")
        total_love_score_name2 += love_value
    print(f"Total love score: {str(total_love_score_name1) + str(total_love_score_name2)}")
calculate_love_score("Angela Yu", "Jack Bauer")
