seuil = 10
notes = []

def saisir_notes():
 compteur = 0
 while compteur <10 :
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree)
        notes.append(note)
       
    except ValueError:
        print ("saisie invalide veuillez reessayer")
        continue
    compteur +=1

saisir_notes()
print(f"{notes}")
for index, note in enumerate(notes, start=1):
    statut = "Admis" if note >= seuil else "Refusé"
    print(f"Étudiant {index} : note {note} → {statut}")

moyenne = sum(notes ) / len (notes )if notes !=[]else 0
print (f"la moyenne globale est de : {moyenne }")
if moyenne >= seuil :
    print ("admis")
    if moyenne >=19 :
        print ("exellent ")
    elif moyenne >= 16 :
        print (" trres bien ")
    elif moyenne >= 14  :
        print ("bien ")
    elif moyenne >= 12 :
        print("asssez bien")
    elif moyenne >= 10 :
        print ("passable ")
    else :
        print ("moyenne = 0")
else :
    print("refuse")