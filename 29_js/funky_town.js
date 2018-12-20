var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var gcd = (a, b) => {
  if ( b == 0 ) {
    return a;
  }
  return gcd(b, a % b);
}

var students = ["Sam", "Tom", "Bobby", "Smith", "Tony", "John"];

var randomStudent = () => {
  return students[Math.floor(Math.random() * students.length)];
}

document.getElementById("fib_button").addEventListener("click", function() {
  var output = fibonacci(5);
  document.getElementById("fib_p").innerHTML = "fibonacci(5): " + output;
  console.log(output);
});
document.getElementById("gcd_button").addEventListener("click", function() {
  var output = gcd(25, 55);
  document.getElementById("gcd_p").innerHTML = "gcd(25, 55): " + output;
  console.log(output);
});
document.getElementById("random_student_button").addEventListener("click", function() {
  var output = randomStudent();
  document.getElementById("random_student_p").innerHTML = "randomStudent(): " + output;
  console.log(output);
});
