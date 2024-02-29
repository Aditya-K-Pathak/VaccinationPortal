var vaccination_status = document.getElementById('name').innerText
vaccination_status = vaccination_status.split(' | ')
if (vaccination_status[1] == 'False'){
    vaccination_status[1] = 'Not Yet Vaccinated!'

    const state = vaccination_status[0] + ' | ' + vaccination_status[1];
    document.getElementById('name').innerText = state
    document.getElementById('name').style.color = 'red';
}
else{
    vaccination_status[1] = 'Vaccinated!'

    const state = vaccination_status[0] + ' | ' + vaccination_status[1];
    document.getElementById('name').innerText = state
    document.getElementById('name').style.color = 'green';
}

const fill_form = (username, password, vaccine, code, date) =>{
    document.getElementById('id_username').value = username;
    document.getElementById('id_password').value = password;
    document.getElementById('id_vaccine').value = vaccine;
    document.getElementById('id_date').value = date
    document.getElementById('id_code').value = code

}

const book_slot = (button) =>{
    const data = button.closest('.detail').innerText.split('\n')[0]
    const vaccine = button.closest('.detail').innerText.split('\n')[4]
    const date = button.closest('.date').innerText.slice(0, 11)
    fill_form(
        localStorage.getItem('username'), 
        localStorage.getItem('password'),
        vaccine, data, date
    )
    document.getElementsByTagName('input')[
        document.getElementsByTagName('input').length - 1
    ].click()
}
