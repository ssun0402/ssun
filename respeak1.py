# 젯슨 부르는 코드

import speech_recognition as sr
from gtts import gTTS
import playsound

# 이름 인식 코드
# 음성인식 끝내는 코드
def speak_jetson():
    
    # 음성인식 객체 생성
    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        
        # 마이크로부터 오디오 읽기
        print('"젯슨"을 불러주세요!')
        audio_data = r.record(source, duration = 3)
        
        try:
            # 음성을 문자열로 전환
            # 구글 API로 인식 (하루에 50회 제한)
            text = r.recognize_google(audio_data, language = 'ko')
            
            if(text == "잭슨") :
                print("네! 부르셨나요?")
                txt = "네! 부르셨나요?"
                tts_kr = gTTS(txt, lang = 'ko', slow = False)
                tts_kr.save("voice.wav")
                playsound.playsound("voice.wav")
                return respeak()
            
            elif (text == "종료") | (text == "종료") :
                return done_respeak()
            
            else:
                return speak_jetson()
            
        # 음성 인식 실패한 경우
        except sr.UnknownValueError:
            return speak_jetson()

# 음성 인식    
def respeak():
    # 음성인식 객체 생성
    r = sr.Recognizer()

    with sr.Microphone() as source :
    
        # 마이크로부터 오디오 읽기
        audio_data = r.record(source, duration = 5)
        
    try:
        # 음성을 문자열로 전환
        # 구글 API로 인식 (하루에 50회 제한)
        text = r.recognize_google(audio_data, language = 'ko')
        print("<음성을 문자로 변환한 값을 아래에 표시했습니다.>")
        print(text)
    
        # 인식된 음성에 대한 대답
        print(text + "라고 말했습니다.")
        txt = text + "라고 말했습니다."
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        tts_kr.save("voice.wav")
        playsound.playsound("voice.wav")
        return speak_jetson()
    
    # 음성 인식 실패한 경우
    except sr.UnknownValueError:
        print("다시 한 번 말씀해주시겠어요?")
        txt = "다시 한 번 말씀해주시겠어요?"
        tts_kr = gTTS(txt, lang = 'ko', slow = False)
        tts_kr.save("voice.wav")
        playsound.playsound("voice.wav")
        return respeak()

# 음성 인식 종료
def done_respeak():
    print("음성인식을 끄겠습니다.")
    txt = "음성인식을 끄겠습니다."
    tts_kr = gTTS(txt, lang = 'ko', slow = False)
    tts_kr.save("voice.wav")
    playsound.playsound("voice.wav")

try:  
    while True :
        speak_jetson()
        respeak()
        done_respeak()
        
# Crtl + c 누르면 음성 인식 멈춤
except KeyboardInterrupt: 
    pass