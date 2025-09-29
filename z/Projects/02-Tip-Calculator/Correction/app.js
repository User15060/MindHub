const btnEl = document.getElementById("btn");
const billEl = document.getElementById("bill");
const tipEl = document.getElementById("tip");
const result = document.getElementById("result");


function CalculatorTip()
{
    let billAmmount = parseFloat(billEl.value);
    let tipAmmount = parseFloat(tipEl.value);

    if (isNaN(billAmmount) || isNaN(tipAmmount)) {
        alert("Please enter valid numbers");
        return;
    }


    let pourcentage = ((billAmmount/100)*tipAmmount);
    let somme = billAmmount+pourcentage;

    result.innerText = `${somme.toFixed(2)} €`;
}


btnEl.addEventListener("click", CalculatorTip);