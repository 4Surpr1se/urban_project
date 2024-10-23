# Алгоритмы (https://tproger.ru/problems/technocup-problems-2017)

https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

https://leetcode.com/problems/lru-cache/description/?envType=problem-list-v2&envId=design

https://leetcode.com/problems/lfu-cache/description/?envType=problem-list-v2&envId=design (сложнее)

# Декораторы

реализация декоратора lru_cache на основе алгоритма из предыдущего шага

# Классы

добавить все приколы что объяснялись в теме
Создание собственной ORM
(Создание абстракт класса, на его основе релизация работы с sqlite)
Исслеодвать есть ли резон держать только один экземпляр инстанса нашей orm с помощью нашего кэша (по идее есть, ведь наш
орм инстанс будет хранить объект коннекшена с дб и плодить их нам смысла нет)
мб добавить

```py
class Connections:
    @staticmethod
    @contextmanager
    def sqlite_connect(db_path: str):
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
```

# Аннотации

добавить poetry аннотацию и что прикольное с инспект и тд, так же какие=то приколы линтеров объяснить или фитчи
реализиовать типо автопроверки

# Асинхронщина

Приложение на фаст апи реализующее нашу орм

# Тестирование нашего АПИ

# Погружение в проектирование архитектуры веб-сервиса

# SOAP простой payment gateway

# GraphQL https://habr.com/ru/articles/765064/
# GraphQL + Websocket сделать
Использовать, где понадобится Веб-приложения:
Для динамических веб-приложений, где требуется частое обновление данных,
GraphQL предоставляет более быстрый и эффективный способ получения информации.

# gRPC Какая-то микросервисная фишка

# Rest + Django аутентификация