import re

def parser(input_list, Range=100):
    # Initialize parsed with dictionaries for each game
    parsed = [{
        "r": 0,
        "g": 0,
        "b": 0
    } for _ in range(Range)]

    # Lists to hold IDs of games that exceed the thresholds or not
    exceeds_threshold = []
    within_threshold = []

    # Loop over each game input string in the provided range
    for i in range(min(Range, len(input_list))):
        game_string = input_list[i]
        game_exceeds_threshold = False  # Track if the game exceeds threshold
        
        # Regex pattern to find all occurrences of 'number color'
        pattern = r'(\d+)\s+(blue|red|green)'
        
        # Find all matches of 'number color'
        matches = re.findall(pattern, game_string)
        
        # Process each match
        for count, color in matches:
            count = int(count)
            if color == 'blue':
                parsed[i]["b"] += count
                if count > 14:  # Individual check for blue
                    game_exceeds_threshold = True
            elif color == 'red':
                parsed[i]["r"] += count
                if count > 12:  # Individual check for red
                    game_exceeds_threshold = True
            elif color == 'green':
                parsed[i]["g"] += count
                if count > 13:  # Individual check for green
                    game_exceeds_threshold = True

        # Add game ID to the appropriate list
        if game_exceeds_threshold:
            exceeds_threshold.append(i + 1)  # Game IDs start from 1
        else:
            within_threshold.append(i + 1)

    return parsed, exceeds_threshold, within_threshold

Input = input("Enter Y2023 S2 P1 Target file: ")

with open(Input, 'r') as file:
    list = file.read()

parsed, exceeds_threshold, within_threshold = parser(list.split('\n'))

print("Parsed Data:", parsed)
print("Games Exceeding Threshold:", exceeds_threshold)
print("Games Within Threshold:", within_threshold)

total = 0
for i in range(len(within_threshold)):
    total += within_threshold[i]

print(total)

# Works now lmoa