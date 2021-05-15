
// Элемент для выбора файлов.
var INPUT = document.querySelector('input[name="readable"]');
// Элемент для вывода сгенерированной таблицы.
var PREVIEW = document.querySelector('#preview');
// Регулярное выражение для проверки расширения файла.
var REGEX = new RegExp('(.*?)\.(csv)$', 'i');


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

        // Читаем содержимое как текстовый файл.
        reader.readAsText(file);
    } else {
        // Мизерная обработка ошибок.
        alert('Файл не выбран либо его формат не поддерживается.');
        event.target.value = '';
    }
}


var index_value = new Array();
k = 0;
c = 0;


// Функция отрисовки таблицы.
function renderTable(data) {
    // Предварительно создадим элементы,
    // отвечающие за каркас таблицы.
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    // Добавим класс к таблице.
    table.classList.add('table_users');
    table.style.display = "block"
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

                        k++;
                        if(k/12==1)
                        {
                            index_value[c]=cell;
                            k=-2;
                            c++
                        }
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
                    map_grid = "container_2";
                    //Рисуем карту
                    drow_map(map_grid);
                    // Добавляем заголовок таблицы к родительскому элементу.
                    table.appendChild(thead);
                    // Добавляем тело таблицы к родительскому элементу.
                    table.appendChild(tbody);
                    // Очищаем элемент для вывода таблицы.
                    PREVIEW.innerHTML = '';
                    // Добавляем саму таблицу к родительскому элементу.
                    PREVIEW.appendChild(table);
                });
                console.log(data);
}

// Регистрируем функцию обработчика события `change`,
// срабатывающего при изменении элемента выбора файла.
window.onload=function(){
    INPUT.addEventListener('change', handleFile);
}




