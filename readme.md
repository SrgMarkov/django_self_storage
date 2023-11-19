# Сайт - Доставка и бережное хранение ваших вещей

### Как это работает
Текущий проект предусматривает развертывание и запуск сайт для доставки и бережного хранения ваших вещей.

### Как запустить
Python 3-й версии должен быть установлен. Устанавливаем зависимости
```sh
pip install -r requirements.txt
```

#### Запуск с тестовыми данными 
Для того чтобы запустить сайт с тестовыми данными нам понадобиться 2а дополнительных файла
`boxx.json`
`images_qr.zip` - необходимо распаковать в папке

```django_self_storage/backend```
далее выполнить команду
```sh
python3 manage.py loaddata boxx.json
```

Данная команда создаст заполненные тестовыми данными таблицы в админ панели

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `EMAIL_HOST_USER`  
- `EMAIL_HOST_PASSWORD`  
- `SECRET_KEY`  
- `ALLOWED_HOSTS`  
- `DEBUG`  

### Отправка email
Для отправки email необходимо заполнить логин и пароль от ящика gmail.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org)
