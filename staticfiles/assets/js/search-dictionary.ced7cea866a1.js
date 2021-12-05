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

let searchDictionaryForm = document.getElementById('search-dictionary-form');
let searchValueForm = document.getElementById('id_search');
let mainContainer = document.getElementById('main-container');

searchDictionaryForm.addEventListener('submit', function (e) {
  e.preventDefault()



  $.ajax({
    type: 'POST',
    url: '/dictionary/search-dictionary/',
    data: {
      search_text: searchValueForm.value,
      csrfmiddlewaretoken: csrftoken
    },
    success: function (results) {
      mainContainer.innerHTML = ''
         
   
            resultDiv = `
                <div class="card col-md-10 mt-5">
                    <div class="card-body">
            <h5 class="card-title">${searchValueForm.value}</h5>
            <p><small>/${results.phonetics}/</small></p>
            <p>
            <span>
            <i class="bi bi-volume-up-fill" onclick="document.getElementById('player').play()"></i> 
            <audio id=player src="${results.audio}"></audio></span>
            </p>
            <p class="card-text"><b>${results.definition}</b></p>
            <div>
            <p><b>synonyms:</b> ${results.synonyms}</p>
            </div>
          </div>
        </div>
        `
            mainContainer.innerHTML = resultDiv
    },
  
      
    error: function (data) {
      let resultDiv = `
      <div class="alert alert-danger col-md-10" role="alert">
           Word not found or bad internet connection
      </div>`
      mainContainer.innerHTML = resultDiv
    }
  });
  
})



  