import os

def solution(list):
    sum = 0
    target = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(len(list)):
        first = 0
        last = 0
        conbined = 0
        word = list[i]
        for x in range(len(word)):
            if word[x] in target:
                first = word[x]
                break
        
        for x in range(len(word)):
            if word[-(x+1)] in target:
                last = word[-(x+1)]
                break
        conbined = int(str(first) + str(last))
        sum += conbined
    
    return sum


Input = input("Enter Y2023 S1 P1 Target file: ")

with open(Input, 'r') as file:
    list = file.read()

print(solution(list.split()))