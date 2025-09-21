from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

menu_items = [
    {"id": 1, "nome": "Sushi Salmão", "preco": 25.00, "categoria": "sushi"},
    {"id": 2, "nome": "Hot Roll", "preco": 38.00, "categoria": "hot_roll"},
    {"id": 3, "nome": "Temaki Frito", "preco": 42.00, "categoria": "temaki"},
    {"id": 4, "nome": "Uramaki", "preco": 24.90, "categora": "uramaki"}
]

@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items)

#SEARCH POR ID
@app.route('/menu/<int:id>',methods=['GET'])
def menu_id(id):
    for menu in menu_items:
       if menu.get('id') == id:
           return jsonify(menu)
       return jsonify({"error": "Item não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)