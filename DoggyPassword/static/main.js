function copyPassword() {
    navigator.clipboard.writeText(
        document.getElementById("password").innerText
    );
    alert("Mot de passe copié !");
}