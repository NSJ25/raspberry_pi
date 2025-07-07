from flask import Flask, render_template, Response
from gpiozero import RGBLED 

# Activation du serveur Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Initialisation de la LED RGB sur les broches GPIO 16, 20 et 21
led = RGBLED(red=16, green=20, blue=21)   

# Route pour allumer/éteindre la LED
@app.route('/rouge', methods=['POST'])
def rouge():
    # Allumer la LED en rouge
    led.color = (1, 0, 0)  # Rouge
    return Response("OK", status=200) 

# Route pour allumer la LED en vert
@app.route('/vert', methods=['POST'])
def vert():
    # Allumer la LED en vert
    led.color = (0, 1, 0)  # Vert
    return Response("OK", status=200)

# Route pour allumer la LED en bleu
@app.route('/bleu', methods=['POST'])
def bleu(): 
    # Allumer la LED en bleu
    led.color = (0, 0, 1)
    return Response("OK", status=200) 

# Route pour éteindre la LED
@app.route('/eteindre', methods=['POST'])
def led_off():
    # Éteindre la LED
    led.off()   
    return Response("OK", status=200) 

# Démarrage du serveur Flask
if __name__ == '__main__':
    app.run(host='localhost', port=8080)



    
    
    