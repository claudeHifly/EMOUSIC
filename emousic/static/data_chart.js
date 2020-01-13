'use strict';

window.chartColors = {
    colPleasantness: 'rgb(0, 123, 255)',
    colAttention: 'rgb(40, 167, 69)',
    colSensitivity: 'rgb(23, 162, 184)',
    colAptitude: 'rgb(255, 193, 7)',
    colPolarityValue: 'rgb(220, 53, 69)'
};

(function (global) {
// Google Analytics
    /* eslint-disable */
    if (document.location.hostname.match(/^(www\.)?chartjs\.org$/)) {
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r;
            i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date();
            a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
            a.async = 1;
            a.src = g;
            m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
        ga('create', 'UA-28909194-3', 'auto');
        ga('send', 'pageview');
    }
    /* eslint-enable */

}(this));


var labels_chart = new Array();
var Pleasantness_data = new Array();
var Attention_data = new Array();
var Sensitivity_data = new Array();
var Aptitude_data = new Array();
var Polarity_value_data = new Array();
for (var i = 0; i < measure_data.length; i++) {
    labels_chart.push(measure_data[i].fields.number);
    Pleasantness_data.push(measure_data[i].fields.pleasantness);
    Attention_data.push(measure_data[i].fields.attention);
    Sensitivity_data.push(measure_data[i].fields.sensitivity);
    Aptitude_data.push(measure_data[i].fields.aptitude);
    Polarity_value_data.push(measure_data[i].fields.polarity_value);
}

function update_graph(graph, labels_chart, database_data, title, color) {
    graph.data.datasets.splice(0, 1);
    window.myLine.update();
    var newDatasets = {
        label: title,
        backgroundColor: color,
        borderColor: color,
        data: database_data,
        fill: false,
    };
    config.data.datasets.push(newDatasets);
    config.options.title.text = title + ' Chart';
    config.data.labels = labels_chart
    window.myLine.update();
}

var config = {
    type: 'line',
    data: {
        labels: labels_chart,
        datasets: [{
            label: 'Pleasantness',
            backgroundColor: window.chartColors.colPleasantness,
            borderColor: window.chartColors.colPleasantness,
            data: Pleasantness_data,
            fill: false,
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Pleasantness Chart'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Measures'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Level'
                }
            }]
        }
    }
};

window.onload = function () {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
};

document.getElementById('Pleasantness').addEventListener('click', function () {
    update_graph(config, labels_chart, Pleasantness_data, "Pleasantness", window.chartColors.colPleasantness);
});

document.getElementById('Attention').addEventListener('click', function () {
    update_graph(config, labels_chart, Attention_data, "Attention", window.chartColors.colAttention);
});

document.getElementById('Sensitivity').addEventListener('click', function () {
    update_graph(config, labels_chart, Sensitivity_data, "Sensitivity", window.chartColors.colSensitivity);
});

document.getElementById('Aptitude').addEventListener('click', function () {
    update_graph(config, labels_chart, Aptitude_data, "Aptitude", window.chartColors.colAptitude);
});

document.getElementById('Polarity_value').addEventListener('click', function () {
    update_graph(config, labels_chart, Polarity_value_data, "Polarity Value", window.chartColors.colPolarityValue);
});


$('#slider-range').on('slidestop', function () {
    labels_chart = new Array();
    Pleasantness_data = new Array();
    Attention_data = new Array();
    Sensitivity_data = new Array();
    Aptitude_data = new Array();
    Polarity_value_data = new Array();
    for (var i = $("#slider-range").slider("values", 0) - 1; i < $("#slider-range").slider("values", 1); i++) {
        labels_chart.push(measure_data[i].fields.number);
        Pleasantness_data.push(measure_data[i].fields.pleasantness);
        Attention_data.push(measure_data[i].fields.attention);
        Sensitivity_data.push(measure_data[i].fields.sensitivity);
        Aptitude_data.push(measure_data[i].fields.aptitude);
        Polarity_value_data.push(measure_data[i].fields.polarity_value);
    }
    //config.data.labels = labels_chart;
    if (config.data['datasets'][0]['label'] == 'Pleasantness') {
        update_graph(config, labels_chart, Pleasantness_data, "Pleasantness", window.chartColors.colPleasantness);
    } else if (config.data['datasets'][0]['label'] == 'Attention') {
        update_graph(config, labels_chart, Attention_data, "Attention", window.chartColors.colAttention);
    } else if (config.data['datasets'][0]['label'] == 'Sensitivity') {
        update_graph(config, labels_chart, Sensitivity_data, "Sensitivity", window.chartColors.colSensitivity);
    } else if (config.data['datasets'][0]['label'] == 'Aptitude') {
        update_graph(config, labels_chart, Aptitude_data, "Aptitude", window.chartColors.colAptitude);
    } else {
        update_graph(config, labels_chart, Polarity_value_data, "Polarity Value", window.chartColors.colPolarityValue);
    }

});




