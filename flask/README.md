# Programação de Sistemas Distribuídos - UEA
## Exercício 4
### Contrbuidores
- Adriano Freitas - https://adrianofreitas.me
- Robson Marques - www.rbmarques.com.br

## Para iniciar o Servidor
### Como configurar e executar o servidor Flask
#### Primeira maneira(Passo-a-passo)
1. Instalar o aplicativo a partir da raiz do projeto
```shell
	$ pip install --editable .
```
2. Apontar para a aplicação correta
```shell
	$ export FLASK_APP=flaskr
```

3. Inicializar o banco de dados
```shell
	$ flask initdb
```

4. Agora basta executar o comando abaixo para rodar o servidor. A aplicação deverá rodar no endereço  http://localhost:5000/
```shell
	$ flask run
```

#### Segunda maneira
1. Simplesmente execute o comando abaixo, ele fará todo o processo de configuração.
```shell
        sh configurar.sh
```
2. Agora basta executar o comando abaixo para rodar o servidor. A aplicação deverá rodar no endereço  http://localhost:5000/
```shell
	$ flask run
```

## Para iniciar o Cliente. Considerando que o servidor esteja configurado e no ar.
1. Simplesmente execute o comando abaixo.
```shell
  $ python3 cliente.py
```
