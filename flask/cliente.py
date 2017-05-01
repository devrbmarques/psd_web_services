# -*- coding: utf-8 -*-
#Adriano Freitas - https://adrianofreitas.me
#Robson Borges - http://rbmarques.com.br

import requests, json
import sys, getopt, os

def ajuda():
    ajuda = "\n+++++++++++++++++++++++++++++++++++++"
    ajuda += "\nCOD\t\tFUNCAO\nlistar\t\tExibir Status Salas\nreservar <N>\tReservar Sala\nliberar <N>\tLiberar Sala\najuda\t\tExibir Ajuda"
    ajuda += "\n"
    ajuda += "\n\nExemplos:\n\treservar 1\n\treservar 2\n\tliberar 1"
    ajuda += "\n+++++++++++++++++++++++++++++++++++++"
    print (ajuda)

def main():
    #limpa a tela
    os.system('clear')
    ##faz um get para preencher o BANCO DE DADOS
    r=requests.get('http://localhost:5000/init')

    ajuda()
    while(True):
        print("\nDIGITE UM COMANDO(<ajuda> PARA EXIBIR OS COMANDOS): ")
        cmd = input()
        os.system('clear')
        if cmd == 'ajuda':
            ajuda()
        elif cmd == 'listar':
            ##faz um get e lista as salas e seus status
            r=requests.get('http://localhost:5000/index')
            ## Exibe as informaçções
            data = json.loads(r.text)
            #calcula o tamanho da lista retornada
            length = len(data)
            if length==0:
                print ("POR FAVOR. REINICIE O CLIENTE")
            else:
                #Exibe as salas e status
                print("ID\tSALA\tSTATUS")
                #Percorre a lista e Exibe as salas e status
                for x in range(0,length):
                    print ("%s\t%s\t%s" % (data[x]['id'], data[x]['sala'],data[x]['status']))
        elif cmd == 'resetar' :
            ##faz um get e reseta o banco de dados
            r=requests.get('http://localhost:5000/init')
            #exibe a resposta
            print(r.text)
        elif cmd.find('reservar') >= 0:
            #define os headers
            headers = {'content-type' : 'application/json'}
            id_sala = cmd[-1]
            action='reservar'

            #JSON formatado
            #payload = {'id': '1', 'action': 'reservar'}
            payload = {u"id": id_sala, u"action":action}
            #URL que para alterar status da sala
            url = 'http://localhost:5000/update'

            #Realiza as requisições do tipo POST
            #e armazenas a resposta na variavel r
            r=requests.post(url, data=payload)

            #exibe a resposta
            print(r.text)

        elif cmd.find('liberar') >= 0:
            headers = {'content-type' : 'application/json'}
            id_sala = cmd[-1]
            action='liberar'

            #JSON formatado
            #payload = {'id': '1', 'action': 'reservar'}
            payload = {u"id": id_sala, u"action":action}
            #URL que para alterar status da sala
            url = 'http://localhost:5000/update'

            #Realiza as requisições do tipo POST
            #e armazenas a resposta na variavel r
            r=requests.post(url, data=payload)

            #exibe a resposta
            print(r.text)
        else:
            print("Algo deu errado!")

# chama a funcao principal
if __name__ == "__main__":
    main()
