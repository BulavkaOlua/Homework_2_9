import logging

LOG_FILE = "login_system.log"
logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log_event(username: str, status: str):
    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

# 🔸 Ручний запуск для перевірки
if __name__ == "__main__":
    log_event("admin", "success")
    log_event("admin", "expired")
    log_event("admin", "failed")
    log_event("admin", "unknown")
    print(f"Логи записано у файл: {LOG_FILE}")

