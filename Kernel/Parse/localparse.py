import json
import re
import js
"""
<br>
<!-- Simply display the live, self-updating image badge directly -->
<img src="" alt="Workflow Status">
<div class="badge-container">
    <h4>Live Deployment Monitor</h4>
    <!-- The script will populate the src attribute here -->
    <img id="live-workflow-badge" src="" alt="Checking workflow status...">
</div>

<script>
    function refreshBadge() {
        const badgeImg = document.getElementById('live-workflow-badge');
        
        // Use a timestamp to destroy the browser's attempt to cache the image
        const cacheBuster = new Date().getTime();
        
        // Construct the official URL with the anti-cache parameter attached
        const liveBadgeUrl = `https://github.com/AdventureBuilder09/Adventurebuilder09.github.io/actions/workflows/pages-build-deployment/badge.svg?v=${cacheBuster}`;
        
        // Update the image element
        badgeImg.src = liveBadgeUrl;
    }

    // 1. Run immediately when the user lands on the page
    refreshBadge();

    // 2. Refresh the image automatically every 10 seconds to catch live builds
    setInterval(refreshBadge, 10000); 
</script>
"""
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