import re
import logging
from datetime import datetime
from logs import log_data  # імпорт логів з logs.py

# Налаштування логування
logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)

def analyze_heartbeat():
    target_key = "Key TSTFEED0300|7E3E|0400"
    timestamp_pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2})")
    timestamps = []

    for line in log_data:
        if target_key in line:
            match = timestamp_pattern.search(line)
            if match:
                time_str = match.group(1)
                dt = datetime.strptime(time_str, "%H:%M:%S")
                timestamps.append(dt)

    timestamps.sort()

    for i in range(1, len(timestamps)):
        diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
        curr_time = timestamps[i].strftime("%H:%M:%S")

        if 31 < diff < 33:
            logging.warning(f"Heartbeat is {diff:.0f} seconds at {curr_time}")
        elif diff >= 33:
            logging.error(f"Heartbeat is {diff:.0f} seconds at {curr_time}")

# Запуск
if __name__ == "__main__":
    analyze_heartbeat()
