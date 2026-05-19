#!/usr/bin/env python3
import time, subprocess, json
from pathlib import Path

while True:
    # Run evolution cycle
    print(f"[IMPROVE] {time.time()}")
    
    # Check music engine, deploy backup, post updates
    subprocess.run(["python3", "/root/.openclaw/workspace/evez-music-studio/studio_fast.py"], 
                   capture_output=True)
    
    # Verify all systems
    checks = {
        "apk": Path("/root/.openclaw/workspace/evez-apk/app/src/main/AndroidManifest.xml").exists(),
        "music": Path("/tmp/evez_STUDIO_FAST.wav").exists(),
        "deploy": Path("/root/.openclaw/workspace/game-agent-infra/deploy").exists(),
    }
    
    print(f"[STATUS] {json.dumps(checks)}")
    time.sleep(60)
