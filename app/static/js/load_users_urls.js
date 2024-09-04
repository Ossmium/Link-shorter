async function load_users_urls(userId) {
    const URL = 'http://localhost:8000/urls/'
    const linksList = document.getElementById('links-' + userId).querySelector('tbody');

    const tableContainer = document.getElementById('links-' + userId);
    let linksLength;

    if (tableContainer.classList.contains('show')) {
        tableContainer.classList.remove('show');
    } else if (linksList.childElementCount > 0) {
        tableContainer.classList.add('show');
    } else {
        let flag = false
        await fetch(`/users/${userId}/links/`)
            .then(response => response.json())
            .then(data => {
                linksLength = data.links.length
                if (!linksLength) {
                    return
                }
                let counter = 1;
                data.links.forEach(link => {
                    const linkRow = document.createElement('tr');
                    linkRow.id = (`link-${counter}`)

                    const urlTd = document.createElement('td');
                    const urlAnchor = document.createElement('a');
                    urlAnchor.href = link.full_url;
                    urlAnchor.textContent = link.full_url;
                    urlTd.appendChild(urlAnchor);

                    const shortUrlTd = document.createElement('td');
                    const shortUrlAnchor = document.createElement('a');
                    shortUrlAnchor.href = `/urls/${link.short_url}/`;
                    shortUrlAnchor.textContent = URL + link.short_url;
                    shortUrlTd.appendChild(shortUrlAnchor);
                    
                    const clickCount = document.createElement('td');
                    const clickCountSpan = document.createElement('span');
                    clickCountSpan.textContent = link.click_count;
                    clickCount.appendChild(clickCountSpan);

                    const createdAt = document.createElement('td');
                    const createdAtSpan = document.createElement('span');
                    createdAtSpan.textContent = link.created_at;
                    createdAt.appendChild(createdAtSpan);

                    const deleteTd = document.createElement('td');
                    const deleteButton = document.createElement('input');
                    deleteButton.type = 'submit';
                    deleteButton.classList.add('btn', 'btn-sm', 'btn-outline-danger');
                    deleteButton.value = 'Удалить';
                    deleteButton.id = `delete_url${link.id}`;
                    deleteButton.dataset.url = `/urls/delete/` + link.id + "/";
                    deleteButton.onclick = function() {
                        delete_user_url(link.id, linkRow.id, userId, linksLength);
                        linksLength -= 1
                    };
                    deleteTd.appendChild(deleteButton);

                    linkRow.appendChild(urlTd);
                    linkRow.appendChild(shortUrlTd);
                    linkRow.appendChild(clickCount);
                    linkRow.appendChild(createdAt)
                    linkRow.appendChild(deleteTd);

                    linksList.appendChild(linkRow);
                    counter += 1;
                    flag = true
                });
                tableContainer.classList.add('show');
            });
    }
}