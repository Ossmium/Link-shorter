function load_users_urls(userId) {
    const userItem = document.getElementById('list-group_' + userId);
    const userIdatt = userItem.getAttribute('data-user-id');
    console.log(userIdatt)
    const linksList = document.getElementById('links-' + userIdatt);

    if (linksList.classList.contains('show')) {
        linksList.classList.remove('show');
    } else if (linksList.childElementCount > 0) {
        linksList.classList.add('show');
    } else {
        fetch(`/users/${userId}/links/`)
            .then(response => response.json())
            .then(data => {
                let counter = 1;
                data.links.forEach(link => {
                    const linkRow = document.createElement('tr');
                    linkRow.id = (`link-${counter}`)

                    const urlTd = document.createElement('td');
                    const urlAnchor = document.createElement('a');
                    urlAnchor.href = link.full_url;  // Предполагается, что структура данных имеет поле link.url
                    urlAnchor.textContent = link.full_url;
                    urlTd.appendChild(urlAnchor);

                    const shortUrlTd = document.createElement('td');
                    const shortUrlAnchor = document.createElement('a');
                    shortUrlAnchor.href = `/urls/${link.short_url}/`;
                    shortUrlAnchor.textContent = link.short_url;
                    shortUrlTd.appendChild(shortUrlAnchor);

                    const deleteTd = document.createElement('td');
                    const deleteButton = document.createElement('input');
                    deleteButton.type = 'submit';
                    deleteButton.classList.add('btn', 'btn-sm', 'btn-outline-danger');
                    deleteButton.value = 'Удалить';
                    deleteButton.id = `delete_url${link.id}`;
                    deleteButton.dataset.url = `/urls/delete/` + link.id + "/";
                    deleteButton.onclick = function() {
                        delete_user_url(link.id, linkRow.id);
                    };
                    deleteTd.appendChild(deleteButton);

                    linkRow.appendChild(urlTd);
                    linkRow.appendChild(shortUrlTd);
                    linkRow.appendChild(deleteTd);

                    linksList.appendChild(linkRow);
                    counter += 1;

                    // const linkItem = document.createElement('a');
                    // linkItem.href = `/urls/${link.short_url}/`;
                    // linkItem.textContent = link.short_url;
                    // linkItem.classList.add('list-group-item');
                    // linksList.appendChild(linkItem);
                });
                linksList.classList.add('show');
            });
    }
}