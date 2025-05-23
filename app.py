from flask import Flask, request, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route("/")
def home():
    return "API para converter número por extenso"

@app.route("/extenso")
def extenso():
    numero = request.args.get('numero')
    idioma = request.args.get('lang', 'pt')
    try:
        valor = num2words(int(numero), lang=idioma)
        return jsonify({"extenso": valor})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
