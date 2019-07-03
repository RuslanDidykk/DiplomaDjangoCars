console.log('js ====================== function loaded');

function load_models(make){
    $('#model').prop('disabled', true);
    $('#trim').prop('disabled', true);
    $('#year').prop('disabled', true);
    $.ajax({
        type: "GET",
        url: "model",
        data: {
            'make': make
        },

        dataType: 'text',
        cache: false,

        success: function (list_data) {
            var myNode = document.getElementById("model");
                while (myNode.firstChild) {
                    myNode.removeChild(myNode.firstChild);
                }

            _list_data = JSON.parse(list_data);
            for (i=0; i<_list_data.length;i++) {
                $("#model").append("<option>"+_list_data[i]+"</option>");
            }
            $('#model').prop('disabled', false);
        }
    });
}


function load_trims(model){
    make = document.getElementById("make").value;
    $('#trim').prop('disabled', true);
    $('#year').prop('disabled', true);
    $.ajax({
        type: "GET",
        url: "trim",
        data: {
            'model': model,
            'make': make
        },

        dataType: 'text',
        cache: false,

        success: function (list_data) {

            var myNode = document.getElementById("trim");
                while (myNode.firstChild) {
                    myNode.removeChild(myNode.firstChild);
                }

            _list_data = JSON.parse(list_data);
            for (i=0; i<_list_data.length;i++) {
                $("#trim").append("<option>"+_list_data[i]+"</option>");
            }
            $('#trim').prop('disabled', false);
        }
    });
}


function load_years(trim){
    console.log('js load_trims function runed');
    console.log(trim);
    make = document.getElementById("make").value;
    model = document.getElementById("model").value;
    $('#year').prop('disabled', true);
    $.ajax({
        type: "GET",
        url: "year",
        data: {
            'trim': trim,
            'model': model,
            'make': make
        },

        dataType: 'text',
        cache: false,

        success: function (list_data) {

            var myNode = document.getElementById("year");
                while (myNode.firstChild) {
                    myNode.removeChild(myNode.firstChild);
                }

            _list_data = JSON.parse(list_data);
            for (i=0; i<_list_data.length;i++) {
                $("#year").append("<option>"+_list_data[i]+"</option>");
            }
             // console.log("<option>32132</option>")
            $('#year').prop('disabled', false);
        }
    });
}


function load_graph(year){
    console.log('js load_graph function runed');
    make = document.getElementById("make").value;
    model = document.getElementById("model").value;
    trim = document.getElementById("trim").value;

    $.ajax({
        type: "GET",
        url: "chart",
        data: {
            'trim': trim,
            'model': model,
            'make': make,
            'year': year
        },

        dataType: 'text',
        cache: false,

        success: function (dict_list_data) {
            _dict_list_data = JSON.parse(dict_list_data);
            var car_data = _dict_list_data['data'];
            var cars_urls = _dict_list_data['urls'];
            insert_to_table(_dict_list_data['full_data']);
            console.log(car_data);
            console.log(cars_urls);


        google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = new google.visualization.DataTable();
            data.addColumn('number');
            data.addColumn('number');
            data.addColumn( {'type': 'string', 'role': 'style'} );
            data.addRows(car_data);

            var options = {
                aggregationTarget: 'series',
                tooltip: { trigger: 'selection' , isHtml: true},
                legend: 'none',
                  hAxis: {title: 'Kilometres',minValue: 0, maxValue: 150},
                  vAxis: {title: 'Price',minValue: 0, maxValue: 150},
                  chartArea: {width:'50%'},
                  trendlines: {
                    0: {
                      type: 'linear',
                      showR2: true,
                      visibleInLegend: true,
                       color: '#a50b0b'
                    }
              }
            };

            options.trendlines[0].type = 'exponential';
            options.trendlines[0].opacity = 0.7;
            options.colors = ['#0e55c9'];

            var chart = new google.visualization.ScatterChart(document.getElementById('chartExponential'));


            google.visualization.events.addListener(chart, 'select', function() {
                selection = chart.getSelection()[0]['row'];

                console.log(selection);

                car_url = cars_urls[selection];
                console.log(car_url);
                window.open(car_url);
              });

            chart.draw(data, options);
            }
        }
    });

}






