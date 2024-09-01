function delete_url(urlId) {
    const delete_url_button = document.getElementById('delete_url' + urlId);
    console.log(delete_url_button.dataset.url)
    $.ajax({
        url: delete_url_button.dataset.url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrfToken,
        },

        success: async function (response) {
            console.log(delete_url_button);
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
}