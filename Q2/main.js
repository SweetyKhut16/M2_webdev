let stringCont = document.getElementById("str-var");
let intCont = document.getElementById("int-var");
let sumFuncAns = document.getElementById("sum-func-answer");
let if_elseAns = document.getElementById("if-else-header-answer");

// Variables
let stringVar = "Keshav";
stringCont.innerHTML = stringVar;
let integerVar = 20;
intCont.innerHTML = integerVar;

// Sum function
let sumFunc = (num1, num2) => {
  return num1 + num2;
};

// Setting the output of the function to html content
sumFuncAns.innerHTML = sumFunc(3, 6);

// Decision making
let age = 20;
if (age >= 18) {
  if_elseAns.innerHTML = "Yes";
} else {
  if_elseAns.innerHTML = "No";
}

// Loop to print multiples of 3
for (let a = 1; a < 11; a++) {
  document.write(a * 2 + "<br>");
}