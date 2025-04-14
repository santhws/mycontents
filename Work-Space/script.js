// // alert("Hello-Word");
// var caixa;

// caixa = "lego";

// console.log(caixa);

// ---------------------------------------------------

// var idade = 20;

// var menor10 = idade <= 10;
// var maior30 = idade >= 30;

// var gratuidade = menor10 || maior30;

// console.log("Idade", idade);
// console.log("Menor que 10", menor10);
// console.log("Maior que 30", maior30);
// console.log("Tem direito a gratuidade?", gratuidade);

// ---------------------------------------------------

// var numero = parseInt(prompt("Digite um Número"));

// var dobro = numero + numero;

// alert("O dobro de " + numero + " é " + dobro);

// ---------------------------------------------------

// var idade = 22;

// if (idade < 18 || idade > 70) {
//   console.log("Pode");
//   console.log("Qual o seu pedido");
// } else {
//   console.log("Não Pode");
//   console.log("Mostre sua Indetidade");
// }

// ---------------------------------------------------

// var nota1 = 7;
// var nota2 = 5.5;

// var media = (nota1 + nota2) / 2;

// var conceito = "";

// if (media >= 8) {
//   conceito = "Òtimo";
// } else if (media >= 6.5) {
//   conceito = "Bom";
// } else {
//   conceito = "Regular";
// }

// console.log(media);
// console.log(conceito);

// switch (conceito) {
//   case "Òtimo":
//     console.log("Parabéns");
//     break;
//   case "Bom":
//     console.log("Indo Bem");
//     break;
//   case "Regular":
//     console.log("Quase");
//     break;

//   default:
//     console.log("Houve algum Erro");
// }

// ---------------------------------------------------

// var numero = 5;

// for (var vez = 1; vez <= numero; vez++) {
//   console.log("Execuntando o for pela " + vez + " Vez");
// }

// console.log("Acabou!");

// ---------------------------------------------------

var alunos = ["Fabio", "Gaby", "Teo", "Karma"];

// for (var i = 0; i < alunos.length; i++) {
//   console.log(alunos[i]);
// }

for (var aluno of alunos) {
  console.log(aluno);
}
