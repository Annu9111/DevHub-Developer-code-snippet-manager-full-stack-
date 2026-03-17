function copyCode(button){
    const code = button.nextElementSibling.innerText;

    navigator.clipboard.writeText(code);

    button.innerText = "✅ Copied!";

    setTimeout(()=>{
        button.innerText = "📋 Copy";
    },2000);
}

