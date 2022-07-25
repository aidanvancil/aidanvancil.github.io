function search_portfolio(random) {
    let input = document.getElementById('query').value
    random = random || '';
    if (random != '') {
        input = random
    }
    input=input.toLowerCase();
    let x = document.getElementsByClassName('modals');
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";                 
        }
    }
}