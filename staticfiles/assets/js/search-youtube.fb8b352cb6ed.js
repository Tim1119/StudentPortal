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

let searchYoutubeForm = document.getElementById('search-youtube-form');
let searchValueForm = document.getElementById('id_search');
let mainContainer = document.getElementById('main-container');

searchYoutubeForm.addEventListener('submit', function (e) {
    e.preventDefault()
 
  
  
$.ajax({
  type: 'POST',
  url: '/youtube/search-youtube/',
  data: {
    search_text: searchValueForm.value,
    csrfmiddlewaretoken: csrftoken
  },
  success: function (results) {
    mainContainer.innerHTML=''
            for (let i=0; i < results.length; i++){
              resultDiv = `
              <div class="card  col-12 col-lg-12 mt-3" >
              <div class="row g-0">
                <div class="col-md-4 container  search-img-div ">
                  <img src="${results[i].thumbnail}" alt="..." class="img-fluid">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title">${results[i].title}</h5>
                    <p class="card-text" style="font-size: 13px;">${results[i].description}</p>
                    <span>
                        <small class="text-muted">  <i class="bi bi-smartwatch"></i> ${results[i].duration} </small>
                        <small class="text-muted">  <i class="bi bi-youtube"></i> ${results[i].channel} </small>
                        <small class="text-muted">  <i class="bi bi-calendar"></i> ${results[i].published} </small>
                        <small class="text-muted">  <i class="bi bi-eye"></i> ${results[i].views} </small>
                      </span>
                      <p class="mt-2">
                          <span>
                              <a href="${results[i].link}" style="font-size: 15px;">${results[i].link}</a>
                          </span>
                      </p>
                  </div>
                </div>
              </div>
            </div>
      `
      mainContainer.innerHTML+=resultDiv
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


