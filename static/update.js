

function num() {
    let name = document.getElementById("name").value;
    let tel = document.getElementById("tel").value;
    console.log(name, tel);
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name': name,
                             'phone': tel})
    });
};

function Clear() {
    fetch('/clear', {
        method: 'get'
    });
    location.reload()
};
