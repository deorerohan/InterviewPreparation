def minion_game(input):
    stuart_count = 0
    kevin_count = 0
    vowels = ["A", "E", "I", "O", "U"]
    current_count = 0
    complete_length = len(input)
    for i in input:
        if i in vowels:
            kevin_count += complete_length - current_count
        else:
            stuart_count += complete_length - current_count
        
        current_count += 1

    if stuart_count > kevin_count:
        print(f"Stuart {stuart_count}")
    elif stuart_count < kevin_count:
        print(f"Kevin {kevin_count}")
    else:
        print(f"Draw")


minion_game("BANANA")
