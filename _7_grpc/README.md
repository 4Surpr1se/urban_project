Вам нужно будет реализовать
Cервис аутентификации на основе нашей ОРМ, структура базы данных должна быть следующей:

erDiagram
USERS ||--o{ USER_ROLES : has
USERS ||--o{ LOGIN_HISTORY : has
ROLES ||--o{ USER_ROLES : has
ROLES ||--o{ ROLE_PERMISSIONS : has
PERMISSIONS ||--o{ ROLE_PERMISSIONS : has

    USERS {
        uuid id PK
        string username
        string email
        string hashed_password
        boolean is_active
        timestamp created_at
        timestamp updated_at
    }

    ROLES {
        uuid id PK
        string name
        string description
        timestamp created_at
        timestamp updated_at
    }

    PERMISSIONS {
        uuid id PK
        string name
        string description
        timestamp created_at
        timestamp updated_at
    }

    USER_ROLES {
        uuid user_id FK
        uuid role_id FK
    }

    ROLE_PERMISSIONS {
        uuid role_id FK
        uuid permission_id FK
    }

    LOGIN_HISTORY {
        uuid id PK
        uuid user_id FK
        string ip_address
        string user_agent
        timestamp login_at
    }

Релизовать сервис нужно будет на основе протокола grpc (для этого рекомендуем
использовать [fast-grpc](https://github.com/OlegYurchik/fast-grpc)),
а аутентификация с использованием jwt.
Однако структура не должна быть привязана к транспортному протоколу и способу аутентификации,
за структурную основу можете взять Ваш `FASTAPI` cервис с реализацией орм, единственное, нужно будет добавить прослойку
аутентификации и авторизации, так же добавить интерфейс работы с пермишенами и ролями, в будущем Ваше стриминг
приложение будет обращаться к этому сервису для проверки пользователя.