function collectData(){
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value
    let confirmPassword = document.getElementById('confirm-password').value
    let email = document.getElementById('email').value
    let confirmEmail = document.getElementById('confirm-email').value
    
    let data = {'username':username, 'password': password, 'confirm Email': confirmEmail, 'confirm password':confirmPassword, 'email': email}

    for (let key in data){
        if (data[key]==''){
            alert('please fill the form completely, you miss '+key)
            return
        }
    }

    if (password != confirmPassword) {
        alert('Your password didn\'t match')
    } else if (email != confirmEmail){
        alert ('Your email didnt match')
    } else {
        nl='\n'
        alert ('Login success!'+nl+nl+'Username: '+username+nl+'Password: '+password+nl+'Email: '+email)
    }
}