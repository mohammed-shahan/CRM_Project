function checkForBlank(val, msg){
    if(document.getElementById(val).value == ''){
        alert(msg);
    }
    return;
}


function validate() {
    checkForBlank('username','Enter Username');
    checkForBlank('password','Enter Password');
}