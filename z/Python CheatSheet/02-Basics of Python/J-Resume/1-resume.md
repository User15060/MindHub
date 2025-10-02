# Programmation Python

## Types de variables

* `a = "Bonjour"` → chaîne de caractères (`str`)
* `b = 5` → nombre entier (`int`)
* `c = 1.5` → nombre à virgule (`float`)
* `d = True` → booléen (`bool`)

---

## Print et Input

```python
nom = input("Quel est votre nom ?")
print("Vous vous appelez " + nom)          # concaténation
print(f"Vous vous appelez {nom}")          # f-string
print("Vous vous appelez %s" % nom)        # ancien format
```

---

## Commentaires

* Commentaire sur une ligne : `# ...`
* Commentaire sur plusieurs lignes :

```python
"""
Texte
sur
plusieurs lignes
"""
```

---

## Conversions

```python
age = 30
print("Votre âge est : " + str(age))   # int → str

age_str = "30"
age_int = int(age_str)                 # str → int
# Utiliser try/except pour gérer les erreurs
```

---

## Boucle While

Boucle exécutée tant que la condition est vraie.

```python
nom = ""
while nom == "":
    nom = input("Quel est votre nom ?")
```

---

## Boucle For

Boucle exécutée un certain nombre de fois.

```python
for i in range(0, 4):   # 0, 1, 2, 3
    print(i)
```

---

## Fonctions

Définition et appel :

```python
def afficher_informations_personne(nom, age, taille=0):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

afficher_informations_personne("Jean", 25)
```

* `return` permet de renvoyer une valeur ou de quitter la fonction.

---

## Conditions

Opérateurs :

* `==` égal
* `<=` inférieur ou égal
* `<` inférieur
* `>=` supérieur ou égal
* `>` supérieur

Exemple :

```python
if age == 17:
    print("Vous êtes presque majeur")
elif 12 <= age < 18:
    print("Vous êtes adolescent")
elif age == 1 or age == 2:
    print("Vous êtes un bébé")
elif age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
```

---

## Exceptions

Gestion des erreurs avec `try/except` :

```python
try:
    age_int = int(age_str)
except:
    print("ERREUR : Vous devez entrer un nombre pour l'âge")
```
