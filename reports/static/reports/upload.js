const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBox = document.getElementById('alert-box')

Dropzone.autoDiscover = false

const handleAlerts = (type, msn) =>{
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msn}
    </div>
    `
}

const myDropzone = new Dropzone('#my-dropzone', {
    url: '/reports/upload/',
    init: function(){
        this.on('sending', (file, xhr, formData)=>{
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            console.log(response)
            const ex = response.ex
            if (ex){
                handleAlerts('danger', 'File already exists.')
             }else{
                handleAlerts('success', 'Your file has been uploaded.')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})