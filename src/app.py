# src/app.py
def say_hello(name="World"):
    return f"Hello, {name}! This is the initial version."

if __name__ == "__main__":
    print(say_hello("Git User"))
    # src/app.py 수정 내용 (예시)
import datetime # 이 줄을 파일 맨 위에 추가

def say_hello(name="World"):
    current_date = datetime.date.today().strftime("%Y-%m-%d") # 날짜 가져오기
    # 출력 메시지에 날짜 정보 추가
    return f"Hello, {name}! Today is {current_date}. This is the initial version." 
    
if __name__ == "__main__":
    print(say_hello("Git User"))