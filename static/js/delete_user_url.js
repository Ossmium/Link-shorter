function delete_user_url(urlId, linkRowId) {
    const delete_url_button = document.getElementById('delete_url' + urlId);
    const linkItem = document.getElementById(linkRowId);

    if (!delete_url_button || !linkItem) {
        console.error('Элементы delete_url_button или linkItem не найдены');
        return;
    }

    $.ajax({
        url: delete_url_button.dataset.url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrfToken,
        },
        success: function (response) {
            linkItem.remove();
        },
        error: function (xhr, status, error) {
            console.error('Ошибка при удалении ссылки. Статус:', status, 'Ошибка:', error);
        }
    });
}