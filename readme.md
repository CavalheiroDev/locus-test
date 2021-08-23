# Locus Custom Software Teste
Uma aplicação desenvolvida para o teste técnico do processo seletivo da empresa Locus Custom Software.

## Rodando o projeto

### Requisitos:
* Certifique-se de que tem o python em sua versão 3 instalado.
* Tenha as portas 8080 e 8000 livres em sua máquina.


Para rodar o projeto em sua máquina clone o repositório com:

```
git clone https://github.com/CavalheiroDev/locus-test.git
```

Dentro da pasta do projeto instale as dependências:

```
pip install -r requirements.txt
```


Agora abra dois terminais, um para rodar a API e outro para rodar o front-end. 

Execute para a API:

```
uvicorn app.main:app --port 8080
```

Execute para o front-end:
* Caso linux:
```
python3 front/manage.py runserver
```
* Caso windows:
```
py front\manage.py runserver
```
