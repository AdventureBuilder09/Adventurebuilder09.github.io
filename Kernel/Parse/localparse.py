import json
import re
import js
import displayCard as draw

#base = input("Please enter the input file (all.json is default)")
base = "all.json"
try:
    with open(base, 'r', encoding='utf-8') as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    print(f"Parse Error: {e.msg}")
    print(f"Line: {e.lineno}, Column: {e.colno}, Position: {e.pos}")
    quit
except FileNotFoundError:
    print("Error: The specified file could not be found.")
    quit


data.sort(key=lambda card : card.get("edhrec_rank"))
head = data
print("Data successfully loaded")
starPTVal = 40
nonePTVal = -2
def cast_int_pt(val):
    if val is None:
        return nonePTVal
    elif val == "*":
        # Return a fixed value depending on where you want '*' to land
        return starPTVal
    try:
        return int(val)
    except (ValueError, TypeError):
        print("Attempt to cast unknown ",val)
        return -3
