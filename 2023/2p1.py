import re

def parser(input_list, Range=100):
    # Initialize parsed with dictionaries for each game
    parsed = [{
        "r": 0,
        "g": 0,
        "b": 0
    } for _ in range(Range)]

    # Loop over each game input string in the provided range
    for i in range(min(Range, len(input_list))):
        game_string = input_list[i]

        # Regex pattern to find all occurrences of 'number color'
        pattern = r'(\d+)\s+(blue|red|green)'
        
        # Find all matches of 'number color'
        matches = re.findall(pattern, game_string)
        
        # Process each match and update the color counts
        for count, color in matches:
            if color == 'blue':
                parsed[i]["b"] += int(count)
            elif color == 'red':
                parsed[i]["r"] += int(count)
            elif color == 'green':
                parsed[i]["g"] += int(count)
                
    return parsed

def determine(list):
    trut = 0
    for i in range(len(list)):
        id = i+1
        if list[i]['r'] <= 12 and list[i]['g'] <= 13 and list[i]['b'] <= 14:
            trut += id
            print(f"hit on {id} total is now {trut}")

    return trut


Input = input("Enter Y2023 S2 P1 Target file: ")

with open(Input, 'r') as file:
    list = file.read()

print(determine(parser(list.split('\n'))))

# THE CODE DOES NOT ACOMPLISH tHE DESIRED RESULT DO NOT USE