from gpiozero import Button, RGBLED
from time import time, sleep

# Initialisation de la LED RGB avec ses broches rouge, verte et bleue
rgb = RGBLED(red=16, green=20, blue=21)

# Initialisation du capteur tactile (Touch Sensor) sur GPIO 24
touch_sensor = Button(24)

# Fonction pour gérer le capteur tactile
def gerer_touch_sensor():
    # Si le capteur est touché, enchaîner plusieurs couleurs
    if touch_sensor.is_pressed:
        rgb.color = (0.5, 1, 0.8) # Couleur pastel verte
        sleep(0.5) 
        rgb.color = (0.7, 0.9, 1) # Bleu clair
        sleep(0.5)  
        rgb.color = (1, 0.8, 0.2) # Jaune-orangé
        sleep(0.5) 
        rgb.color = (1, 0.3, 1) # Magenta clair
        sleep(0.5)  
        rgb.color = (0.6, 1, 1) # Cyan pastel
        sleep(0.5)   
    else:
        # Si le capteur n’est pas touché, éteindre la LED
        rgb.color = (0, 0, 0)

# === Méthode alternative (désactivée) ===
# Autre méthode pour gérer le capteur tactile qui enchaîne les couleurs 
# Fonction pour gérer le capteur tactile
#def gerer_touch_sensor():
#   if touch_sensor.is_pressed:
#        # Si le capteur est touché, enchaîner plusieurs couleurs
#       couleurs = [
#           (0.5, 1, 0.8),   # Couleur pastel verte
#           (0.7, 0.9, 1),   # Bleu clair
#           (1, 0.8, 0.2),   # Jaune-orangé
#           (1, 0.3, 1),     # Magenta clair
#           (0.6, 1, 1)      # Cyan pastel
#        ]
        # Boucle pour changer de couleur toutes les 0.5 secondes
#       for couleur in couleurs:
#           rgb.color = couleur
#            sleep(0.5)
#    else:
        # Si le capteur n’est pas touché, éteindre la LED
#        rgb.color = (0, 0, 0)

# Boucle infinie qui vérifie sans cesse l'état du capteur tactile et agit en conséquence
while True:
    gerer_touch_sensor()
    sleep(0.1)  # Petite pause pour éviter une boucle trop rapide