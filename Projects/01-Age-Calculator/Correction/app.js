const btnElement = document.getElementById("btn");
const birthElement = document.getElementById("birth");

function CaclulatorAge()
{
    let currentDate = new Date();
    let birthDate = birthElement.value;

    if(birthDate === "")
    {
        alert("Please enter a date")
    }
    
}

btnElement.addEventListener("click", CaclulatorAge);