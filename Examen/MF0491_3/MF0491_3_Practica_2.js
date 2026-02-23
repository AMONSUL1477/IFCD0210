function analizarConsumo(consumos) 
{
    let diasConsumoAlto = 0;
    let totalSemana = 0;
    let consumoMinimo = consumos[0];

    for (let i = 0; i < consumos.length; i++) 
        {
            totalSemana += consumos[i];

            if (consumos[i] > 30) 
                {
                    diasConsumoAlto++;
                }

            if (consumos[i] < consumoMinimo) 
                {
                    consumoMinimo = consumos[i];
                }
        }

    return [diasConsumoAlto, totalSemana, consumoMinimo];
}

const consumos = [28, 35, 22, 40, 31, 18, 25];
console.log(analizarConsumo(consumos)); 
