#!/usr/bin/env python3
"""
AUTO-OUTREACH SENDER
Sends brutal messages via xurl + logs to Telegram
Uses Standard Compute for message generation
"""

import subprocess
import json
import time
from pathlib import Path

BASE = Path("/root/.openclaw/workspace/game-agent-infra")
MESSAGES = (BASE / "evez_data/brutal_outreach_messages.txt").read_text().strip().split('\n\n')
SENT_LOG = BASE / "evez_data/sent_messages.jsonl"

def send_via_xurl(message):
    """Try xurl first"""
    try:
        result = subprocess.run(["xurl", "post", message], capture_output=True, text=True, timeout=10)
        return "success" in result.stdout.lower() or result.returncode == 0
    except:
        return False

def send_via_telegram(text):
    """Log to Telegram bot channel"""
    subprocess.run([
        "curl", "-s", "-X", "POST",
        "https://api.telegram.org/bot8677713465:AAHNusffuxD7dsXCw64PPxcwqmaGT9TZg6o/sendMessage",
        "-d", "chat_id=7453631330",
        "-d", f"text={text}"
    ], capture_output=True)

def run_outreach_batch(count=10):
    """Send count messages"""
    sent = 0
    for msg in MESSAGES:
        if sent >= count:
            break
        if send_via_xurl(msg):
            send_via_telegram(f"✅ Sent via xurl: {msg[:50]}...")
            SENT_LOG.write_text(json.dumps({"timestamp": time.time(), "message": msg[:50]}) + "\n")
            sent += 1
        else:
            send_via_telegram(f"📝 Logged: {msg[:50]}...")
            SENT_LOG.write_text(json.dumps({"timestamp": time.time(), "message": msg[:50], "status": "logged"}) + "\n")
            sent += 1
    return sent

if __name__ == "__main__":
    print(f"Sending 10 brutal outreach messages...")
    run_outreach_batch(10)
    print("Done.")