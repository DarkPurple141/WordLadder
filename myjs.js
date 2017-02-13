
function value_check() {
	var returnval = true;

	var pass = document.getElementById('word1');
	var confirm = document.getElementById('word2');
	var list = [pass,confirm];

	for (i = 0; i < list.length; i++) { 
    	if (!(list[i].value)) {
			list[i].style.borderColor = "Red";
			returnval = false;
		}
	}

	if (pass.value && confirm.value) {
		if (pass.value.length != confirm.value.length) {
			alert("Words have to be the same length.")
			pass.style.borderColor = "Red";
			confirm.style.borderColor = "Red";
			return false;
		}
		
	} 

	if (!(returnval)) {
		alert("Please fill in all fields before continuing.")
		return returnval;
	}

}

function clickfunction(id) {
	var el = document.getElementById(id);
	//var el = document.querySelector("div.onclick_text");
	var hide = el.style.display == "block";
	if (hide) {
		el.style.display = "none";
	} else {
		el.style.display = "block";
	}
}