from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Moslima Chatbot draait!"

@app.route('/chat', methods=['POST'])
def chat():
    vraag = request.json.get("message", "")
    antwoorden = {
        "wat is de hijab?": "De hijab is de islamitische hoofddoek die moslima’s dragen uit gehoorzaamheid aan Allah.",
        "wie is allah?": "Allah is de Enige God in de islam, de Schepper van alles.",
        "wat is halal?": "Halal betekent toegestaan volgens de islamitische wetten.",
    }
    antwoord = antwoorden.get(vraag.lower(), "Sorry zuster, daar heb ik nog geen antwoord op.")
    return jsonify({"response": antwoord})

if __name__ == "__main__":
    app.run()
