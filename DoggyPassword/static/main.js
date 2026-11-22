function copyPassword() {
    navigator.clipboard.writeText(
        document.getElementById("password").innerText
    );
    alert("✅ Password copied !");
}