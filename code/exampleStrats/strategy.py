def strategy(history, avgPreviousScore, avgPreviousCoop, memory):
    """
    - If I got a good outcome (win), do the same move again
    - If I got a bad outcome (lose), change my move
    """
    # Cooperate first
    if history.shape[1] == 0:
        return 1, None
    
    my_last_move = history[0][-1]
    opponent_last_move = history[1][-1]
    good_outcome = False
    
    if my_last_move == 1 and opponent_last_move == 1:
        good_outcome = True
    elif my_last_move == 0 and opponent_last_move == 1:
        good_outcome = True
    
    if good_outcome:
        # If last outcome was good, repeat the same move
        return my_last_move, None
    else:
        # If last outcome was bad, switch moves
        return 1 - my_last_move, None