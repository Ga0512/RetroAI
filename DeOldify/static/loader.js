// Verificar se a página foi carregada através de um recarregamento (F5)
window.addEventListener('load', function () {
    var loader = document.getElementById('loaders');
    loader.style.display = 'none'; // Ocultar a mensagem de "Carregando..." após o carregamento da página
});

document.getElementById('upload-form').addEventListener('submit', function (event) {
    // Exibir a mensagem de "Carregando..." ao enviar o formulário
    var loader = document.getElementById('loaders');
    loader.style.display = 'block';
});


