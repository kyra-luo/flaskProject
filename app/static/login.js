//tell user the input Pin is too long or too short
function myfunction(){
    const mess=document.getElementsByClassName('message')[0];
    const input1=document.querySelector('.PIN1');
    if(input1.value.length<6){
      mess.innerHTML='Password should between 6 and 20';
      mess.style.color='blue';
    }else if(input1.value.length>20){
        mess.innerHTML='Password is too long, make sure no more than 20 digit';
        mess.style.color='darkgoldenrod';
    }else{
        mess.innerHTML='Good Password';
        mess.style.color='black';
    }
}
// hid or not hid the psw

function Hid(className) {
    const pins = document.querySelectorAll('.' + className);
    console.log("test test")
    pins.forEach((pin) => {
        if (pin.type === "password") {
            pin.type = 'text';
        } else {
            pin.type = 'password';
        }
    });
}

function checkpin() {
    var state = false;
    var mess = document.getElementsByClassName('message1')[0];
    var PIN1 = document.querySelector('.PIN1');
    var PIN2 = document.querySelector('.PIN2');
    if (PIN1.value !== PIN2.value) {
        mess.innerHTML = 'Two times password is not same';
        mess.style.color = 'red';
    } else if (PIN1.value === PIN2.value) {
        mess.innerHTML = 'The two password are same';
        mess.style.color = 'blue';
    }
}