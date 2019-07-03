console.log('table_inserter.js loaded');


function clear_table() {
    console.log('clear_table runned');
    tbody = document.getElementById('tbody_data');
    tbody.innerHTML = '';
    // for (i=1; i<table.rows.length;i++) {
    //     table.deleteRow(i)
    // }
}

function insert_to_table(list_data){
    console.log('insert_to_table function runed');
    clear_table();
    tbody = document.getElementById('tbody_data');
    console.log('tbody',tbody);
    var temp_row;
    var temp_cell;
    var car_data;
    for (i=0; i<list_data.length;i++) {
        car_data=list_data[i];

        temp_row = tbody.insertRow(i);
        temp_row.setAttribute("class", car_data[8], 0);
        for (j=0; j<7;j++) {
            temp_cell = temp_row.insertCell(j);
            temp_cell.innerHTML = '<a href="'+car_data[7]+'">'+car_data[j]+'</a>'
        }
    }
}