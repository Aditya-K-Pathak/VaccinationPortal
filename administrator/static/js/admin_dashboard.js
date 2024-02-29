const Edit = (button) =>{
    var logs = button.closest('.hospital-detail').innerText.split('\n')
    localStorage.setItem('center_code', logs[0].slice(13))
    localStorage.setItem('hospital_name', logs[1])
    localStorage.setItem('city_name', logs[2])
    localStorage.setItem('vaccine_name', logs[3].slice(14))
    localStorage.setItem('doses', logs[4].slice(17))
    localStorage.setItem('opening', logs[5].slice(8, 16))
    localStorage.setItem('closing', logs[5].slice(18, 26))
}

const logout = () => {
    localStorage.clear()
}

const Delete = (button) =>{
    var logs = button.closest('.hospital-detail').innerText.split('\n')
    document.getElementById('id_code').value = logs[0].slice(13);
    console.log(document.getElementById('id_code').value)
    document.getElementsByTagName('input')[2].click()
}