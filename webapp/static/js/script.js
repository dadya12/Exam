async function makeRequest(url, method = "GET", data = null) {
    let options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };
    if (data) {
        options.body = JSON.stringify(data);
    }
    let response = await fetch(url, options);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(await response.text());
        console.log(error);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let a = event.target.closest('a');
    let url = a.getAttribute('href');
    try {
        let response = await makeRequest(url, 'POST');
        let span = document.getElementById(a.getAttribute('data-span-count-id'));
        span.innerText = `${response.count} favorites`;
        if (response.favorite) {
            a.textContent = 'Удалить из избранного';
        } else {
            a.textContent = 'Добавить в избранное';
        }
    } catch (err) {
        console.error('Error:', err);
    }
}

function onLoad() {
    let links = document.querySelectorAll('a.btn.favorite-button');
    links.forEach(link => {
        link.addEventListener('click', onClick);
    });
}