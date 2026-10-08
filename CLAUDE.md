# AI 캐릭터 지구과학 강의 제작 (휘T)

## 목표
휘T(남성)가 녹화한 지구과학 판서 강의(아이패드 화면 녹화 + 음성)를
1번 캐릭터(20대 여성, 실사풍, 안경, 긴 흑발, 흰 셔츠 + 짙은 회색 스커트, 은색 시계, 검은 노트)가
강의하는 영상으로 바꾼다.

## 폴더
- input/      : 원본 강의 영상 (예: RPReplay_*.mov) 을 여기에 넣는다
- assets/     : character_panel.png (1번 캐릭터 480x1080), character_sheet_3outfits.png (의상 3종, 1번 확정)
- scripts/    : voice_convert.py (로컬 음성 변환), compose.py (화면 합성)
- output/     : 결과물. 완성본은 D:\클로드 에도 복사한다.

## 지금까지 한 것
- 원본 음성 평균 높이 약 100Hz. 로컬 변환 프리셋 A/B/C 중 B(205Hz) 로 초안 제작 → 떨림이 남아 품질 한계.
- 레이아웃: 1920x1080, 왼쪽 판서 1440x1080, 오른쪽 캐릭터 패널 480x1080.

## 다음 할 일 (크롬 확장 연결 상태에서)
1. Supertone (또는 ElevenLabs Voice Changer) 에서 원본 음성을 여성 목소리로 변환 → output/voice_ai.wav
   - 사이트 로그인은 사용자가 직접 해 둔다. 크레딧 쓰는 버튼은 누르기 전에 반드시 확인받기.
2. HeyGen 에서 assets/character_panel.png 로 사진 아바타 생성 → voice_ai.wav 로 말하는 영상 생성 → output/avatar.mp4
   - 무료 플랜은 1분 제한. 2분 강의면 나눠서 생성하거나 유료 플랜 필요.
3. python scripts/compose.py input/<원본>.mov output/avatar.mp4 output/voice_ai.wav output/final.mp4
4. 유튜브 업로드 시 'AI 생성/합성 콘텐츠' 표시를 켠다.

## 빠른 실행 (AI 서비스 없이 로컬만)
pip install praat-parselmouth
python scripts/voice_convert.py input/lecture.mov output/voice_B.wav B
python scripts/compose.py input/lecture.mov assets/character_panel.png output/voice_B.wav output/draft.mp4
