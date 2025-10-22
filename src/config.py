import os

# Базовый URL можно переопределить через переменную окружения
BASE_URL = os.getenv("SB_BASE_URL", "https://stellarburgers.education-services.ru").rstrip("/")
