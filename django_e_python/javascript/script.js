function gritar() {
	alert("AHHHHHHHHHHHHHHHH");
}

function perguntar() {
	var nome;
	var idade;
	nome = prompt("Qual é o seu nome? ");
	idade = prompt("Quantos aos você tem?")
	alert("Olá " + nome + "!" + " Você tem " + idade + " anos.");
}

function mudar_texto() {
	var h1 = document.getElementsByTagName("h1")

	if(h1[0].innerText == "Geek University"){
		h1[0].innerText = "Evolua seu lado geek!";
	}else{
		h1[0].innerText = "Geek University"
	}
} 

function incrementar() {
	var p1 = document.getElementById("p1");

	p1.innerText = parseInt(p1.innerText) + 1;
}