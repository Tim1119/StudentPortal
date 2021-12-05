$(document).ready(function () {  
    let btn = document.getElementById('download-btn');   
    btn.addEventListener('click', function (e) {
        e.preventDefault()
        var element = document.getElementById('blog');
        html2pdf(element, {
            margin: 1,
            filename: noteDetail + 'note',
            image: {
                type: 'png',
                quality: 1
            },
            html2canvas: {
                scale: 2,
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