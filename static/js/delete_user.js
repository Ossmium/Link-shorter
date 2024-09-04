function delete_user(userId) {
    const delete_user_button = document.getElementById('delete_user_' + userId);
    console.log(delete_user_button.dataset.url)
    $.ajax({
        url: delete_user_button.dataset.url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrfToken,
        },

        success: async function (response) {
            let html = await (await fetch(location.href)).text();
            let newdoc = new DOMParser().parseFromString(html, 'text/html');
            document.getElementById('usersList').outerHTML = newdoc.querySelector('#usersList').outerHTML;
        },
        error: function (response) {
            alert(response.responseJSON.errors);
            console.log(response.responseJSON.errors)
        }
    });
}