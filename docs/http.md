# Ресурс

Ресурс — это ключевая абстракция, на которой концентрируется протокол HTTP. Ресурс — это все, что вы хотите показать внешнему миру через ваше приложение. Например, если мы пишем приложение для управления задачами, экземпляры ресурсов будут следующие:

Конкретный пользователь
Конкретная задача
Список задач

# URI ресурса

Когда вы разрабатываете RESTful сервисы, вы должны сосредоточить свое внимание на ресурсах приложения. Способ, которым мы идентифицируем ресурс для предоставления, состоит в том, чтобы назначить ему URI — универсальный идентификатор ресурса. Например:

Создать пользователя: POST /users
Удалить пользователя: DELETE /users/1
Получить всех пользователей: GET /users
Получить одного пользователя: GET /users/1


# Компоненты HTTP

HTTP определяет следующую структуру запроса:

- строка запроса (request line) — определяет тип сообщения
- заголовки запроса (header fields) — характеризуют тело сообщения, параметры передачи и прочие сведения
- тело сообщения (body) — необязательное

HTTP определяет следующую структуру ответного сообщения (response):

- строка состояния (status line), включающая код состояния и сообщение о причине
- поля заголовка ответа (header fields)
- дополнительное тело сообщения (body)

# Методы HTTP-запроса

Метод, используемый в HTTP-запросе, указывает, какое действие вы хотите выполнить с этим запросом. Важные примеры:

- GET: получить подробную информацию о ресурсе
- POST: создать новый ресурс
- PUT: обновить существующий ресурс
- DELETE: Удалить ресурс

# Links
1. HTTP status codes - описание для каждого кода - https://restapitutorial.ru/httpstatuscodes.html
