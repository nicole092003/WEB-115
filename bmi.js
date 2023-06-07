

function doCalcBMI(){
    let theWeight = document.getElementById("myPounds").value;
    let theHeight = document.getElementById("myHeight").value;
    let myBMI = theWeight / (theHeight * theHeight)*703;
    myBMI = myBMI.toFixed(2);
    document.getElementById("bmiResult").innerHTML = myOutput(myBMI);
};
function myOutput(myBMI){
    let theString = "Your body mass index (BMI) is: " + (myBMI);
    return theString;
};

document.getElementById("CalcBMI").addEventListener("click",doCalcBMI);

