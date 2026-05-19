#!/usr/bin/env python3
"""
AUTONOMOUS EVOLUTION LOOP
Runs all EVEZ agents continuously - no human required
"""

import subprocess
import time
import json
from pathlib import Path
from datetime import datetime

class AutonomousEvolution:
    def __init__(self):
        self.running = True
        self.cycle = 0
        
    def run_twitter_agent(self):
        """Post meme every 30 minutes"""
        result = subprocess.run(
            ["python3", "tools/twitter_meme_agent_brutal.py"],
            capture_output=True, text=True
        )
        return result.stdout
    
    def run_git_auto_commit(self):
        """Auto-commit growth logs"""
        now = datetime.now().isoformat()
        log = {"timestamp": now, "cycle": self.cycle, "status": "evolving"}
        Path("evez_data/autonomous_growth.jsonl").write_text(json.dumps(log) + "\n")
        
        subprocess.run(["git", "add", "evez_data/autonomous_growth.jsonl"], capture_output=True)
        subprocess.run(["git", "commit", "-m", f"Auto: autonomous evolution cycle #{self.cycle}"], capture_output=True)
        subprocess.run(["git", "push"], capture_output=True)
    
    def run_market_expansion(self):
        """Calculate next expansion targets"""
        return "Ready for 100 more outreaches + 5 client conversions"
    
    def run(self):
        """Main loop"""
        print("[AE] AUTONOMOUS EVOLUTION LOOP STARTED")
        while self.running:
            self.cycle += 1
            print(f"\n[AE] Cycle {self.cycle}")
            
            # Twitter agent
            print("[AE] Running Twitter agent...")
            self.run_twitter_agent()
            
            # Git auto-commit
            print("[AE] Auto-committing growth...")
            self.run_git_auto_commit()
            
            # Expansion target
            print("[AE] " + self.run_market_expansion())
            
            print(f"[AE] Cycle complete. Next in 30 minutes.")
            
            # Wait 30 min
            time.sleep(1800)

if __name__ == "__main__":
    ae = AutonomousEvolution()
    ae.run()