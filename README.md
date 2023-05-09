<h1>Формирование Excel-файлов с данными</h1>

Эта программа позволяет сформировать несколько Excel-файлов с данными. Для каждого файла генерируется заданное 
количество записей. Каждая запись содержит случайно сгенерированный СНИЛС и ИНН физического лица.

<h2>Инструкция по использованию</h2>

<h3>1 Вариант</h3>

Запустить main.exe файл, который находится в директории "dist"

<h3>2 Вариант</h3>

Для использования программы необходимо выполнить следующие шаги:
<ol>
<li>Создайте виртуальное окружение с помощью следующей команды:</li>

    python3 -m venv env

<li>Активируйте виртуальное окружение:</li>

    source env/bin/activate (для Linux и macOS)
    env\Scripts\activate (для Windows)

<li>Установите зависимости, выполнив следующую команду:</li>
    
    pip install -r requirements.txt

<li>После установки зависимостей запустите программу, выполнив команду:</li>

    python main.py
</ol>

<h2>Описание файлов</h2>
<ul>
<li>main.py - главный файл программы, который запускает пользовательский интерфейс и обрабатывает пользовательский ввод.</li>
<li>get_inn_snils.py - вспомогательный модуль, который содержит функции для генерации СНИЛС и ИНН физического лица.</li>
</ul>

<h2>Интерфейс пользователя</h2>
Программа имеет простой интерфейс, состоящий из двух полей ввода и кнопки "Сформировать". При нажатии на кнопку 
начинается процесс генерации файлов, а индикатор прогресса отображает текущее состояние процесса. После завершения 
генерации появляется окно с информацией о завершении процесса.