<<<<<<< HEAD
// const chatBody = document.querySelector(".chat-body");
// const txtInput = document.querySelector("#txtInput");
// const send = document.querySelector(".send");

send.addEventListener("click", () => renderUserMessage());

txtInput.addEventListener("keyup", (event) => {
  if (event.keyCode === 13) {
    renderUserMessage();
  }
});

const renderUserMessage = () => {
  const userInput = txtInput.value;
  renderMessageEle(userInput, "user");
  txtInput.value = "";
  setTimeout(() => {
    renderChatbotResponse(userInput);
    setScrollPosition();
  }, 600);
};

const renderChatbotResponse = (userInput) => {
  const res = getChatbotResponse(userInput);
  renderMessageEle(res);
};

const renderMessageEle = (txt, type) => {
  let className = "user-message";
  if (type !== "user") {
    className = "chatbot-message";
  }
  const messageEle = document.createElement("div");
  const txtNode = document.createTextNode(txt);
  messageEle.classList.add(className);
  messageEle.append(txtNode);
  chatBody.append(messageEle);
};

const getChatbotResponse = (userInput) => {
  return responseObj[userInput] == undefined
    ? "Ask Arthur agai "
    : responseObj[userInput];
};

const setScrollPosition = () => {
  if (chatBody.scrollHeight > 0) {
    chatBody.scrollTop = chatBody.scrollHeight;
  }
};



let closeCart = document.querySelector('.closebtnhum');
let burgerbtn = document.querySelector('.navbar_show_btn');
let burgermenu = document.querySelector('.burgerMenu123');
let closeburg=document.querySelector('.closeBurger');

burgerbtn.addEventListener('click', () => {
  burgermenu.classList.toggle('showNav');
  console.log("fnwj")
})
closeburg.addEventListener("click",()=>{
  burgermenu.classList.remove('showNav')
})

closeCart.addEventListener('click', () => {
  body.classList.toggle('showCart');

  console.log("fnwj")

})
=======
const chatBody = document.querySelector(".chat-body");
const txtInput = document.querySelector("#txtInput");
const send = document.querySelector(".send");

send.addEventListener("click", () => renderUserMessage());

txtInput.addEventListener("keyup", (event) => {
  if (event.keyCode === 13) {
    renderUserMessage();
  }
});

const renderUserMessage = () => {
  const userInput = txtInput.value;
  renderMessageEle(userInput, "user");
  txtInput.value = "";
  setTimeout(() => {
    renderChatbotResponse(userInput);
    setScrollPosition();
  }, 600);
};

const renderChatbotResponse = (userInput) => {
  const res = getChatbotResponse(userInput);
  renderMessageEle(res);
};

const renderMessageEle = (txt, type) => {
  let className = "user-message";
  if (type !== "user") {
    className = "chatbot-message";
  }
  const messageEle = document.createElement("div");
  const txtNode = document.createTextNode(txt);
  messageEle.classList.add(className);
  messageEle.append(txtNode);
  chatBody.append(messageEle);
};

const getChatbotResponse = (userInput) => {
  return responseObj[userInput] == undefined
    ? "Ask Arthur agai "
    : responseObj[userInput];
};

const setScrollPosition = () => {
  if (chatBody.scrollHeight > 0) {
    chatBody.scrollTop = chatBody.scrollHeight;
  }
};



let closeCart = document.querySelector('.closebtnhum');
let burgerbtn = document.querySelector('.navbar_show_btn');
let burgermenu = document.querySelector('.burgerMenu123');
let closeburg=document.querySelector('.closeBurger');

burgerbtn.addEventListener('click', () => {
  burgermenu.classList.toggle('showNav');
  console.log("fnwj")
})
closeburg.addEventListener("click",()=>{
  burgermenu.classList.remove('showNav')
})

// closeCart.addEventListener('click', () => {
//   body.classList.toggle('showCart');

//   console.log("fnwj")

// })
>>>>>>> main
