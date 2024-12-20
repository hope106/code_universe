from datetime import datetime
import pytz

def get_current_date():
    # 한국 시간대 설정
    korea_tz = pytz.timezone('Asia/Seoul')
    
    # 캐나다 주요 시간대 설정
    canada_timezones = {
        'Vancouver (PT)': 'America/Vancouver',
        'Edmonton (MT)': 'America/Edmonton',
        'Toronto (ET)': 'America/Toronto',
        'Halifax (AT)': 'America/Halifax',
        'St. John\'s (NT)': 'America/St_Johns'
    }
    
    # 현재 UTC 시간 가져오기
    current_utc = datetime.now(pytz.UTC)
    
    # 한국 시간 출력
    korea_time = current_utc.astimezone(korea_tz)
    formatted_date = korea_time.strftime("%Y-%m-%d")
    formatted_datetime = korea_time.strftime("%Y-%m-%d %H:%M:%S")
    
    print("=== 한국 시간 ===")
    print(f"한국 날짜: {formatted_date}")
    print(f"한국 현재 날짜와 시간: {formatted_datetime}")
    print(f"시간대: {korea_time.tzname()}")  # KST (Korea Standard Time) 표시
    
    print("\n=== 캐나다 주요 도시 시간 및 한국과의 시차 ===")
    # 캐나다 각 도시 시간 출력 및 시차 계산
    for city, timezone in canada_timezones.items():
        local_tz = pytz.timezone(timezone)
        local_time = current_utc.astimezone(local_tz)
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        
        # 시차 계산
        time_diff = korea_time.hour - local_time.hour
        # 날짜가 다른 경우 시차 조정
        if korea_time.day > local_time.day:
            time_diff += 24
        elif korea_time.day < local_time.day:
            time_diff -= 24
            
        # 시차 표시 문구 생성
        if time_diff > 0:
            time_diff_str = f"(한국이 {time_diff}시간 앞)"
        else:
            time_diff_str = f"(한국이 {abs(time_diff)}시간 뒤)"
            
        print(f"{city}: {formatted_time} {time_diff_str}")

    print("\n=== 시간대 변환 가이드 ===")
    print("예시: 한국 오후 2시(14:00)일 때")
    for city, timezone in canada_timezones.items():
        local_tz = pytz.timezone(timezone)
        # 한국 기준 14시를 기준으로 각 도시의 시간 계산
        korea_sample = korea_tz.localize(datetime.now().replace(hour=14, minute=0))
        local_sample = korea_sample.astimezone(local_tz)
        print(f"{city}: {local_sample.strftime('%H:%M')} ({local_sample.strftime('%p')})")

# 함수 실행
if __name__ == "__main__":
    get_current_date()