def solution(players, callings):
    players_dict = {player : i for i, player in enumerate(players)}
    for call in callings:
        call_idx = players_dict[call]
        cut_idx = call_idx - 1
        cut_p = players[cut_idx]
        players[call_idx], players[cut_idx] = players[cut_idx], players[call_idx]
        players_dict[call] = cut_idx
        players_dict[cut_p] = call_idx
    return players