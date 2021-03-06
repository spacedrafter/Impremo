# План тестирования

## Введение
В этом документа будет описан план тестирования разрабатываемого приложения.
Цель тестирования: проверить работоспобоность приложения.

## Объекты тестирования
В разрабатываемом приложении выбраны три страницы для проведения тестирования:

- "Регистрация";
- "Добавить пост";
- "Комментирование";

Атрибуты качества платформы по ISO 25010:
1. функциональность
- функциональная полнота: приложение должно выполнять все заявленные функции;
- функциональная корректность: приложение должно выполнять все заявленные функции корректно;
2. производительность
- временная характеристика: приложение должно загружать данные не более 1 секунды;
3. переносимость:
- кроссбраузерность: приложение должно корректно работать на различных браузерах.
4. удобство использования
- адаптивный дизайн: приложение должно подстраиваться под размер окна браузера.

Данные атрибуты были выбраны с учётом специфики приложения.

## Риски
Разабатываемое приложение является приложением типа клиент-сервер. Большинство рисков возникает при неполадках на стороне сервера, в следствии этого возникают различные проблемы у клиента. Это могут быть неполадки с базами данных, в которых хранится вся информация приложения, или неработоспособность сервера, которая не позволит клиентам использовать приложание.

## Аспекты тестирования

## Регистрация
Этот вариант использования необходимо протестировать на:
1. Добавление нового пользователя;
2. Добавление пользователя с некорректными данными;

## Добавление поста
Этот вариант использования необходимо протестировать на:
1. Добавление поста пользователем;
2. Добавление пустого поста;

## Комментирование
Этот вариант использования необходимо протестировать на:
1. Добавление комментария к посту и сохранение изменений;
2. Добавление пустого комментария к посту и сохранение изменений;


## Подходы к тестированию
Для тестирования приложения будет использовано ручное тестирование.

## Представление результатов
Представление результатов будет представлено в документе [test_result.md](https://github.com/Sergey-Sil/Impremo/tree/master/Tests/test_result.md) .

## Выводы
Данный план теста даёт нам возможность проверить функционал приложения, доступный на текущем уровне реализации.
