$(document).ready(function () {
    $('#urlCreate').submit(function () {
        const create_url_button = document.getElementById('create_url');
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: create_url_button.dataset.url,

            success: async function (response) {
                let html = await (await fetch(location.href)).text();
                let newdoc = new DOMParser().parseFromString(html, 'text/html');
                document.getElementById('urls').outerHTML = newdoc.querySelector('#urls').outerHTML;
                document.getElementById('id_full_url').value = '';
            },
            error: function (response) {
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})