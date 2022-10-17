# Opportunity-Cup 2022 - Хакатон от Сбера


* [Front-end](#front)
  * [bad_age_update](#bau)
  * [bad_time_update](#btu)
  * [many_clicks_update](#mcu)
  * [night_time_update](#ntu)
  * [map](#map)
  * [upload](#upload)
* [Back-end](#back)
  * [1. POST /import_transactions](#import)
  * [2. GET /get_transactions](#get_t)
  * [3. GET /get_cities](#get_c)
  * [4. GET /get_transactions_by_ids/$transactions](#get_tbi)
  * [5. GET /set_many_click_delay/$delay](#set_mcd)
  * [6. GET /set_bad_time/$time_from/$time_to](#set_bt)
  * [7. GET /set_night_time/$time_from/$time_to](#set_nt)
  * [8. GET /set_bad_age/$age_from/$age_to](#set_ba)
  * [9. GET /set_equal_delay/$delay](#set_ed)
* [Паттерны](#patterns)
  * [1. Множество кликов](#pat_1)
  * [2. Операции с одного устройства](#pat_2)
  * [3. Подозрительная активность в ночное время](#pat_3)
  * [4. Невалидный аккаунт](#pat_4)
  * [5. Неактивное время](#pat_5)
  * [6. Неподходящий возраст](#pat_6)
* [Инструкции](#instruct)
  * [Установка зависимостей](#libs)
  * [Запуск back-end приложения](#start_back)
  * [Запуск front-end приложения](#start_front)
  
  
  ## <a name="front"></a> Front-end
  ### <a name="bau"></a> bad_age_update
  ### <a name="btu"></a> bad_time_update
  ### <a name="mcu"></a> many_clicks_update
  ### <a name="ntu"></a> night_time_update
  ### <a name="map"></a> map
  ### <a name="upload"></a> upload
  ## <a name="back"></a> Back-end
  Разработка back-end'а велась с использованием веб-фреймворка Flask (Python)
  ### <a name="import"></a> 1. POST /import_transactions
  Принимает на вход `json` файл или `json` данные с транзакциями.
  
  Возвращает id выявленных мошеннических операция по паттернам.
  
  При невалидных данных возвращает `400`: `{"code": 400,"message": "Validation Failed"}`
  ### <a name="get_t"></a> 2. GET /get_transactions
  Возвращает все транзакции, хранящиеся в базе данных в формате `json`.
  ### <a name="get_c"></a> 3. GET /get_cities
  Возвращает название и координаты городов, которые есть в базе данных в формате `json`.
  ### <a name="get_tbi"></a> 4. GET /get_transactions_by_ids/$transactions
  Принимает строку, в которой через запятую перечислены `id` транзакций.
  
  Возвращает информацию обо всех перечисленных транзакциях в формате `json`.
  ### <a name="set_mcd"></a> 5. GET /set_many_click_delay/$delay
  Принимает минимальное количество минут между транзакциями.
  
  Устанавливает это значение для последующих проверок.
  ### <a name="set_bt"></a> 6. GET /set_bad_time/$time_from/$time_to
  Принимает 
  ### <a name="set_nt"></a> 7. GET /set_night_time/$time_from/$time_to
  ### <a name="set_ba"></a> 8. GET /set_bad_age/$age_from/$age_to
  ### <a name="set_ed"></a> 9. GET /set_equal_delay/$delay
  ## <a name="patterns"></a> Паттерны
  ### <a name="pat_1"></a> Множество кликов
  ### <a name="pat_2"></a> Операции с одного устройства
  ### <a name="pat_3"></a> Подозрительная активность в ночное время
  ### <a name="pat_4"></a> Невалидный аккаунт
  ### <a name="pat_5"></a> Неактивное время
  ### <a name="pat_6"></a> Неподходящий возраст
  ## <a name="instruct"></a> Инструкции
  ### <a name="libs"></a> Установка зависимостей
  ### <a name="start_back"></a> Запуск back-end приложения
  ### <a name="start_front"></a> Запуск front-end приложения
