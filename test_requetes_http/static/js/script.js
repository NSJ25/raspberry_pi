// fonction init() est appelée lorsque la page est chargée
function init(){
    console.log("Page chargée");
}

// fonction getId(id) retourne l'élément HTML avec l'ID spécifié
function getId(id){
    return document.getElementById(id);
}

// fonction onRouge() envoie une requête POST à l'URL "/rouge" et appelle la fonction allumeRouge lorsque la réponse est reçue
function onRouge(){
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/rouge", true);
    xhr.onload = allumerRouge;
    xhr.send();
}

// fonction allumeRouge() est appelée lorsque la requête POST à "/rouge" est terminée
function allumerRouge(){
    getId("result").innerText = "La LED rouge est allumée";
}

// fonction onVert() envoie une requête POST à l'URL "/vert" et appelle la fonction allumeVert lorsque la réponse est reçue
function onVert(){
     const xhr = new XMLHttpRequest();
    xhr.open("POST", "/vert", true);
    xhr.onload = allumerVert;
    xhr.send();
}

// fonction allumeVert() est appelée lorsque la requête POST à "/vert" est terminée
function allumerVert(){
    getId("result").innerText = "La LED verte est allumée";
}

// fonction onBleu() envoie une requête POST à l'URL "/bleu" et appelle la fonction allumeBleu lorsque la réponse est reçue
function onBleu(){
     const xhr = new XMLHttpRequest();
    xhr.open("POST", "/bleu", true);
    xhr.onload = allumerBleu;
    xhr.send();
}
// fonction allumeBleu() est appelée lorsque la requête POST à "/bleu" est terminée
function allumerBleu(){
    getId("result").innerText = "La LED bleue est allumée";
}

// fonction eteindre() envoie une requête POST à l'URL "/eteindre" et appelle la fonction eteindre lorsque la réponse est reçue
function eteindre(){
     const xhr = new XMLHttpRequest();
    xhr.open("POST", "/eteindre", true);
    xhr.onload = ledEteinte;
    xhr.send();
}

// fonction ledEteinte() est appelée lorsque la requête POST à "/eteindre" est terminée
function ledEteinte(){
    getId("result").innerText = "Toutes les LEDs sont éteintes";
}
/*// Version avec fetch API
function onRouge() {
    fetch("/rouge", { method: "POST" })
        .then(response => {
            if (response.ok) {
                getId("result").innerText = "La LED rouge est allumée";
            } else {
                getId("result").innerText = "Erreur lors de l'allumage en rouge.";
            }
        });
}

// Vert
function onVert() {
    fetch("/vert", { method: "POST" })
        .then(response => {
            if (response.ok) {
                getId("result").innerText = "La LED verte est allumée";
            } else {
                getId("result").innerText = "Erreur lors de l'allumage en vert.";
            }
        });
}

// Bleu
function onBleu() {
    fetch("/bleu", { method: "POST" })
        .then(response => {
            if (response.ok) {
                getId("result").innerText = "La LED bleue est allumée";
            } else {
                getId("result").innerText = "Erreur lors de l'allumage en bleu.";
            }
        });
}

// Éteindre
function eteindre() {
    fetch("/eteindre", { method: "POST" })
        .then(response => {
            if (response.ok) {
                getId("result").innerText = "Toutes les LEDs sont éteintes";
            } else {
                getId("result").innerText = "Erreur lors de l'extinction.";
            }
        });
}
*/