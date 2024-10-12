import random

# Global variable to track opponent's history
opponent_history = []

def player(prev_play):
    # If it's the first game, start with Rock
    if prev_play == '':
        move = 'R'
    else:
        # Store the opponent's last move
        opponent_history.append(prev_play)
        
        # Count the occurrences of each move in opponent history
        count_r = opponent_history.count('R')
        count_p = opponent_history.count('P')
        count_s = opponent_history.count('S')

        # Find the opponent's most played move
        if count_r >= count_p and count_r >= count_s:
            # If opponent plays Rock most, play Paper
            move = 'P'
        elif count_p >= count_r and count_p >= count_s:
            # If opponent plays Paper most, play Scissors
            move = 'S'
        else:
            # If opponent plays Scissors most, play Rock
            move = 'R'
    
    return move
