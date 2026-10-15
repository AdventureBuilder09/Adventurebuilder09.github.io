import json
import re
import js
async def process_text(event):
      try:
            # 1. Grab input text from the textarea
            decklist = js.document.getElementById("input-text").value
            
            # 2. Load the JSON configuration file (pre-fetched via config)
            try:
                with open("points.json", "r") as f:
                    cardDB = json.load(f)
            except Exception as e:
                js.document.getElementById("output-text").value = f"Error loading JSON: {e}"
                return

            # 3. Process lines (example: uppercase words or apply replacement rules from JSON)
            lines = raw_text.splitlines()
            pts = lines.size()
            
            replacement_map = config_data.get("replacements", {})

            for line in lines:
                # Apply simple custom processing rules defined in JSON
                for target, score in replacement_map.items():
                    if current_line.contains(target):
                      pts = pts + score
                    

            # 4. Join back and display in the output textarea
            final_output = f"Points value: {pts}"
            js.document.getElementById("output-text").value = final_output
      except Exception as e:
        js.document.getElementById("output-text").value = f"Uncaught PY Error: {e}"