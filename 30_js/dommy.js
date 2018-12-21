var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}
var list_num = 8;
var list = document.getElementById("thelist");
var list_button = document.getElementById("b");

var heading = document.getElementById("h");

list_button.addEventListener('click', function(){
    var li = document.createElement("li");
    li.innerHTML="item " + list_num;
    list.appendChild(li);
    list_num++;
});

list.addEventListener('mouseover', function(e){
    console.log(e.target.innerHTML);
    heading.innerHTML = e.target.innerHTML;
});

list.addEventListener('mouseout', function(){
    heading.innerHTML = "Hello World!";
});

list.addEventListener('click', function(e){
    console.log(e);
    list.removeChild(e.target);
});
