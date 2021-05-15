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
    //console.log("Импут124412513651235е213462346н2346"+JSON.stringify(data));
    let responseData;
    $.post("/",
        {
            data:JSON.stringify(data)
        },
        function(data, status){
            responseData = data;
            alert(responseData);
            console.log(responseData);
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
                        if(k/15==1)
                        {
                            index_value[c]=cell;
                            k=-2;
                            c++
                        }
                        // Создадим элемент ячейки для таблицы.s
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
        });
    
}