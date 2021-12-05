
$(document).on('submit','#userSettingsForm',function(event){
    event.preventDefault();

    $.ajax({
      type:'POST',
      url:'save_settings/',
      data:{ "currency": $('#inputGroupSelect').val(), csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success: function(data){
        console.log(data.message)
        console.log(data['message'])
        alert_div = document.getElementById('alert-user-changes')
        currency_val = $('#inputGroupSelect').val()
        alert_div.innerHTML= data.message + `. currency is now set as ${currency_val}`
        alert_div.classList.remove('d-none')

      },
      error: function(data){
          console.log(data)
      }
    });
  });