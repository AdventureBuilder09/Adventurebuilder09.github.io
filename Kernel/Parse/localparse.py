import json
import re
import js
async def process_text(event):
           # 1. Grab input text from the textarea
            decklist = js.document.getElementById("input-text").value
            
            # 2. Load the JSON configuration file (pre-fetched via config)
            try:
                with open("all.json", "r") as f:
                    cardDB = json.load(f)
            except Exception as e:
                js.document.getElementById("output-text").value = f"Error loading JSON: {e}"
                return

            # 3. Process lines (example: uppercase words or apply replacement rules from JSON)
            lines = raw_text.splitlines()
            processed_lines = []
            
            replacement_map = config_data.get("replacements", {})

            for line in lines:
                # Apply simple custom processing rules defined in JSON
                current_line = line
                for target, replacement in replacement_map.items():
                    current_line = current_line.replace(target, replacement)
                processed_lines.append(current_line)

            # 4. Join back and display in the output textarea
            final_output = "\n".join(processed_lines)
            js.document.getElementById("output-text").value = final_output
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
starPTVal = 40 #higher than every printed PT, shut up BFM and Infinity Elemental don't exist
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
