from datetime import datetime
import pytz

def get_current_date():
    # 한국 시간대 설정
    korea_tz = pytz.timezone('Asia/Seoul')
    
    # 현재 UTC 시간을 한국 시간으로 변환
    current_datetime = datetime.now(pytz.UTC).astimezone(korea_tz)
    
    # 날짜 형식 지정하여 출력
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"한국 날짜: {formatted_date}")
    print(f"한국 현재 날짜와 시간: {formatted_datetime}")
    print(f"시간대: {current_datetime.tzname()}")  # KST (Korea Standard Time) 표시

# 함수 실행
if __name__ == "__main__":
    get_current_date()