function checkForBlank(val, msg){
    if(document.getElementById(val).value == ''){
        alert(msg);
    }
    return;
}

function checkPhno(){
    var phnum = document.getElementById('phnumber').value;
    if(phnum.length != 10){
        alert('Please enter 10 digits for phone number')
    }
    else{
        document.getElementById('phno_error').innerText = '';
    }
}


function validate() {
    checkForBlank('fullname','Enter Full Name');
    checkForBlank('emailid','Enter your Email address');
    checkForBlank('phnumber','Enter Phone Number');
    checkForBlank('username','Enter Username');
    checkForBlank('password','Enter Password');
    checkForBlank('confpassword','Confirm your password');
    checkPhno();
}