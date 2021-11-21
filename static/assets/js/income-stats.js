function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Generate Chart for Data 
var myChart = null // Initialise Chart for plotting
function renderChart(data, labels) {
    const ctx = document.getElementById('Chart').getContext('2d');
     myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Expenses for last six months',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                  beginAtZero: false
                }
              }
           
        }
    });
}
noData = document.getElementById('no-data-to-chart')
chartView = document.getElementById('chartView') // display chart from data if user has created categories
chartViewBtn = document.getElementById('chartView-btn') // button display chart from data if user has created categories
// Generate Line Chart for User from six month data
function getChartData(){
    fetch('/income/income-summary-json/',{
        headers: {
            'X-CSRFToken': csrftoken,
        },
        method:'POST'
    })
    .then((res) => res.json())
    .then((results) => {
        if (Object.keys(results.income_source_data).length > 0){
            noData.classList.add('d-none')
            chartView.classList.remove('d-none')
            chartViewBtn.classList.remove('d-none')
            const category_data = results.income_source_data
        const[labels,data] = [
            Object.keys(category_data),
            Object.values(category_data)
        ]
        renderChart(data,labels)
        }
        else{
            noData.classList.remove('d-none')
            chartView.classList.add('d-none')
            chartViewBtn.classList.add('d-none')
        }
       
    })
}

// This helps to search the user by a specific date 
specificResult = document.getElementById('search-specific-date-result')
specificDate = document.getElementById('search-by-specific-date');
searchByDateForm = document.getElementById('specific-date-form-search');
searchByDateForm.addEventListener('submit',function(e){
    e.preventDefault()
    specificResult.innerHTML = ''
    specificRangeResult.classList.add(['d-none'])
    specificResult.classList.add('d-none')
    fetch('/income/search-by-date/',{
        body:JSON.stringify({date:specificDate.value}),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            method:'POST'
        })
    .then((res) => res.json())
    .then((results) => {
        if (Object.keys(results.income_source_data).length > 0){
            const income_data = results.income_source_data
        const[labels,data] = [
            Object.keys(income_data),
            Object.values(income_data)
        ]
        myChart.destroy()
        renderChart(data,labels)
       myChart.data.datasets.label = 'Expense for today'
        specificResult.classList.add(['alert-success'])
           specificResult.classList.remove(['d-none'])
           specificResult.classList.remove(['alert-danger'])
           specificResult.innerHTML =   `sorry, chart for ${specificDate.value} has been generated below`

        }else{
           specificResult.classList.add(['alert-danger'])
           specificResult.classList.remove(['d-none'])
           specificResult.innerHTML =   `sorry, no expense was incured on ${specificDate.value}`
        }
        
    })

})

// this helps to search the date within a specific range of dates
specificRangeResult = document.getElementById('search-specific-date-range-result');
specificDateRange = document.getElementById('search-by-date-range');
searchByDateRangeForm = document.getElementById('date-range-form-search');
searchByDateRangeForm.addEventListener('submit',function(e){
    e.preventDefault()
    specificRangeResult.innerHTML =''
    specificResult.classList.add('d-none')
    fetch('/income/search-within-date/',{
        body:JSON.stringify({date:specificDateRange.value}),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            method:'POST'
        })
    .then((res) => res.json())
    .then((results) => {
        console.log()
        if (Object.keys(results.income_source_data).length > 0){
            specificRangeResult.classList.add(['alert-success'])
               specificRangeResult.classList.remove(['d-none'])
               specificRangeResult.innerHTML =   `chart from ${specificDateRange.value}  to today has been generated below`
            const income_data = results.income_source_data
        const[labels,data] = [
            Object.keys(income_data),
            Object.values(income_data)
        ]
        myChart.destroy()
        renderChart(data,labels)
        }else{
           specificRangeResult.classList.add(['alert-danger'])
           specificRangeResult.classList.remove(['d-none'])
           specificRangeResult.innerHTML =   `sorry, no expense since ${specificDate.value} to today has been incurred`
        }
        
    })

})
document.onload = getChartData() 


// Change the kind of chart displayed to user`
const chartTitle = document.getElementById('card-title')
const barChart = document.getElementById('barChart')
const lineChart = document.getElementById('lineChart')
const pieChart = document.getElementById('pieChart')
const doughnutChart = document.getElementById('doughnutChart') 

barChart.addEventListener('click',changebar)
lineChart.addEventListener('click',changeline)
pieChart.addEventListener('click',changepie)
doughnutChart.addEventListener('click',changedoughnut)

function changebar(){
    chartTitle.innerHTML = 'Bar Chart showing Income by Sources'
  myChart.config.type = 'bar'
  myChart.update()
}
function changeline(){
    chartTitle.innerHTML = 'Line Chart showing Income by Sources'
    myChart.config.type = 'line'
    myChart.update()
}
function changepie(){
    chartTitle.innerHTML = 'Pie Chart showing Income by Sources'
    myChart.config.type = 'pie'
    myChart.update()
}
function changedoughnut(){
    chartTitle.innerHTML = 'Doughnut Chart showing Income by Sources'
    myChart.config.type = 'doughnut'
    myChart.update()
}


$(document).ready(function () {  
    let btn = document.getElementById('download-btn');   
    btn.addEventListener('click', function (e) {
        e.preventDefault()
       

        var element = document.getElementById('card');
        html2pdf(element, {
            margin: 1,
            filename: 'income',
            image: {
                type: 'png',
                quality: 1
            },
            html2canvas: {
                scale: 1,
                letterRendering: true
            },
            jsPDF: {
                unit: 'in',
                format: 'letter',
                orientation: 'portrait'
            }
        });
    })
})