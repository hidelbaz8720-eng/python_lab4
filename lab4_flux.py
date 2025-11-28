seuil = 10 # note minimale pour être admis

try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide.")
    exit(1)

if note >= seuil:
    print("Admis")
    if note == 20 :
       print("excellent ")
        
    elif note >= 16 :
      print ("tres bien")
    elif note >15 :
      print ("bien")
    elif note >= 12 :
      print (" assez bien")
    elif note >=10 :
     print ("passable") 
elif note <0 or note > 20 :
    print ("note invalide")
else:
    print("Refusé")
    if note >=7 :
         print ("tu peux passer l'examen de rattrapage")
         
mot_cle = "stop"
message = ""

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")
    if message.lower() != mot_cle:
        print(f"Vous avez saisi : {message}")

print("Boucle terminée, mot-clé détecté.")
for i in range(1, 6):  # va de 1 inclus à 6 exclu
    print(f"Nombre {i}")
fruits = ["pomme", "banane", "cerise"]

for index, fruit in enumerate(fruits):
    print(f"{index} → {fruit}")