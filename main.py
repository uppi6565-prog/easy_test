import time
import requests

url = "https://uxxi.online/10MB.bin"
headers = {"User-Agent": "Mozilla/5.0"}

times = []
sizes = []

for _ in range(10):
    start = time.perf_counter()
    try:
        with requests.get(url, headers=headers, stream=True) as p:
            p.raise_for_status()
            downloaded = sum(len(c) for c in p.iter_content(256 * 1024) if c)
            
        duration = time.perf_counter() - start
        times.append(duration)
        sizes.append(downloaded)
        
        # Считаем скорость для конкретного запроса
        total_mbs = downloaded / 1048576
        speed = total_mbs / duration
        print(f"Скорость запроса: {speed} МБ/с")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if times:
    total_mbs = sum(sizes) / 1048576
    avg_time = sum(times) / len(times)
    total_speed = total_mbs / sum(times)
    
    print(f"Общий объем: {total_mbs} МБ")
    print(f"Среднее время: {avg_time} с")
    print(f"Итоговая средняя скорость: {total_speed} МБ/с")
