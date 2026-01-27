let manejador;



function mostrarFecha()
{
    let fecha = new Date();
    let hora = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();

    let diasem = fecha.getDay();
    let diames = fecha.getDate();
    let mes = fecha.getMonth() + 1;

    let tem = fecha.get
    



    let spanHora = document.getElementById("horas");
    let spanMinutos = document.getElementById("minutos");
    let spanSegundos = document.getElementById("segundos");
  
    let spanDiaSem = document.getElementById("diasem");
    let spanDiames = document.getElementById("diames");
    let spanMes = document.getElementById("mes");


    spanHora.innerHTML = hora.toString().padStart(2,'0');
    spanMinutos.innerHTML = String(minutos).padStart(2,'0');
    spanSegundos.innerHTML = segundos.toString().padStart(2,'0');

    
    spanDiaSem.innerHTML = diaSemana(diasem);
    spanDiames.innerHTML = diames.toString().padStart(2,'0');
    spanMes.innerHTML = mes.toString().padStart(2,'0');
}

function iniciar()
{
    mostrarFecha();
    manejador = setInterval(mostrarFecha,1000);
}

function parar()
{
    clearInterval(manejador);

}

function diaSemana(numDia)
{
    let semana = ['Domingo', 'Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes', 'Sabado'];


    return semana [numDia];


}



