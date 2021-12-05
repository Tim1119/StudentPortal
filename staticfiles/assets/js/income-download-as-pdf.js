$(document).ready(function () {  
    let btn = document.getElementById('download-btn');   
    btn.addEventListener('click', function (e) {
        e.preventDefault()

        var element = document.getElementById('card');
        console.log(user.toString(),'dsw')
        html2pdf(element, {
            margin: 1,
            filename: 'income',
            image: {
                type: 'jpeg',
                quality: 0.98
            },
            html2canvas: {
                scale: 2,
                letterRendering: true
            },
            jsPDF: {
                unit: 'in',
                format: 'a4',
                orientation: 'portrait'
            }
        });
    })
})