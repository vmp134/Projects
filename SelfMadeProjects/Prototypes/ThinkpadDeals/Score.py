import re
import json

def score_title(title:str):
    score:int = 0
    total_score:int = 100
    desired_model_tracker = 0.75
    title = title.lower()

    # Desired Traits. "-1" for no preference.
    desired_model = "t14"       
    desired_generation:int = 2
    desired_ram:int = 16
    desired_storage:int = -1
    desired_resolution:int = -1

    if (desired_model + " ") in title:  
        score += 50
        desired_model_tracker = 1
    
    return float(score/total_score)

def score_price(price:float):
    desired_price:float = 100
    return desired_price/price

def total_score(title:str, price:float):
    return (score_title(title) * score_price(price))