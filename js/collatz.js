

var doCollatz = function(number){
	var result;
	if(number == 1){
		return;
	}

	if(number % 2 == 0){
		result = number / 2;
	}else{
		result = 3 * number + 1;
	}

	document.getElementById("results").innerHTML += "Step: " + result + "</br>"

	doCollatz(result);
}

function calculate(){
	var number = parseInt(document.getElementById("input").value);
	if (number>=0){
		document.getElementById("results").innerHTML += "Number: " + number + "</br>"
		doCollatz(number);
	}else
		alert("Invalid input, please write a positive number.");
}

document.getElementById("button").onclick = calculate;