# Python_base4
Программа сделана для курса Основы питон
## Пример работы
Код делает следующее, из *исходной картинки*:![image](https://user-images.githubusercontent.com/124410504/228325024-fbf04fb3-ed31-41ee-96d1-d07d965a5472.png)\
создает *2 одинаковые картинки* с разным расширением:\
![image](https://user-images.githubusercontent.com/124410504/228325732-88a246a4-0b0c-46df-95f2-533b8a1df5f9.png)\

и\
\
![image](https://user-images.githubusercontent.com/124410504/228325811-acc93bd4-57e3-4652-9fd0-84f2f75cce16.png)

## технические моменты
Исходная картинка должна называться ```image.jpg``` и распологаться в одной директории с кодом. Также ее mode (цветовой режим) должен быть RGB.

## улучшение кода, информация
Впринципе, можно легко доработать код, чтоб он работал и с другими mode (например SMYK), как это сделать можно понять, прочитав [библиотеку PILLOW](https://dvmn.org/encyclopedia/modules/pillow/).
В коде есть переменная ```count_pixel```, она и определяет насколько картинка будет *искаженной*. Пример дан для ```count_pixel = 60```.\
Несколько примеров для разных ```count_pixel```

```count_pixel = 100```\
![image](https://user-images.githubusercontent.com/124410504/228328675-85102d64-a34a-4cc1-92e9-82ccf65df8ae.png)\
\
```count_pixel = 150```\
![image](https://user-images.githubusercontent.com/124410504/228328882-8f41b281-d1d6-4ece-8f55-03327d7bbfc3.png)

