from datetime import datetime

def get_current_date():
    # 현재 날짜와 시간 가져오기
    current_datetime = datetime.now()
    
    # 날짜 형식 지정하여 출력
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"오늘 날짜: {formatted_date}")
    print(f"현재 날짜와 시간: {formatted_datetime}")

# 함수 실행
if __name__ == "__main__":
    get_current_date()