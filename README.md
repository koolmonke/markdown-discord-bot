## markdown-discord-bot

Это бот для отображения превью текстовых файлов загруженных отправленных в Discord канал. Поскольку Discord встроил
функцию превью в Discord-клиент этот бот больше не поддерживается

### Как запустить

Пример для docker-compose для запуска сервиса этого бота

```yaml
services:
  discord-service:
    build: .
    environment:
      DISCORD_TOKEN: <your_token_here>
    restart: always
```