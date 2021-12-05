const searchField = document.getElementById('searchField');
const searchNotFound = document.getElementById('search-not-found');
const appTable = document.getElementById('app-table');
const pagination = document.getElementById('pagination');
const tableBody = document.getElementById('table-body');
const suggestedSearch = document.getElementById('random-search');
const tableOutput = document.getElementById('table-ouput');
// CSRF TOKEN 
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







const searchFunction = function(e){
    const searchValue = e.target.value 
    
    if (searchValue.trim().length > 0){
        tableBody.innerHTML = ''
        fetch('/income/search-income/',{
            body:JSON.stringify({searchText:searchValue}),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            method:'POST'
        })
        .then((res) => res.json())
        .then((data) => {
            appTable.classList.add('d-none')
            searchNotFound.classList.remove('d-none')
            searchNotFound.classList.add('block')       
               if (data.length==0){
                   tableOutput.classList.add('d-none')
                   pagination.classList.add('d-none')
                   // searchNotFound.innerHTML = `<p class=mt-5>'No result found'</p>`
               }else{
                   searchNotFound.classList.add('d-none')
                   tableOutput.classList.remove('d-none')
                   suggestedSearch.innerHTML =` <p>Result matching ${searchValue} sources</p>`
                   data.forEach((item) => {
                         
                    tableBody.innerHTML += `
                        <tr>
                            <td>${item.description}</td>
                            <td>${item.amount}</td>
                            <td>${item.income_date}</td>
                        </tr>
                        `
                   });
                   
               }
              
        })
    }else{
        appTable.classList.remove('d-none')
            tableOutput.classList.add('d-none')
            pagination.classList.remove('d-none')
           
    }
}

searchField.addEventListener('keyup',searchFunction)