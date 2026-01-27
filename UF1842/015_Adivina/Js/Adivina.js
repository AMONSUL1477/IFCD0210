const objetivo = Math.floor(Math.random() * 100) + 1;
const max_intentos = 10;
let intentos = 1;

function adivinar(e){
    e.preventDefault();
    
    let num;
    let numero = document.getElementById("numero");
    let quedan = document.getElementById("quedan");
    let resultado = document.getElementById("resultado");
    let btn_enviar = document.getElementById("enviar");

    num = parseInt(numero.value);
    console.log(num);

    if(max_intentos - intentos > 0){
        quedan.innerHTML = max_intentos - intentos;
        intentos ++;

        if(num == objetivo){
            resultado.innerHTML = "ENHORABUENA has acertado.";
            btn_enviar.disabled = true;
            numero.disabled = true;
        }
        else if(num < objetivo){
            resultado.innerHTML = `El número ${num} es menor que el objetivo.`;
        }
        else{
            resultado.innerHTML = `El número ${num} es mayor que el objetivo.`;
        }
    }
    else{
        resultado.innerHTML = `TERMINADO. El número era ${objetivo}`;
        btn_enviar.disabled = true;
        numero.disabled = true;
    }
    numero.value = "";
    numero.focus();

}

function reiniciar(){
    window.location.reload();
}