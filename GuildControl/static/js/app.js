// static/js/app.js

document.addEventListener("DOMContentLoaded", () => {

    console.log("GuildControl iniciado com sucesso!");

    const botoes = document.querySelectorAll("button");

    botoes.forEach(botao => {

        botao.addEventListener("click", () => {
            console.log("Botão clicado!");
        });

    });

    const formulario = document.querySelector("form");

    if (formulario) {

        formulario.addEventListener("submit", (e) => {

            console.log("Formulário enviado.");

        });

    }

});
