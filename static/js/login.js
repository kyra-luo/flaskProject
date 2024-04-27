
// hid or not hid the psw
function HID(){
    var pin=document.querySelector('.PIN0');
    if(pin.type=="password"){
        pin.type='text';
    }else{
        pin.type='password'
    }
}