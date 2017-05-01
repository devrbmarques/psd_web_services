# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.

    :adapted by:
        Adriano Freitas - adrianofreitas.me
        Robson Borges - rbmarques.com.br
"""

import os
import json
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'salas.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#se a requisicao para a URL / ou /index for do tipo GET
@app.route('/')
@app.route('/index')
def index():
    #conecta com o BD
    db = get_db()
    #faz uma consulta no banco de dados
    cur = db.execute('SELECT id,sala, status FROM salas ORDER BY id ASC')
    entries = cur.fetchall()
    
    #Cria uma string JSON e retorna para o cliente
    rows = [ dict(ix) for ix in entries ]
    
    return json.dumps(rows)

#se a requisicao para a URL /init for do tipo GET
@app.route('/init', methods=['GET'])
def popular_DB():
    #Inicializa DB
    db = get_db()
    #Captura os valores do DB e ordena (ordem crescente)
    cur = db.execute('SELECT id,sala, status FROM salas ORDER BY id ASC')
    #armazenas os valores na variavel entries
    entries = cur.fetchall()

    #verifica se existe algum valor na variavel entries
    #
    if len(entries)==0:
        status = 'livre'

        ## Bloco A :)
        sala = 'A0'
        for x in range(1, 5):
            db.execute('INSERT INTO salas (sala, status) VALUES (?, ?)',
                       [ sala+str(x), status ] )
        db.commit()#gravas as informacoes no BD

        ## Bloco B :)
        sala = 'B0'
        for x in range(1, 5):
            db.execute('INSERT INTO salas (sala, status) VALUES (?, ?)',
                       [ sala+str(x), status ] )
        db.commit()#gravas as informacoes no BD
        #RETORNA UMA MSG
        return 'BANCO DE DADOS PREENCHIDO'
    return 'ERROR'

#se a requisicao para a URL /update for do tipo POST
@app.route('/update', methods=['POST'])
def atualizar_status():
    #armazenas requisicoes HTTP
    data = request.form

    #Armazenas dados da chave ACTION no json
    action=data['action']

    #verifica se o valor e inteiro
    try:
        #Armazenas dados da chave ID no json
        id_sala=int(data['id'])
    except ValueError:
        return ("Valor INVALIDO")

    ##GET DB
    db = get_db()
    cur = db.execute('SELECT status FROM salas WHERE id = ?',
                    [id_sala])
    entries = cur.fetchall()

    #Verifica se o valor existe no BD
    if len(entries)==0:
        return ("ID INVALIDO. DIGITE <listar> PARA LISTAR AS SALAS")
    else:
        #Converte os dados do SQLite para JSON
        sala = [ dict(ix) for ix in entries ]
        #Pega o status atual da string JSON
        status_atual = sala[0]['status']

        #Se action for 'reservar'...
        if action == 'reservar':
            #verifica o status atual  da sala
            if status_atual == "ocupada":
                message = 'ERRO: A sala NAO esta livre\n'
            else:
                status="ocupada"
                #atualiza o status no BD
                db.execute('UPDATE salas SET  status = ? WHERE id = ?',
                           [ status, id_sala])
                db.commit()
                message = 'Sala reservada\n'
        elif action == 'liberar':#Se action for 'liberar'...
            #verifica o status atual  da sala
            if status_atual == "livre":
                message = 'ERRO: A sala JA esta livre\n'
            else:
                status="livre"
                #atualiza o status no BD
                db.execute('UPDATE salas SET  status = ? WHERE id = ?',
                           [ status, id_sala])
                db.commit()
                message = 'Sala liberada\n'

        else:
            message = "Error\n"

    #retorna uma mensagem para o cliente
    return message
