# Exercício 4 Programação de Sistemas Distribuídos
# Adriano Freitas <adrianofreitas.me>
# Robson Borges <rbmarques.com.br>

## URL e Tipo de requisição HTTP

# As URLs abaixo suportam apenas GET, quando requisitada chama a função index()
#Essa função retorna um texto no formato JSON, que contém uma lista com as salas e seus respectivos status
localhost:5000/
localhost:5000/index

# A URL abaixo suportam apenas GET, quando requisitada chama a função popular_DB()
#Essa função verifica o Banco de Dados salas.db, se o mesmo estiver vazio essa função preencher-o com alguns dados
localhost:5000/init

# A URL abaixo suporta apenas POST, quando requisitada chama a função atualizar_status()
# Essa função recebe dois parâmetros via formulário WEB(action e id), através desses parâmetros ela verifica o status atual sala(identificada pelo id) e dependendo do parâmetro 'action' ela altera o status da sala. Ela também faz todas as checagens de erros
localhost:5000/update
