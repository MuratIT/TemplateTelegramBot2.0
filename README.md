# TemplateTelegramBot2.0

Этот шаблон предназначен для создания Telegram-бота с использованием библиотеки aiogram версии 3.16.0, а также интеграции с FastAPI версии 0.115.6 через Webhook или Long Polling.

## Ключевые возможности шаблона

1. Динамическая загрузка модулей и middleware-компонентов.
2. Применение объектно-ориентированного программирования (ООП).

### Динамическая загрузка модулей

При запуске бот автоматически загружает все модули, находящиеся в директории modules. Каждый модуль должен наследовать базовый класс Module, который расположен в директории classes.

Для регистрации обработчиков сообщений необходимо переопределить метод register_handlers в вашем модуле. В этом методе вы можете зарегистрировать все необходимые обработчики событий.

**Пример модуля:**

```python
class MyModule(Module):
    def __init__(self):
        super(MyModule, self).__init__()

    @staticmethod
    async def handle(message: Message):
        await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

    def register_handlers(self):
        self.router.message.register(self.handle, CommandStart())
```

Обратите внимание, что имя класса должно совпадать с именем файла модуля.

#### Динамическая загрузка middleware-компонентов

Бот также поддерживает автоматическую загрузку middleware-компонентов, находящихся в директории middlewares. Эти компоненты должны быть реализованы согласно спецификациям библиотеки aiogram и будут динамически подключены к обновлению состояния бота.

Пример middleware-компонента:

```python
class MyMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        print("Before handler")
        result = await handler(event, data)
        print("After handler")
        return result
```

Как и в случае с модулями, название класса middleware должно соответствовать названию файла.

### Фильтры и клавиатуры

Файлы фильтров и клавиатур могут быть размещены в соответствующих директориях (filters и keyboards) и импортированы в ваши модули для использования с обработчиками событий. Все фильтры и клавиатуры создаются с применением возможностей библиотеки aiogram. Этот функционал является опциональным.


### Переменные окружения

В корневой директории проекта находится файл .env, где необходимо задать следующие параметры:

- TOKEN: Токен вашего бота, полученный у @BotFather.
- BASE_URL: URL, на который Telegram будет отправлять обновления (используется при работе через Webhook).
- WEBHOOK_PATH: Путь к вашему боту, начинающийся с /. Этот параметр обязателен при использовании Webhook. Вы можете задать любое строковое значение.
- REDIS_URL: URL для подключения к Redis для работы с машинным состоянием и хранения состояния в Redis. 

### Запуск бота

Вы можете запустить бота двумя способами:

1. Long Polling: Используйте следующую команду:
   
```bash
python main.py
```
   
   
2. Webhook: Для запуска через Webhook выполните команду:
   
```bash
uvicorn main:app.app
```


3. Запуск через Docker Compose. Обратите внимание, что настройка проекта подразумевает запуск бота через Webhook.

Для начала нужно настроить проект под ваш домен и выпустить SSL-сертификаты.

Укажите свой домен в трех файлах:

- ./init-letsencrypt.sh
- ./data/nginx/app.conf
- ./data/nginx/letsencrypt/app.conf

Также для корректной работы бота укажите домен в файле .env,
установив значение переменной BASE_URL в виде URL, например: https://webside.com.

В файле ./init-letsencrypt.sh необходимо указать свой email-адрес.
Сделайте файл init-letsencrypt.sh исполняемым с помощью команды:
```bash
chmod +x init-letsencrypt.sh
```
Запустите файл:
```bash
./init-letsencrypt.sh
```

Следуйте инструкциям, которые появятся в процессе выполнения.

После выпуска SSL-сертификата можно запустить контейнеры Docker Compose командой:
```bash
docker-compose up -d
```

## Примечание

Шаблон может изменяться и совершенствоваться со временем, поэтому рекомендуется периодически проверять наличие обновлений.