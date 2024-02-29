const cache = () => {
    localStorage.setItem('admin_username', document.getElementById('username').value)
    localStorage.setItem('admin_password', document.getElementById('password').value)
}


if (localStorage.getItem('admin_username')){
    document.getElementById('username').value = localStorage.getItem('admin_username')
    document.getElementById('password').value = localStorage.getItem('admin_password')
    document.getElementById('submit').click()
}