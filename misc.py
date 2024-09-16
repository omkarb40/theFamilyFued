# The Family Fued ft. Steve Harvey
questions = [
    ["Name something you find in a woman's purse", "Wallet", "Phone", "Makeup", "Keys", 1],
    ["Name a type of fruit", "Apple", "Banana", "Orange", "Grapes", 2],
    ["Name a popular vacation spot", "Beach", "City", "Mountain", "Disneyland", 3],
    ["Name something you do when you wake up", "Brush teeth", "Take a shower", "Check phone", "Exercise", 4],
    ["Name a type of music", "Rock", "Pop", "Hip-Hop", "Classical", 1],
    ["Name a type of car", "Toyota", "Ford", "Honda", "Tesla", 2],
    ["Name a type of food", "Pizza", "Burger", "Sushi", "Tacos", 3],
    ["Name a type of sport", "Football", "Basketball", "Baseball", "Soccer", 4],
    ["Name a type of animal", "Dog", "Cat", "Bird", "Fish", 1],
    ["Name a type of movie", "Action", "Comedy", "Romance", "Horror", 2],
]  # Survey questions

scores = {"Team A":0, "Team B":0}

print("Welcome to Family Feud!")
print("Two teams will compete to guess the most popular responses to survey questions.")
print("The team with the highest score at the end of the game wins!")

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nSurvey says ... {question[0]}")
    print("Team A, Please respond")
    team_a_resp = input("Enter your response: ")
    print("Team B, Please respond: ")
    team_b_resp = input("Enter your response: ")

    if team_a_resp.lower() in [x.lower() for x in question[1:5]]:
        scores["Team A"] += 1
        print("Team A scores!")
    if team_b_resp.lower in [x.lower() for x in question[1:5]]:
        scores["Team B"] += 1
        print("Team B scores!")
    
    print(f"Current Scores are: Team A - {scores['Team A']} and Team B - {scores['Team B']}")

print(f"Final Scores are: Team A - {scores['Team A']} and Team B - {scores['Team B']}")
if scores["Team A"] > scores["Team B"]:
    print("Team A Wins!!")
elif scores["Team B"] > scores["Team A"]:
    print("Team B Wins!!")
else:
    print("Its a Tie!!")