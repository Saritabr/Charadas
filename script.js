function esconderResposta(){
    document.getElementById('resposta').style.visibility = 'hidden'
}
function mostrarResposta(){
    document.getElementById('resposta').style.visibility = 'visible'
}

async function gerarCharada() {
    esconderResposta();
    const apiUrl = 'http://127.0.0.1/charadas';
    const pergunta = document.getElementById('pergunta');
    const resposta = document.getElementById('resposta');
    
    try {
    const response = await fetch (apiUrl);
    
    const dados = await response.json();
    console.log(dados)
    pergunta.innerHTML = dados.Pergunta;
    resposta.innerHTML = dados.Resposta;
    }
    catch (error) {
        console.error("API com problemas!")
    }
}