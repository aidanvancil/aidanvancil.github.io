# -*- coding: utf-8 -*-
"""
@author: aidan
"""
def rps_evaluation(player_one: str, player_two:str) -> int:
    fighting_set = ["Rock", "Paper", "Scissors"]
    p1 = fighting_set.index(player_one)
    p2 = fighting_set.index(player_two)
    game = [p1,p2]
    win_conditions_for_p1 = [[0,2], [1,0], [2,1]]
    tie_condition = [[0,0],[1,1],[2,2]]
    for p in win_conditions_for_p1:
        if game == p:
            print(1)
            return 1
    for p in tie_condition:
        if game == p:
            print(0)
            return 0
    else:
        print(-1)
        return -1
rps_evaluation("Rock", "Scissors")
rps_evaluation("Scissors", "Rock")
rps_evaluation("Rock", "Rock")
rps_evaluation("Paper", "Rock")
