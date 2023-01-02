
from JSONStructure import unlist_dict
import json




f = open('game_info.json')

d = json.load(f)

s = unlist_dict(d)

with open('one_game_substruc_TEE_v1.txt',"w",encoding="utf-8") as f:
    f.write(s)