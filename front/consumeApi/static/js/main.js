cnpjs = document.querySelectorAll('#cnpj');

cnpjs.forEach(cnpj =>{
    cnpj.innerText = cnpj.innerText.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/g,"\$1.\$2.\$3\/\$4\-\$5")
});

cpfs = document.querySelectorAll('#cpf')
cpfs.forEach(cpf =>{
    cpf.innerText = cpf.innerText.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g,"\$1.\$2.\$3\-\$4")
});