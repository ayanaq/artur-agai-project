let signupBtn = document.getElementById("signupBtn");
let signinBtn = document.getElementById("signinBtn");
let usernameField = document.getElementById("usernameField");
let emailField = document.getElementById("emailField");
let passwordField = document.getElementById("passwordField");
let title = document.getElementById("title");
let sendBtn = document.getElementById("sendBtn")
let formAuth = document.getElementById("formAuth")


signinBtn.onclick = function(){
    emailField.style.maxHeight = "0";
    title.innerHTML = "Sign In";
    signupBtn.classList.add("swipe");
    signinBtn.classList.remove("swipe");
    console.log('')

}

signupBtn.onclick = function(){
    emailField.style.maxHeight = "60px";
    title.innerHTML = "Sign Up";
    signupBtn.classList.remove("swipe");
    signinBtn.classList.add("swipe");

}

formAuth.addEventListener('submit', (event) => {
    event.preventDefault();
    let username = usernameField.value;
    let email = emailField.value;
    let password = passwordField.value;
    
    if (signupBtn.classList.contains('swipe')) {
        signIn(username, email, password);
    }
})

async function signIn(username, password) {
    data = {
        username: username,
        password: password
    }

    let response = await fetch('http://85.209.9.201/api/v1/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
      });

    if (response.ok) {
        let json = await response.json();
        console.log(json);
    } else {
        alert("Ошибка HTTP: " + response.status)
    }
}

let closeCart = document.querySelector('.closebtnhum');
closeCart.addEventListener('click', () => {
    body.classList.toggle('showCart');
    console.log("fnwj")
})

function toggleNav() {
    var burgermenu = document.querySelector('.burgerMenu123');
    burgermenu.classList.toggle('showNav');
    console.log("fnwj");
}

var closeburg = document.querySelector('.closeBurger');
closeburg.addEventListener("click", function() {
    var burgermenu = document.querySelector('.burgerMenu123');
    burgermenu.classList.remove('showNav');
    console.log("fnwj");
});