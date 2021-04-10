
/*

//Парсинг cvs файла с другого сайта

Papa.parse("http://example.com/bigfoo.csv", {
    download: true,
    step: function (row) {
        console.log("Row:", row.data);
    },
    complete: function () {
        console.log("All done!");
    }

    // Функция отрисовки таблицы.
    function renderTable(data)
{
    // Предварительно создадим элементы,
    // отвечающие за каркас таблицы.
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    // Добавим класс к таблице.
    table.classList.add('table');

    // Разбиваем входящие данные построчно.
    // Разделитель - перенос строки.
    // Перебираем полученный массив строк.
    data.split(/\r\n|\r|\n/)
        .forEach(function (row, index) {
            // Создадим элемент строки для таблицы.
            let trow = document.createElement('tr');

            // Разбиваем каждую строку на ячейку.
            // Разделитель - точка с запятой.
            // Перебираем полученный массив будущих ячеек.
            row.split(/;/).forEach(function (cell) {
                // Создадим элемент ячейки для таблицы.
                let tcell = document.createElement(index > 0 ? 'td' : 'th');
                // Заполним содержимое ячейки.
                tcell.textContent = cell;
                // Добавляем ячейку к родительской строке.
                trow.appendChild(tcell);
            });

            // Добавляем строку к родительскому элементу.
            // Если индекс строки больше нуля,
            // то родительский элемент - `tbody`,
            // в противном случае- `thead`.
            index > 0 ? tbody.appendChild(trow) : thead.appendChild(trow);
        });

    // Добавляем заголовок таблицы к родительскому элементу.
    table.appendChild(thead);
    // Добавляем тело таблицы к родительскому элементу.
    table.appendChild(tbody);

    // Очищаем элемент для вывода таблицы.
    PREVIEW.innerHTML = '';
    // Добавляем саму таблицу к родительскому элементу.
    PREVIEW.appendChild(table);
}
})
;
*/




// Элемент для выбора файлов.
const INPUT = document.querySelector('input[name="readable"]');
// Элемент для вывода сгенерированной таблицы.
const PREVIEW = document.querySelector('#preview');
// Регулярное выражение для проверки расширения файла.
const REGEX = new RegExp('(.*?)\.(csv)$', 'i');

function decode(responseArrayBuffer) {
    const
        dataView = new DataView(responseArrayBuffer),
        decoder = new TextDecoder('windows-1251');
    return decoder.decode(dataView);
}

fetch(file)
    .then(response => response.arrayBuffer())
    .then(decode)
    .then(console.log)
    .catch(err => console.log(err.message));


// Функция, отрабатывающая при выборе файла.


function handleFile(event) {
    // Выбираем первый файл из списка файлов.
    const file = event.target.files[0];

    // Если файл выбран и его расширение допустимо,
    // то читаем его содержимое и отправляем
    // в функцию отрисовки таблицы.
    if (file && REGEX.test(file.name)) {
        // Создаем экземпляр объекта.
        const reader = new FileReader();

        // Чтение файла асинхронное, поэтому
        // создание таблицы привязываем к событию `load`,
        // которое срабатывает при успешном завершении операции чтения.
        reader.onload = (e) =>renderTable(e.target.result);
        //reader.onload = (e) => MapImput(e.target.result)
        // Читаем содержимое как текстовый файл.
        reader.readAsText(file);
    } else {
        // Мизерная обработка ошибок.
        alert('Файл не выбран либо его формат не поддерживается.');
        event.target.value = '';
    }
}

/*
function MapImput (data){

}
*/

// Функция отрисовки таблицы.
function renderTable(data) {
    // Предварительно создадим элементы,
    // отвечающие за каркас таблицы.
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    // Добавим класс к таблице.
    table.classList.add('table_users');

    // Разбиваем входящие данные построчно.
    // Разделитель - перенос строки.
    // Перебираем полученный массив строк.
    data.split(/\r\n|\r|\n/)
        .forEach(function (row, index) {
            // Создадим элемент строки для таблицы.
            let trow = document.createElement('tr');
            trow.classList.add('tr_users')
            // Разбиваем каждую строку на ячейку.
            // Разделитель - точка с запятой.
            // Перебираем полученный массив будущих ячеек.
            row.split(/,/).forEach(function (cell) {
                // Создадим элемент ячейки для таблицы.
                let td = document.createElement( index > 0 ? 'td':'th');
                td.classList.add('td_users')
                // Заполним содержимое ячейки.
                td.textContent = cell;
                // Добавляем ячейку к родительской строке.
                trow.appendChild(td);
            });

            // Добавляем строку к родительскому элементу.
            // Если индекс строки больше нуля,
            // то родительский элемент - `tbody`,
            // в противном случае- `thead`.
            index > 0 ? tbody.appendChild(trow) : thead.appendChild(trow);
        });

    // Добавляем заголовок таблицы к родительскому элементу.
    table.appendChild(thead);
    // Добавляем тело таблицы к родительскому элементу.
    table.appendChild(tbody);

    // Очищаем элемент для вывода таблицы.
    PREVIEW.innerHTML = '';
    // Добавляем саму таблицу к родительскому элементу.
    PREVIEW.appendChild(table);
}

// Регистрируем функцию обработчика события `change`,
// срабатывающего при изменении элемента выбора файла.
INPUT.addEventListener('change', handleFile);


