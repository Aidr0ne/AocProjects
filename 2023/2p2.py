import re
import math

def calculate_min_cubes(input_list):
    min_cubes_required = []
    total_power = 0

    for game_string in input_list:
        max_red = max_green = max_blue = 0  # Initialize min counts for each color
        
        # Split the game string into each turn
        turns = game_string.split(";")
        
        for turn in turns:
            # Find all occurrences of 'number color' in the turn
            matches = re.findall(r'(\d+)\s+(blue|red|green)', turn)
            
            # Track the max number of each color required in this game
            turn_red = turn_green = turn_blue = 0
            for count, color in matches:
                count = int(count)
                if color == 'red':
                    turn_red += count
                elif color == 'green':
                    turn_green += count
                elif color == 'blue':
                    turn_blue += count
            
            # Update the maximum cubes needed for each color across all turns
            max_red = max(max_red, turn_red)
            max_green = max(max_green, turn_green)
            max_blue = max(max_blue, turn_blue)

        # Store the minimum cubes required for this game
        min_cubes_required.append({"r": max_red, "g": max_green, "b": max_blue})
        
        # Calculate the power for this game
        game_power = max_red * max_green * max_blue
        total_power += game_power

    return min_cubes_required, total_power

Input = input("Enter Y2023 S2 P2e Target file: ")

with open(Input, 'r') as file:
    list = file.read()

min_cubes_required, total_power = calculate_min_cubes(list.split('\n'))

print("Minimum Cubes Required for Each Game:", min_cubes_required)
print("Total Power:", total_power)

# works
