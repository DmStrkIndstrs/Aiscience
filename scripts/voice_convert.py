"""남성 강의 음성 -> 여성 캐릭터 음성 (Praat 'Change gender', 로컬 처리)
사용: python scripts/voice_convert.py input/lecture.mov output/voice.wav [preset]
preset: A(차분 190Hz) / B(기본 205Hz, 기본값) / C(밝음 225Hz)
필요: pip install praat-parselmouth, ffmpeg (PATH)
"""
import sys, subprocess, tempfile, os
import parselmouth
from parselmouth.praat import call

PRESETS = {"A": (1.15, 190, 1.1), "B": (1.2, 205, 1.2), "C": (1.25, 225, 1.3)}
src, dst = sys.argv[1], sys.argv[2]
formant, pitch, rng = PRESETS[sys.argv[3] if len(sys.argv) > 3 else "B"]

tmp = os.path.join(tempfile.mkdtemp(), "mono.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "44100", tmp], check=True)
out = call(parselmouth.Sound(tmp), "Change gender", 75, 600, formant, pitch, rng, 1.0)
raw = dst + ".raw.wav"
out.save(raw, "WAV")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw,
                "-af", "highpass=f=100,equalizer=f=3500:t=q:w=1:g=2,loudnorm=I=-16", "-ar", "48000", dst], check=True)
os.remove(raw)
print("saved", dst)
