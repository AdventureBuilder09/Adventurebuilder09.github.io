import js
import json
async def process_text(event):
           # 1. Grab input text from the textarea
            raw_text = js.document.getElementById("input-text").value
            
            # 2. Load the JSON configuration file (pre-fetched via config)
            try:
                with open("config.json", "r") as f:
                    config_data = json.load(f)
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