# 젯슨 부르는 코드

import speech_recognition as sr
from gtts import gTTS
import playsound
import time

while True:
    # 음성인식 객체 생성
    r = sr.Recognizer()

    with sr.Microphone() as source :
        
        print("음성을 입력하세요!")
        
        # 마이크로부터 오디오 읽기
        audio_data = r.record(source, duration = 5)
    
    try:
        # 음성을 문자열로 전환
        # 구글 API로 인식 (하루에 50회 제한)
        text = r.recognize_google(audio_data, language = 'ko')
    
        if (text == "마이클 젯슨") : 
            # 스피커로부터 텍스트 읽기
            print("네 음성을 말해주세요!")
            txt = "네 음성을 말해주세요!"
            tts_kr = gTTS(txt, lang = 'ko', slow = False)
            tts_kr.save("voice.wav")
            playsound.playsound("voice.wav")
            
        elif (text == "음성 인식 꺼줘") :
            print("음성인식을 끄겠습니다.")
            txt = "음성인식을 끄겠습니다."
            tts_kr = gTTS(txt, lang = 'ko', slow = False)
            tts_kr.save("voice.wav")
            playsound.playsound("voice.wav")
            pass
        
        else : 
            print("<음성을 문자로 변환한 값을 아래에 표시했습니다.>")
            print(text)
    
    # 음성 인식 실패한 경우
    except sr.UnknownValueError:
        print("다시 한 번 말씀해주시겠어요?")
        txt = "다시 한 번 말씀해주시겠어요?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        tts_kr.save("voice.wav")
        playsound.playsound("voice.wav")