### ID: 1

### Title: Проверка, что введенное в поисковую строку искомое слово находится на первой позиции в suggestion list 



 **Description**: проверка того, что при вводе слова в поисковую строку, система отображает его на первой позиции в suggestion

 **Severity**: Critical

 **Priority**: High

 **Milestone**: Release 1.0

 **Environment**: 

 * Chrome (newer  v.122.0.6261.131   (64 bits) )
 * Windows 10
  

 **Pre-conditions**: нет

 **Test data**:

 *  Искомое слово - Selenium
 *  Адрес сайта - [yandex.ru](https://ya.ru/)
  
#### Steps and expected result 


| Steps           | Expected result  |
|-----------------|-----------------|
| 1. Открыть [сайт](https://ya.ru/) | Сайт корректно открывается и отображается |
| 2. Кликнуть по поисковой строке | Курсор появился в поисковой строке |
| 3 .Ввести искомое слово "Selenium" в поисковую строку | Введенные символы корректно отображаются, по мере ввода символов появляется suggestion list |
| 4. Проверить, что слово "Selenium" появилось на первой строчке в suggestion list поиска  | "Selenium" появилось на первой строчке в suggestion list поиска |



