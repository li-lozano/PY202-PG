function copyToClickBoard(){
    const TEXTO = document.querySelector('.pg-text');

    navigator.clipboard.writeText(TEXTO.value)
        .then(() => {
        console.log("Texto copiado al clipboard...")
    })
        .catch(err => {
        console.log('Al parecer algo salio mal - ', err);
    })
}

function getNewPassword(){
    const TEXTO = document.querySelector('.pg-text');

    location.reload(TEXTO);

}


