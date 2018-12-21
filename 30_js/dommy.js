var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var fact = (n) => {
  if ( n == 0 ) {
    return 1;
  }
  return n * fact(n-1);
}

//list vars
var list_num = 8;
var list = document.getElementById("thelist");
var list_button = document.getElementById("b");

//heading
var heading = document.getElementById("h");

//fib vars
var fib_num = 0;
var fib_list = document.getElementById("fiblist");
var fib_button = document.getElementById("fb");

//fact vars
var fact_num = 0;


//when the list button is clicked, another list element is appended
list_button.addEventListener('click', function(){
    var li = document.createElement("li");
    li.innerHTML = "item " + list_num;
    list.appendChild(li);
    list_num++;
});

//when the mouse is over a list item, the heading contains the text of the list item
list.addEventListener('mouseover', function(e){
    console.log(e.target.innerHTML);
    heading.innerHTML = e.target.innerHTML;
});

//when the mouse is not over a list item, the heading defaults
list.addEventListener('mouseout', function(){
    heading.innerHTML = "Hello World!";
});

//when a list item is clicked, it is removed
list.addEventListener('click', function(e){
    console.log(e);
    list.removeChild(e.target);
});

//when fib button is clicked, the next fib number is appended to the fib list
fib_button.addEventListener('click', function(){
    var li = document.createElement("li");
    li.innerHTML = `fib(${fib_num}) = ` + fibonacci(fib_num);
    fib_list.appendChild(li);
    fib_num++;
});


//additional name list stuff
var fact_button = document.createElement("button");
fact_button.innerHTML = "fact";
fib_button.insertAdjacentElement('afterend', fact_button);
var fact_list = document.createElement("ol");
//fact_list.setAttribute("id", "fact_list");
list_button.parentNode.insertBefore(fact_list, list_button);

fact_button.addEventListener('click', function(){
    var li = document.createElement("li");
    console.log("test");
    li.innerHTML = `fact(${fact_num}) = ` + fact(fact_num);
    fact_list.appendChild(li);
    fact_num++;
});
