//lineChart
$(function (){
  $('#lineChart').highcharts({
    title: {
      text: 'world largest income',
      x: -20 //center
    },
    subtitle: {
      text: 'Source: database',
      x: -20
    },
    xAxis: {
      categories:['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    yAxis: {
      title: {
        text: 'Mount(millions)'
      },
      plotLines: [{
        value: 0,
        width: 1,
        color: '#808080'
      }]
    },
    tooltip: {
      valueSuffix: '$'
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
    },
    series: [{
        'name': 'Tokyo',
        'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
      }, {
        'name': 'New York',
        'data': [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
      }, {
       'name': 'Berlin',
        'data': [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
      }, {
        'name': 'London',
        'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
      }],
  })
});
function getTestCasesCountDatSource(category,seriesList) {
  $('#casesCountlineChart').highcharts({
    title: {
      text: 'Test Cases Total Trend Report #BuildNo',
      x: -20 //center
    },
    subtitle: {
      text: 'Source: Jenkins',
      x: -20
    },
    xAxis: {
      categories:category
    },
    yAxis: {
      title: {
        text: 'Mount()'
      },
      plotLines: [{
        value: 0,
        width: 1,
        color: '#808080'
      }]
    },
    tooltip: {
      valueSuffix: ''
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
    },
    series:seriesList 
  })
};

function getTestResponseTimeDatSource(category,seriesList) {
	  $('#timelineChart').highcharts({
	    title: {
	      text: 'Test\'s Response Time Trend Report #BuildNo',
	      x: -20 //center
	    },
	    subtitle: {
	      text: 'Source: Jenkins',
	      x: -20
	    },
	    xAxis: {
	      categories:category
	    },
	    yAxis: {
	      title: {
	        text: 'Time(ms)'
	      },
	      plotLines: [{
	        value: 0,
	        width: 1,
	        color: '#808080'
	      }]
	    },
	    tooltip: {
	      valueSuffix: 'ms'
	    },
	    legend: {
	      layout: 'vertical',
	      align: 'right',
	      verticalAlign: 'middle',
	      borderWidth: 0
	    },
	    series: seriesList
	  })
	};
	
function getSuccessRateDatSource(category,seriesList) {
		  $('#ratelineChart').highcharts({
		    title: {
		      text: 'Test\'s Run SuccessRate Time Trend Report #BuildNo',
		      x: -20 //center
		    },
		    subtitle: {
		      text: 'Source: Jenkins',
		      x: -20
		    },
		    xAxis: {
		      categories:category
		    },
		    yAxis: {
		      title: {
		        text: 'SuccessRate(%)'
		      },
		      plotLines: [{
		        value: 0,
		        width: 1,
		        color: '#808080'
		      }]
		    },
		    tooltip: {
		      valueSuffix: '%'
		    },
		    legend: {
		      layout: 'vertical',
		      align: 'right',
		      verticalAlign: 'middle',
		      borderWidth: 0
		    },
		    series: seriesList
		  })
		};
		
		
//barchart
function getSuccessRateBuildNoDatSource(seriesList) {
		    $('#successRatebarChart').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'TestCases\'s Success Rate Trend Report #BuildNo'
		        },
		        subtitle: {
		            text: 'Source: <a href="http://ciapi.qa.nt.ctripcorp.com:8080/job">Jenkins Histrory</a>'
		        },
		        xAxis: {
		            type: 'category',
		            labels: {
		                rotation: -45,
		                style: {
		                    fontSize: '13px',
		                    fontFamily: 'Verdana, sans-serif'
		                }
		            }
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Rate (%)'
		            }
		        },
		        legend: {
		            enabled: false
		        },
		        tooltip: {
		            pointFormat: 'SuccessRate: <b>{point.y:.1f} %</b>'
		        },
		        series: [{
		            name: 'Rate',
		            data: seriesList,
		            dataLabels: {
		                enabled: true,
		                rotation: -90,
		                color: '#FFFFFF',
		                align: 'right',
		                format: '{point.y:.1f}', // one decimal
		                y: 10, // 10 pixels down from the top
		                style: {
		                    fontSize: '13px',
		                    fontFamily: 'Verdana, sans-serif'
		                }
		            }
		        }]
		    });
		};
$(function () {
    $('#barChart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'World\'s largest cities per 2014'
        },
        subtitle: {
            text: 'Source: <a href="http://en.wikipedia.org/wiki/List_of_cities_proper_by_population">Wikipedia</a>'
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Population (millions)'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Population in 2008: <b>{point.y:.1f} millions</b>'
        },
        series: [{
            name: 'Population',
            data: [
                ['Shanghai', 23.7],
                ['Lagos', 16.1],
                ['Instanbul', 14.2],
                ['Karachi', 14.0],
                ['Mumbai', 12.5],
                ['Moscow', 12.1],
                ['São Paulo', 11.8],
                ['Beijing', 11.7],
                ['Guangzhou', 11.1],
                ['Delhi', 11.1],
                ['Shenzhen', 10.5],
                ['Seoul', 10.4],
                ['Jakarta', 10.0],
                ['Kinshasa', 9.3],
                ['Tianjin', 9.3],
                ['Tokyo', 9.0],
                ['Cairo', 8.9],
                ['Dhaka', 8.9],
                ['Mexico City', 8.9],
                ['Lima', 8.9]
            ],
            dataLabels: {
                enabled: true,
                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y:.1f}', // one decimal
                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
});