function drow_map(map_class){

    container = document.getElementById("container_2").style.display="block";

    var data = [
        ['ru-3637',Math.trunc(index_value[0])],
        ['ru-ck', Math.trunc(index_value[1])],
        ['ru-ar', Math.trunc(index_value[2])],
        ['ru-nn', Math.trunc(index_value[3])],
        ['ru-yn', Math.trunc(index_value[4])],
        ['ru-ky', Math.trunc(index_value[5])],
        ['ru-sk', Math.trunc(index_value[6])],
        ['ru-kh', Math.trunc(index_value[7])],
        ['ru-sl', Math.trunc(index_value[8])],
        ['ru-ka', Math.trunc(index_value[9])],
        ['ru-kt', Math.trunc(index_value[10])],
        ['ru-2510',Math.trunc(index_value[11])],
        ['ru-rz', Math.trunc(index_value[12])],
        ['ru-sa', Math.trunc(index_value[13])],
        ['ru-ul', Math.trunc(index_value[14])],
        ['ru-om', Math.trunc(index_value[15])],
        ['ru-ns', Math.trunc(index_value[16])],
        ['ru-mm', Math.trunc(index_value[17])],
        ['ru-ln', Math.trunc(index_value[18])],
        ['ru-sp', Math.trunc(index_value[19])],
        ['ru-ki', Math.trunc(index_value[20])],
        ['ru-kc', Math.trunc(index_value[21])],
        ['ru-in', Math.trunc(index_value[22])],
        ['ru-kb', Math.trunc(index_value[23])],
        ['ru-no', Math.trunc(index_value[24])],
        ['ru-st', Math.trunc(index_value[25])],
        ['ru-sm', Math.trunc(index_value[26])],
        ['ru-ps', Math.trunc(index_value[27])],
        ['ru-tv', Math.trunc(index_value[28])],
        ['ru-vo', Math.trunc(index_value[29])],
        ['ru-iv', Math.trunc(index_value[30])],
        ['ru-ys', Math.trunc(index_value[31])],
        ['ru-kg', Math.trunc(index_value[32])],
        ['ru-br', Math.trunc(index_value[33])],
        ['ru-ks', Math.trunc(index_value[34])],
        ['ru-lp', Math.trunc(index_value[35])],
        ['ru-ms', Math.trunc(index_value[36])],
        ['ru-ol', Math.trunc(index_value[37])],
        ['ru-nz', Math.trunc(index_value[38])],
        ['ru-pz', Math.trunc(index_value[39])],
        ['ru-vl', Math.trunc(index_value[40])],
        ['ru-vr', Math.trunc(index_value[41])],
        ['ru-ko', Math.trunc(index_value[42])],
        ['ru-sv', Math.trunc(index_value[43])],
        ['ru-bk', Math.trunc(index_value[44])],
        ['ru-ud', Math.trunc(index_value[45])],
        ['ru-mr', Math.trunc(index_value[46])],
        ['ru-cv', Math.trunc(index_value[47])],
        ['ru-cl', Math.trunc(index_value[48])],
        ['ru-ob', Math.trunc(index_value[49])],
        ['ru-sr', Math.trunc(index_value[50])],
        ['ru-tt', Math.trunc(index_value[51])],
        ['ru-to', Math.trunc(index_value[52])],
        ['ru-ty', Math.trunc(index_value[53])],
        ['ru-ga', Math.trunc(index_value[54])],
        ['ru-kk', Math.trunc(index_value[55])],
        ['ru-cn', Math.trunc(index_value[56])],
        ['ru-kl', Math.trunc(index_value[57])],
        ['ru-da', Math.trunc(index_value[58])],
        ['ru-ro', Math.trunc(index_value[59])],
        ['ru-bl', Math.trunc(index_value[60])],
        ['ru-tu', Math.trunc(index_value[61])],
        ['ru-ir', Math.trunc(index_value[62])],
        ['ru-ct', Math.trunc(index_value[63])],
        ['ru-yv', Math.trunc(index_value[64])],
        ['ru-am', Math.trunc(index_value[65])],
        ['ru-tb', Math.trunc(index_value[66])],
        ['ru-tl', Math.trunc(index_value[67])],
        ['ru-ng', Math.trunc(index_value[68])],
        ['ru-vg', Math.trunc(index_value[69])],
        ['ru-kv', Math.trunc(index_value[70])],
        ['ru-me', Math.trunc(index_value[71])],
        ['ru-ke', Math.trunc(index_value[72])],
        ['ru-as', Math.trunc(index_value[73])],
        ['ru-pr', Math.trunc(index_value[74])],
        ['ru-mg', Math.trunc(index_value[75])],
        ['ru-bu', Math.trunc(index_value[76])],
        ['ru-kn', Math.trunc(index_value[77])],
        ['ru-kd', Math.trunc(index_value[78])],
        ['ru-ku', Math.trunc(index_value[79])],
        ['ru-al', Math.trunc(index_value[80])],
        ['ru-km', Math.trunc(index_value[81])],
        ['ru-pe', Math.trunc(index_value[82])],
        ['ru-ad', Math.trunc(index_value[83])]
    ];

    /*
    var data = [
        ['ru-3637',0],
        ['ru-ck', 1],
        ['ru-ar', 2],
        ['ru-nn', 3],
        ['ru-yn', 4],
        ['ru-ky', 5],
        ['ru-sk', 6],
        ['ru-kh', 7],
        ['ru-sl', 8],
        ['ru-ka', 9],
        ['ru-kt', 10],
        ['ru-2510',11],
        ['ru-rz', 12],
        ['ru-sa', 13],
        ['ru-ul', 14],
        ['ru-om', 15],
        ['ru-ns', 16],
        ['ru-mm', 17],
        ['ru-ln', 18],
        ['ru-sp', 19],
        ['ru-ki', 20],
        ['ru-kc', 21],
        ['ru-in', 22],
        ['ru-kb', 23],
        ['ru-no', 24],
        ['ru-st', 25],
        ['ru-sm', 26],
        ['ru-ps', 27],
        ['ru-tv', 28],
        ['ru-vo', 29],
        ['ru-iv', 30],
        ['ru-ys', 31],
        ['ru-kg', 32],
        ['ru-br', 33],
        ['ru-ks', 34],
        ['ru-lp', 35],
        ['ru-ms', 36],
        ['ru-ol', 37],
        ['ru-nz', 38],
        ['ru-pz', 39],
        ['ru-vl', 40],
        ['ru-vr', 41],
        ['ru-ko', 42],
        ['ru-sv', 43],
        ['ru-bk', 44],
        ['ru-ud', 45],
        ['ru-mr', 46],
        ['ru-cv', 47],
        ['ru-cl', 48],
        ['ru-ob', 49],
        ['ru-sr', 50],
        ['ru-tt', 51],
        ['ru-to', 52],
        ['ru-ty', 53],
        ['ru-ga', 54],
        ['ru-kk', 55],
        ['ru-cn', 56],
        ['ru-kl', 57],
        ['ru-da', 58],
        ['ru-ro', 59],
        ['ru-bl', 60],
        ['ru-tu', 61],
        ['ru-ir', 62],
        ['ru-ct', 63],
        ['ru-yv', 64],
        ['ru-am', 65],
        ['ru-tb', 66],
        ['ru-tl', 67],
        ['ru-ng', 68],
        ['ru-vg', 69],
        ['ru-kv', 70],
        ['ru-me', 71],
        ['ru-ke', 72],
        ['ru-as', 73],
        ['ru-pr', 74],
        ['ru-mg', 75],
        ['ru-bu', 76],
        ['ru-kn', 77],
        ['ru-kd', 78],
        ['ru-ku', 79],
        ['ru-al', 80],
        ['ru-km', 81],
        ['ru-pe', 82],
        ['ru-ad', 83]
    ];
    */
    // Create the chart
    Highcharts.mapChart(map_class.toString(), {
        chart: {
            map: 'countries/ru/ru-all'
        },

        title: {
            text: 'Индекс счастья'
        },
        /*
        subtitle: {
            text: 'Source map: <a href="http://code.highcharts.com/mapdata/countries/ru/ru-all.js">Russia</a>'
        },
        */
        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0
        },

        series: [{
            data: data,
            name: 'Random data',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }]
    });
}
var save_data = function()
{
    var data = JSON.stringify(object)

    var request = new XMLHttpRequest()
    request.open('POST', 'сохранить_данные.php')
    request.send(data)

    request.onreadystatechange = function()
    {
        if(request.readyState === 4)
        {
            if(request.responseText)
            {
                var response = JSON.parse(request.responseText)

                if(response !== 'ok')
                {
                    alert('ошибка сохранения')
                }
            }
        }
    }
}

