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

let searchYoutubeForm = document.getElementById('search-wikipedia-form');
let searchValueForm = document.getElementById('id_search');
let mainContainer = document.getElementById('main-container');

searchYoutubeForm.addEventListener('submit', function (e) {
  e.preventDefault()

  
$.ajax({
  type: 'POST',
  url: '/wikipedia/search-wikipedia/',
  data: {
    search_text: searchValueForm.value,
    csrfmiddlewaretoken: csrftoken
  },
  success: function (results) {
    if (results) {

      for (let i = 0; i < results.length; i++) {
        resultDiv = `
            
            <div class="card col-md-10 mt-5">
                <div class="card-body">
        <h5 class="card-title">${results[i].title}</h5>
        <a href="${results[i].link}">${results[i].link}</a>
        <p class="text-justify">
        ${results[i].summary}
        </p>
       
      </div>
    </div>`
        mainContainer.innerHTML += resultDiv
      }

    }

  },
  error: function (data) {
    let resultDiv = `
    <div class="alert alert-danger col-md-10" role="alert">
         Page not found or bad internet connection
    </div>`
    mainContainer.innerHTML = resultDiv
  }
});




})
