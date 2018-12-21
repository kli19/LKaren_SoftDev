var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
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

