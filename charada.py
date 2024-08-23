from flask import Flask, jsonify
from flask_cors import CORS
import random

lista_charadas = [
    {"Pergunta": "Cai em pé e corre deitado, mas não cai deitado. O que é?", "Resposta": "chuva"},
    {"Pergunta": "O que é um pontinho amarelo que cai do céu?", "Resposta": "Um Yellowcóptero"},
    {"Pergunta": "O que é cheio de furos, mas ainda segura muita água?", "Resposta": "uma esponja"},
    {"Pergunta": "O que tem olhos, mas não vê?", "Resposta": "uma agulha"},
    {"Pergunta": "Quanto mais seca, mais molhada fica. O que é?", "Resposta": "uma toalha"},
    {"Pergunta": "O que não pode ser usado antes de ser quebrado?", "Resposta": "um ovo"},
    {"Pergunta": "O que tem uma cabeça, uma cauda, mas não tem corpo?", "Resposta": "uma moeda"},
    {"Pergunta": "O que tem raízes que ninguém vê, é maior que as árvores, cresce sem parar, mas não é árvore?", "Resposta": "uma montanha"},
    {"Pergunta": "O que você pode segurar com a mão esquerda, mas não com a direita?", "Resposta": "a mão direita"},
    {"Pergunta": "O que sobe, mas nunca desce?", "Resposta": "a sua idade"},
    {"Pergunta": "O que corre, mas nunca anda; tem uma cama, mas nunca dorme; tem boca, mas nunca come?", "Resposta": "um rio"},
    {"Pergunta": "O que tem dentes, mas não pode morder?", "Resposta": "um pente"},
    {"Pergunta": "O que é pequeno, mas pode encher uma sala?", "Resposta": "uma luz acesa"},
    {"Pergunta": "O que tem muitas chaves, mas não pode abrir nenhuma porta?", "Resposta": "um piano"},
    {"Pergunta": "O que tem pés, mas não pode andar?", "Resposta": "uma mesa"},
    {"Pergunta": "O que pode atravessar uma parede sem deixar rastro?", "Resposta": "um buraco"},
    {"Pergunta": "O que sempre cai e nunca se machuca?", "Resposta": "a chuva"},
    {"Pergunta": "O que é leve como uma pena, mas ninguém pode segurar por muito tempo?", "Resposta": "a respiração"},
    {"Pergunta": "O que viaja pelo mundo, mas fica no mesmo lugar?", "Resposta": "um selo postal"},
    {"Pergunta": "O que tem uma face, mas nunca sorri?", "Resposta": "um relógio"}
]


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'API CHARADA ESTÁ ONLINE!'

@app.route('/charadas', methods=['GET'])
def charadas():
    charadas = random.choice(lista_charadas)
    return jsonify(charadas)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)