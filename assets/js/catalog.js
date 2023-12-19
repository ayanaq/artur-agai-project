// let iconCart = document.querySelector('.icon_cart');
// let closeCart = document.querySelector('.close');
// let body = document.querySelector('body');
// let listProductHTML = document.querySelector('.listProduct');

// let listProducts = [];
// iconCart.addEventListener('click' , () => {
//     body.classList.toggle('showCart');
//     // console.log('faji');
// })

// closeCart.addEventListener('click' , () => {
//     body.classList.toggle('showCart');
// })

// const addDataToHTML = () => {
//     listProductHTML.innerHTML = '';
//     if(listProducts.length > 0){
//         listProducts.forEach( product => {
//             let newProduct = document.createElement('div');
//             newProduct.classList.add('item');
//             newProduct.innerHTML = `
//             <img src="${product.image}" alt="">
//             <h2>GYNO-TARDYFERON</h2>
//             <div class="price">$3,99</div>
//             <button class="addCart">
//                 Add To Cart
//             </button>
//         `;
//         listProductHTML.appendChild(newProduct);
//         })
//     }
// }

// listProductHTML.addEventListener('click' , (event) => {
//     let positionClick = event.target;
//     if(positionClick.classList.contains('addCart')){
//         alert('1');
//     }
// })

// async function getProducts() {
//     let response = await fetch('http://85.209.9.201:666/api/v1/catalog/products/')
//     if (response.ok) {
//         let json = await response.json()
//         console.log(json)
//     } else {
//         alert(response)
//     }
// }

// getProducts();

// const initApp = () => {
//     fetch('/assets/js/catalog.json')
//     .then(Response => response.json())
//     .then(data => {
//         listProducts = data;
//         addDataToHTML();  
//     })
// }
// initApp();
let listProductHTML = document.querySelector('.listProduct');
let listCartHTML = document.querySelector('.listCart');
let iconCart = document.querySelector('.icon_cart');
let iconCartSpan = document.querySelector('.icon_cart span');
let body = document.querySelector('body');
let closeCart = document.querySelector('.closebtnhum');
let products = [];
let cart = [];


iconCart.addEventListener('click', () => {
    body.classList.toggle('showCart');
    console.log("fnwj")
})
closeCart.addEventListener('click', () => {
    body.classList.toggle('showCart');

    console.log("fnwj")

})

    const addDataToHTML = () => {
    // remove datas default from HTML

        // add new datas
        if(products.length > 0) // if has data
        {
            products.forEach(product => {
                let newProduct = document.createElement('div');
                newProduct.dataset.id = product.id;
                newProduct.classList.add('item');
                newProduct.innerHTML = 
                `<img src="${product.image}" alt="">
                <h2>${product.name}</h2>
                <div class="price">$${product.price}</div>
                <button class="addCart">Add To Cart</button>`;
                listProductHTML.appendChild(newProduct);
            });
        }
    }
    listProductHTML.addEventListener('click', (event) => {
        let positionClick = event.target;
        if(positionClick.classList.contains('addCart')){
            let id_product = positionClick.parentElement.dataset.id;
            addToCart(id_product);
        }
    })
const addToCart = (product_id) => {
    let positionThisProductInCart = cart.findIndex((value) => value.product_id == product_id);
    if(cart.length <= 0){
        cart = [{
            product_id: product_id,
            quantity: 1
        }];
    }else if(positionThisProductInCart < 0){
        cart.push({
            product_id: product_id,
            quantity: 1
        });
    }else{
        cart[positionThisProductInCart].quantity = cart[positionThisProductInCart].quantity + 1;
    }
    addCartToHTML();
    addCartToMemory();
}
const addCartToMemory = () => {
    localStorage.setItem('cart', JSON.stringify(cart));
}
const addCartToHTML = () => {
    listCartHTML.innerHTML = '';
    let totalQuantity = 0;
    if(cart.length > 0){
        cart.forEach(item => {
            totalQuantity = totalQuantity +  item.quantity;
            let newItem = document.createElement('div');
            newItem.classList.add('item');
            newItem.dataset.id = item.product_id;

            let positionProduct = products.findIndex((value) => value.id == item.product_id);
            let info = products[positionProduct];
            listCartHTML.appendChild(newItem);
            newItem.innerHTML = `
            <div class="image">
                    <img src="${info.image}">
                </div>
                <div class="name">
                ${info.name}
                </div>
                <div class="totalPrice">$${info.price * item.quantity}</div>
                <div class="quantity">
                    <span class="minus"><</span>
                    <span>${item.quantity}</span>
                    <span class="plus">></span>
                </div>
            `;
        })
    }
    iconCartSpan.innerText = totalQuantity;
}

listCartHTML.addEventListener('click', (event) => {
    let positionClick = event.target;
    if(positionClick.classList.contains('minus') || positionClick.classList.contains('plus')){
        let product_id = positionClick.parentElement.parentElement.dataset.id;
        let type = 'minus';
        if(positionClick.classList.contains('plus')){
            type = 'plus';
        }
        changeQuantityCart(product_id, type);
    }
})
const changeQuantityCart = (product_id, type) => {
    let positionItemInCart = cart.findIndex((value) => value.product_id == product_id);
    if(positionItemInCart >= 0){
        let info = cart[positionItemInCart];
        switch (type) {
            case 'plus':
                cart[positionItemInCart].quantity = cart[positionItemInCart].quantity + 1;
                break;
        
            default:
                let changeQuantity = cart[positionItemInCart].quantity - 1;
                if (changeQuantity > 0) {
                    cart[positionItemInCart].quantity = changeQuantity;
                }else{
                    cart.splice(positionItemInCart, 1);
                }
                break;
        }
    }
    addCartToHTML();
    addCartToMemory();
}

const initApp = () => {
    // get data product
    fetch('catalog.json')
    .then(response => response.json())
    .then(data => {
        products = data;
        addDataToHTML();

        // get data cart from memory
        if(localStorage.getItem('cart')){
            cart = JSON.parse(localStorage.getItem('cart'));
            addCartToHTML();
        }
    })
}
initApp();