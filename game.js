document.addEventListener('DOMContentLoaded', init, false);

function init() {
    let fifty_button = document.querySelector('button');
    fifty_button.addEventListener('click', fifty_code, false)
    
}   


function fifty_code(){
    let fifty_button = document.querySelector('button');
fifty_button.disabled = true
    let all_options = document.querySelectorAll('.pick');  
    let all_labels = document.querySelectorAll('label');
    let x = all_labels[3].innerText
    let correct =  document.querySelector('#hidden');

    for(let x of all_labels) {

        x.innerText = ''
  
    }

    all_labels[0].textContent = correct.textContent
    all_labels[3].textContent = x

    for (let y of all_options) {

        y.disabled = true;

    }

   
    all_options[0].disabled = false
    all_options[0].value = correct.textContent[0]

    all_options[3].disabled = false
    all_options[3].value = x
    
    fifty_button.disabled = true

}

