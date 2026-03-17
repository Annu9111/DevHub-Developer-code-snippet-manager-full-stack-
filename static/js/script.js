function copyCode(button){
    const code = button.nextElementSibling.innerText;

    navigator.clipboard.writeText(code);

    button.innerText = "✅ Copied!";

    setTimeout(()=>{
        button.innerText = "📋 Copy";
    },2000);
}

setTimeout(() => {
    const flash = document.querySelector(".flash-message");
    if(flash){
        flash.style.display = "none";
    }
}, 3000);

