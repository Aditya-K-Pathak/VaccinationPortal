document.getElementsByTagName('title')[0].innerHTML = localStorage.getItem('center_code')
document.getElementById('centercode').value = localStorage.getItem('center_code')
document.getElementById('centername').value = localStorage.getItem('hospital_name')
document.getElementById('centerlocation').value = localStorage.getItem('city_name')
document.getElementById('vaccinename').value = localStorage.getItem('vaccine_name')
document.getElementById('dosecount').value = localStorage.getItem('doses')
document.getElementById('openingtime').value = localStorage.getItem('opening')
document.getElementById('closingtime').value = localStorage.getItem('closing')
