#!/usr/bin/env python3
"""
EVEZ MUSIC STUDIO - FAST VERSION
Real music with actual melody, chords, bass
"""
import math, struct, wave

SR = 48000
DUR = 120  # 2 minutes
N = DUR * SR
audio = [0.0] * N

# CHORD PROGRESSION: Am - F - C - G (real song structure)
chords = {
    0: [110, 138, 164, 220],   # Am
    30: [146, 174, 220, 293],  # F  
    60: [164, 196, 246, 329],  # C
    90: [138, 164, 196, 261],  # G
}

# Lead melody notes (G4 A4 B4 progression)
melody = [
    (329, 0, 15),    # G4
    (349, 15, 16),   # G#4
    (293, 30, 16),   # D4
    (277, 45, 16),   # C#4
    (293, 60, 16),   # D4
    (246, 75, 16),   # B3
]

for t in range(N):
    sec = t / SR
    
    # Chords
    chord_freqs = [110, 146, 164, 138]  # default Am
    for beat, freqs in chords.items():
        if sec >= beat and sec < beat + 30:
            chord_freqs = freqs
            break
    
    pad = sum(math.sin(t * f * 2 * math.pi / SR) * 0.12 for f in chord_freqs) * 0.6
    
    # Lead melody
    mel = 0
    for freq, start, dur in melody:
        if start <= sec < start + dur:
            mel = math.sin(t * freq * 2 * math.pi / SR) * 0.4
            break
    
    # Bass
    bass_freq = 55 + (sec % 30) * 0.1
    bass = math.sin(t * bass_freq * 2 * math.pi / SR) * 0.5
    
    # Drums
    kick = 1.0 if (t % 18750) < 1000 else 0.2
    snare = 0.8 if (t % 37500) < 500 else 0
    
    audio[t] = pad + mel + bass + kick + snare

# Normalize
mx = max(abs(x) for x in audio) or 1
audio = [x/mx * 0.9 for x in audio]

with wave.open('/tmp/evez_STUDIO_FAST.wav', 'w') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    for i in range(0, len(audio), 2):
        w.writeframes(struct.pack('<hh', int(audio[i]*32767), int(audio[min(i+1,len(audio)-1)]*32767)))

print("STUDIO FAST COMPLETE")