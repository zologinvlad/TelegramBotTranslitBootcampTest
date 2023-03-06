# TelegramBotTranslitBootcampTest
## Инструкия по запуску телеграмм-бота через Docker

1. Сделать `fork` репозитория, а затем `git clone` на свой ПК. :white_check_mark:
2. Открыть приложение 'Telegram', перейти в бот @BotFather, и создать своего бота. :white_check_mark:
3. После создания бота, Вы получите свой `TOKEN`. :white_check_mark:
4. TOKEN скопируйте в dockerfile в строку `ENV TOKEN='<your_token>'`. :white_check_mark:
5. Создайте Docker image прописав в терминале команду `docker build .` (при создание image необходимо находиться в папке с файлами данного бота, в противном случае укажите корректный путь до файла). :white_check_mark:
6. Для запуска бота через Docker нужно получить `IMAGE ID`, сделать это можно прописать в терминале команду `docker images`. :white_check_mark:
7. Затем запустите Docker через терминал, прописав команду `docker run -d -p 80:80 <IMAGE ID>` подставив полученный ранее ID взамен `<IMAGE ID>`. :white_check_mark:
8. Бот запущен, чтобы остановить его, в терминале пропишите команду `docker stop <CONTAINER ID>` (CONTAINER ID можно посмотреть прописав команду `docker ps`). :white_check_mark:
