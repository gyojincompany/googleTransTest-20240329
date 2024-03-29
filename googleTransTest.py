import googletrans

while True:
    korStr = input("번역할 문장을 입력하세요:")
    if korStr == "끝":
        break
    trans = googletrans.Translator()  # 구글 번역 객체 생성
    result1 = trans.translate(korStr, dest="en")  # 영어로 번역
    # print(googletrans.LANGUAGES) -> 번역 언어의 dest 약자 찾기
    result2 = trans.translate(korStr, dest="ja")  # 일본어로 번역
    result3 = trans.translate(korStr, dest="zh-cn")  # 중국어로 번역
    print(f"입력하신 [{korStr}]은 영어로 [{result1.text}] 입니다")
    print(f"입력하신 [{korStr}]은 일본어로 [{result2.text}] 입니다")
    print(f"입력하신 [{korStr}]은 중국어로 [{result3.text}] 입니다")
