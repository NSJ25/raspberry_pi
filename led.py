from gpiozero import LED, Button, Buzzer, RGBLED #importatio des module utile pour le controle de ses composant
from time import sleep #importation du tem

# Initialisation des LEDs connectées aux broches GPIO 14 et 15 
led1 = LED(14) 
led2 = LED(15) 

# Initialisation du buzzer connecté à la broche GPIO 18
buzzer = Buzzer(18) 

# Initialisation de la LED RGB avec ses broches rouge, verte et bleue
rgb = RGBLED(red=16, green=20, bleu=21)  

# Initialisation des boutons avec gestion anti-rebond (bounce_time = temps à attendre pour ignorer un faux appui)
bouton = Button(23, bounce_time=0.5) 
bouton_buzz = Button(24, bounce_time=0.5) #
 
# Fonction pour contrôler le buzzer et la LED RGB selon l'état du bouton buzzer
def control_buzzer():
	 # Si le bouton buzzer est appuyé
	if bouton_buzz.is_pressed: 
		buzzer.on()
		rgb.color = (0,1,0)
		sleep(5)
		buzzer.off()
	else:
		buzzer.off()
		rgb.color = (1,0,0)

# Fonction pour allumer successivement les deux LEDs quand le bouton normal est appuyé
def allumage():
	if bouton.is_pressed:
		led1.on()
		sleep(2)
		led1.off()
		led2.on()
		sleep(2)
		led2.off()
		# LED RGB passe au rouge (indique buzzer éteint)
	else: 
		# Si bouton pas appuyé, LEDs éteintes
		led1.off()
		led2.off()

# Boucle infinie qui vérifie sans cesse l'état des boutons et agit en conséquence
while True:
	control_buzzer()
	allumage()

	
