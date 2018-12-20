var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

document.getElementById("b").addEventListener("click", function(){
    int num = 8;
    var list = document.getElementByID("thelist");
    var li = document.createElement("li");
    li.innerHTML="item " + num;
    list.appendChild(li);
    num++;
});
