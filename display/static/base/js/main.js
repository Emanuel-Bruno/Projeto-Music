
const maximizar_caixa_selecao = ()=>{
    document.getElementById('body_caixa_selecao').classList.add('maximizado')
    document.getElementById('maximizador_caixa_selecao').style.display="none"
    document.getElementById('minimizador_caixa_selecao').style.display="block"
    document.getElementById('conteudo_caixa_selecao').style.display="block";
}

const minimizar_caixa_selecao = ()=>{
    document.getElementById('body_caixa_selecao').classList.remove('maximizado')
    document.getElementById('minimizador_caixa_selecao').style.display="none"
    document.getElementById('maximizador_caixa_selecao').style.display="block"
    document.getElementById('conteudo_caixa_selecao').style.display="none";
}

