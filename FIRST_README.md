Комментарии по первой версии второй части диплома автоматизации

In diplom_2/src/users.py:

> +AUTH_REGISTER = "/api/auth/register"
+AUTH_LOGIN = "/api/auth/login"
+AUTH_USER = "/api/auth/user"
Можно лучше здесь и далее: адреса лучше вынести во внешний модуль(например, urls). Они могут измениться, что затруднит поддержку тестов

In diplom_2/tests/conftest.py:

> +@pytest.fixture()
+def new_user_payload():
+    return user_payload()
Нужно исправить: фикстуры не занимаются выполнением примитивной логики, они выполняют сложную логику предусловий\постусловий и вычислений. Эти объекты можно сразу создавать в тестах или фикстурах

In diplom_2/tests/test_auth.py:

> +        token = body.get("accessToken")
+        users.client.set_token(token)
+        users.delete_current()
+        users.client.set_token(None)
Необходимо исправить здесь и далее: удаление курьера в тестах этого сценария - часть пост-условия, а не шаг теста. Лучше его вынести в фикстуры

In diplom_2/tests/test_users.py:

> +        token = body.get("accessToken")
+        users.client.set_token(token)
+        users.delete_current()
+        users.client.set_token(None)
Необходимо исправить здесь и далее: удаление курьера в тестах этого сценария - часть пост-условия, а не шаг теста. Лучше его вынести в фикстуры

In diplom_2/tests/test_auth.py:

> @@ -0,0 +1,35 @@
+import allure
+import pytest
+from src.data import Status
+from src.factories import user_payload
+
+@allure.suite("Auth")
+class TestAuth:
+
+    @allure.title("Логин под существующим пользователем")
+    def test_login_ok(self, users, new_user_payload):
+        reg = users.register(new_user_payload)
Необходимо исправить здесь и далее: необходимо сделать allure-аннотации для каждого метода отправки запроса. При такой реализации подходит как контекст-менеджер with allure.step, так навесить декоратор на соответствующий метод отправки
