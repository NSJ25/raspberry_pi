from flask import Flask, render_template
from gpiozero import LED

# activation du serveur Flask
app = Flask(__name__) 

# Route pour la page d'accueil
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Initialisation de la LED sur GPIO 14
led = LED(14)  

# Route pour allumer/éteindre la LED
@app.route('/etat_led', methods=['POST'])
def led_on():
    if led.is_lit:
        led.off()
    else:       
        led.on()
    
    # Message à afficher en fonction de l'état de la LED        
    message = "La LED est allumée" if led.is_lit else "La LED est éteinte"
    
    # Récupération de l'état de la LED
    etat = "Éteindre" if led.is_lit else "Allumer"      
    
    # Rendu du template avec le message et l'état de la LED
    return render_template('index.html', message=message, etat=etat)

# Démarrage du serveur Flask
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
