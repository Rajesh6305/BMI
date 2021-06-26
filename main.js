function calcBMI(weight1,height1) {
var weight1 = document.main.weight.value;
var height1 = document.main.height.value;
var bmi = parseInt(weight1/(height1*height1));
if(bmi < 18.5){
	window.location.href='underweight.html';
}
else if(bmi >= 18.5 && bmi <= 24.9){
	window.location.href='fit.html';
}
else if(bmi >= 25 && bmi <= 29.9){
	window.location.href='overweight.html';
} 
else{
	window.location.href='obese.html'; 
}
}