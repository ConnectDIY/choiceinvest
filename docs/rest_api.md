REST расшифровывается как REpresentational State Transfer.

# REST и Ресурсы

Важно отметить, что с REST вам нужно думать о приложении с точки зрения ресурсов:
Определите, какие ресурсы вы хотите открыть для внешнего мира Используйте глаголы, уже определенные протоколом HTTP, для
выполнения операций с этими ресурсами.

Вот как обычно реализуется служба REST:

- **Формат обмена данными**: здесь нет никаких ограничений. JSON — очень популярный формат, хотя можно использовать и
  другие, такие как XML
- **Транспорт**: всегда HTTP. REST полностью построен на основе HTTP.
- **Определение сервиса**: не существует стандарта для этого, а REST является гибким. Это может быть недостатком в
  некоторых сценариях, поскольку потребляющему приложению может быть необходимо понимать форматы запросов и ответов.
  Однако широко используются такие языки определения веб-приложений, как WADL (Web Application Definition Language) и
  Swagger.

REST фокусируется на ресурсах и на том, насколько эффективно вы выполняете операции с ними, используя HTTP.

Contract First подход к разработке REST API Потребитель должен знать детали предоставляемой услуги. По этой причине
должен быть заключен договор. Договор на обслуживание определяет:

- Каковы входы и выходы из сервиса?
- По какому URL-адресу доступен сервис?
- Как отправлять авторизацию?

## When

https://dzone.com/articles/design-first-or-code-first-whats-the-best-approach

- When Developer Experience Matters
- When Delivering Mission-Critical APIs
- When Ensuring Good Communication

# Code-First подход

## When

- When Delivery Speedy Matters
- When Developing Internal APIs

# Best practices for REST API design

Далее выдержка из https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/

## Use JSON

Лучше всего для котейнера передачи данных использовать JSON, хотя можно и другие. FastAPI по умолчанию превращает модели
данных в JSON.

Чтобы убедиться, что, когда наше приложение REST API отвечает с помощью JSON, клиенты интерпретируют его как таковой, мы
должны установить `Content-Type` в заголовке ответа на `application/json` после того, как запрос сделан. Многие
фреймворки делают это за тебя, но стоит убедиться.

Единственное исключение — если мы пытаемся отправлять и получать файлы между клиентом и сервером. Затем нам нужно
обработать ответы файлов и отправить данные формы с клиента на сервер.

## Use nouns instead of verbs in endpoint paths

Мы не должны использовать глаголы в наших путях к конечным точкам. Вместо этого мы должны использовать существительные,
которые представляют сущность, конечную точку, которую мы извлекаем или манипулируем, в качестве имени пути.

Это связано с тем, что в нашем методе HTTP-запроса уже есть глагол. Наличие глаголов в путях конечных точек нашего API
бесполезно и делает их излишне длинными, поскольку они не передают никакой новой информации.

Действие должно быть указано методом HTTP-запроса, который мы делаем.

- GET retrieves resources.
- POST submits new data to the server.
- PUT updates existing data.
- DELETE removes data.

The verbs map to CRUD operations.

Примеры:

1. GET /articles/ для получения новостных статей.
2. PUT /articles/:id is for updating the article with the given id.
3. DELETE /articles/:id is for deleting an existing article with the given ID.

`/articles` represents a REST API resource.

## Используйте логическое вложение на endpoints

При проектировании конечных точек имеет смысл сгруппировать те, которые содержат связанную информацию. То есть, если
один объект может содержать другой объект, вы должны спроектировать конечную точку так, чтобы это отражалось.

Это хорошая практика, независимо от того, структурированы ли ваши данные в базе данных таким образом. На самом деле,
может быть целесообразно избегать зеркального отображения структуры вашей базы данных на ваших конечных точках, чтобы не
давать злоумышленникам ненужную информацию.

Например, если мы хотим, чтобы конечная точка получала комментарии к новостной статье, мы должны добавить
путь `/comments`
в конец пути `/articles`. Мы можем сделать это с помощью следующего кода в
Express: `app.get('/articles/:articleId/comments'`

Однако вложенность может зайти слишком далеко. Примерно после второго или третьего уровня вложенные конечные точки могут
стать громоздкими. Вместо этого рассмотрите возможность возврата URL-адреса этих ресурсов, особенно если эти данные не
обязательно содержатся в объекте верхнего уровня.

Например, предположим, что вы хотите вернуть автора определенных комментариев. You could
use `/articles/:articleId/comments/:commentId/author`. Но это выходит из-под контроля. Вместо этого верните URI для
этого конкретного пользователя в ответе JSON: `"author": "/users/:userId"`

## Handle errors gracefully and return standard error codes

Чтобы избежать путаницы для пользователей API при возникновении ошибки, мы должны корректно обрабатывать ошибки и
возвращать коды ответов HTTP, которые указывают, какой тип ошибки произошел. Это дает сопровождающим API достаточно
информации, чтобы понять возникшую проблему. Мы не хотим, чтобы ошибки приводили к сбоям в работе нашей системы, поэтому
мы можем оставить их необработанными, а это означает, что с ними должен справиться потребитель API.

Common error HTTP status codes include:

- 400 Bad Request – This means that client-side input fails validation.
- 401 Unauthorized – This means the user isn’t not authorized to access a resource. It usually returns when the user
  isn’t authenticated.
- 403 Forbidden – This means the user is authenticated, but it’s not allowed to access a resource.
- 404 Not Found – This indicates that a resource is not found.
- 500 Internal server error – This is a generic server error. It probably shouldn’t be thrown explicitly.
- 502 Bad Gateway – This indicates an invalid response from an upstream server.
- 503 Service Unavailable – This indicates that something unexpected happened on server side (It can be anything like
  server overload, some parts of the system failed, etc.).

## Allow filtering, sorting, and pagination

Т.к. часто на бэкенде находятся базы с большим кол-вом данных, то фильтровать/сортировать/и разделять на страницы это
хорошая практика.

E.g.
`http://example.com/articles?sort=+author,-datepublished`

## Maintain good security practices

Большая часть связи между клиентом и сервером должна быть конфиденциальной, поскольку мы часто отправляем и получаем
личную информацию. Поэтому использование SSL/TLS для обеспечения безопасности является обязательным.

SSL-сертификат не так уж сложно загрузить на сервер, и его стоимость либо бесплатна, либо очень низка. Нет никаких
причин не использовать наши REST API для обмена данными по защищенным каналам, а не по открытым.

Чтобы обеспечить соблюдение принципа наименьших привилегий, нам нужно добавить проверки ролей либо для одной роли, либо
иметь более детализированные роли для каждого пользователя.

## Cache data to improve performance
Вещь нужная. Есть разные решения, одно из наиболее популярных - redis.

If you are using caching, you should also include Cache-Control information in your headers. This will help users effectively use your caching system.

## Versioning our APIs

Versioning is usually done with /v1/, /v2/, etc. added at the start of the API path.

`app.get('/v1/employees', (req, res)`

# Links

1. Best practices for REST API design - https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
2. Best practices for REST API security: Authentication and authorization
    - https://stackoverflow.blog/2021/10/06/best-practices-for-authentication-and-authorization-for-rest-apis/
3.  http://stateless.co/hal_specification.html or to https://jsonapi.org/ for hateoas introduction