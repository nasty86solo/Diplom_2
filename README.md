# Stellar Burgers — API tests (Task 2)

Автотесты для API Stellar Burgers (покрывают создание пользователя, логин, создание заказа).
Базовый URL можно задать через переменную окружения `SB_BASE_URL` (по умолчанию используется
`https://stellarburgers.education-services.ru`).

## Структура
```
src/
  config.py        # базовые настройки (BASE_URL)
  http.py          # лёгкий HTTP‑клиент поверх requests.Session
  users.py         # методы Users API
  orders.py        # методы Orders API
  factories.py     # генерация тестовых данных (Faker)
  data.py          # текстовые сообщения/помощники
tests/
  conftest.py
  test_users.py    # регистрация и дубликаты/обязательные поля
  test_auth.py     # логин: успех и неверные данные
  test_orders.py   # создание заказа: автор/без автор, валид/невалид ингредиенты
pytest.ini
requirements.txt
.gitignore
```

## Запуск
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# export SB_BASE_URL="https://stellarburgers.nomoreparties.site"

# прогон с allure-результатами
pytest -q --alluredir=allure-results

# сформировать и открыть отчёт Allure (нужен allure-CLI)
# allure serve allure-results
```
