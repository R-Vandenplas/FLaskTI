var btn_recherche = document.getElementById('btn_recherche');
console.log(btn_recherche);
btn_recherche.addEventListener('click', function(event) {
    event.preventDefault();
    let nom_film = document.getElementById('nom_recherche').value;
    window.location.href="/rech?nom=" + nom_film;
});