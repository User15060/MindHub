const btnElement = document.getElementById("btn");
const birthElement = document.getElementById("birth");
const resultElement = document.getElementById("result")


function CaclulatorAge()
{
    let birthDate = birthElement.value;

    if(birthDate === "")
    {
        alert("Please enter a date");
        return;
    }

    const AGE = getAge(birthDate);

    resultElement.textContent = `You have ${AGE} years old`
}

function getAge(birthDate)
{
    const currentDate = new Date();
    const birthdayDate = new Date(birthDate);

    let ageYear = currentDate.getFullYear() - birthdayDate.getFullYear();
    let ageMonth = currentDate.getMonth() - birthdayDate.getMonth();

    if(ageMonth < 0 || ageMonth === 0 && currentDate.getDate() < birthdayDate.getDate())
    {
        ageYear--;
    }

    return ageYear;
}

btnElement.addEventListener("click", CaclulatorAge);