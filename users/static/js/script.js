const set_user_detail = () => {
    username = document.getElementById('username').value
    password = document.getElementById('password').value

    localStorage.setItem('username', username)
    localStorage.setItem('password', password)
}

if (localStorage.getItem('username')){
    document.getElementById('username').value = localStorage.getItem('username')
    document.getElementById('password').value = localStorage.getItem('password')
    document.getElementsByTagName('input')
    [document.getElementsByTagName('input').length - 1].click()
}