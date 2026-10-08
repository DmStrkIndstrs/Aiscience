"""판서 화면(왼쪽 4:3) + 캐릭터(오른쪽 패널) + 음성 -> 1920x1080 강의 영상
사용: python scripts/compose.py <판서영상> <캐릭터: png 또는 mp4> <음성.wav> <출력.mp4>
캐릭터가 mp4(HeyGen 등 말하는 영상)면 480x1080 패널에 맞춰 잘라 넣고, 짧으면 반복합니다.
"""
import sys, subprocess
screen, char, voice, out = sys.argv[1:5]
is_video = char.lower().endswith((".mp4", ".mov", ".webm"))
char_in = ["-stream_loop", "-1", "-i", char] if is_video else ["-loop", "1", "-i", char]
fc = ("[0:v]fps=30,scale=1440:1080[l];"
      "color=c=0xEDEDED:s=1920x1080:r=30[bg];[bg][l]overlay=0:0:shortest=1[a];"
      "[1:v]fps=30,scale=480:1080:force_original_aspect_ratio=increase,crop=480:1080[c];"
      "[a][c]overlay=1440:0:shortest=1,format=yuv420p[v]")
subprocess.run(["ffmpeg", "-y", "-i", screen, *char_in, "-i", voice,
                "-filter_complex", fc, "-map", "[v]", "-map", "2:a", "-shortest",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
                "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
print("saved", out)
