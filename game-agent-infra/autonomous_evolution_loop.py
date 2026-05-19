#!/usr/bin/env python3
"""
AUTONOMOUS EVOLUTION LOOP - BRUTAL MODE
Every 30min: Post meme, commit, expand
"""
import subprocess
import time
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/root/.openclaw/workspace/game-agent-infra")

class AutonomousEvolution:
    def __init__(self):
        self.running = True
        self.cycle = 0
        
    def run_twitter_agent(self):
        """Post meme via brutal poster"""
        result = subprocess.run(
            ["python3", "tools/twitter_meme_agent_brutal.py"],
            capture_output=True, text=True, cwd=str(BASE_DIR)
        )
        return result.stdout
    
    def run_git_auto_commit(self):
        """Auto-commit growth logs"""
        now = datetime.now().isoformat()
        log = {"timestamp": now, "cycle": self.cycle}
        growth_file = BASE_DIR / "evez_data" / "autonomous_growth.jsonl"
        growth_file.parent.mkdir(exist_ok=True)
        with open(growth_file, "a") as f:
            f.write(json.dumps(log) + "\n")
        
        subprocess.run(["git", "add", str(growth_file)], capture_output=True, cwd=str(BASE_DIR))
        subprocess.run(["git", "commit", "-m", f"Auto: evolution #{self.cycle}"], 
                      capture_output=True, cwd=str(BASE_DIR))
        subprocess.run(["git", "push"], capture_output=True, cwd=str(BASE_DIR))
    
    def run(self):
        """Main loop - brutal mode"""
        print("[AE] BRUTAL AUTONOMOUS EVOLUTION STARTED")
        while self.running:
            self.cycle += 1
            print(f"\n[AE] Cycle {self.cycle}")
            
            self.run_twitter_agent()
            self.run_git_auto_commit()
            
            print(f"[AE] Cycle complete. Next in 30 min.")
            time.sleep(1800)

if __name__ == "__main__":
    ae = AutonomousEvolution()
    ae.run()