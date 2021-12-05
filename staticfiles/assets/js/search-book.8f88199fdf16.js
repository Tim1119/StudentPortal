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



// This helps to search the user by a specific date 

let searchBookForm = document.getElementById('search-book-form');
let searchValueForm = document.getElementById('id_search');
let mainContainer = document.getElementById('main-container');

searchBookForm.addEventListener('submit', function (e) {
    e.preventDefault()
 


    fetch('/books/search-book/', {
            body: JSON.stringify({
                
                search_text: searchValueForm.value
            }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            method: 'POST'
        })
        .then((res) => res.json())
        .then((results) => {
          
          console.log(results)
          mainContainer.innerHTML=''
            for (let i=0; i < results.length; i++){
              
              resultDiv = `
              <div class="card  col-12 col-lg-12 mt-3" >
              <div class="row g-0">
                <div class="col-md-4 container search-img-div ">
                  <img src="${results[i].thumbnail}" alt="..." class="img-fluid">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title">${results[i].title}</h5>
                    <p class="card-text" style="font-size: 13px;">${results[i].description}</p>
                      <p class="mt-2">
                          <span>
                              <a href="${results[i].preview}" style="font-size: 15px;">${results[i].preview}</a>
                          </span>
                      </p>
                  </div>
                </div>
              </div>
            </div>
      `
      mainContainer.innerHTML+=resultDiv
            }
         
           
        })
        

})