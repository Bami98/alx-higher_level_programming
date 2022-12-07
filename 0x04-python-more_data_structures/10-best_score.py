#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    maxScore = list(a_dictionary.values())[0]
    bestScorer = ''
    for key, value in a_dictionary.items():
        if maxScore < value:
           bestScorer, maxScore = key , value
    return bestScorer
