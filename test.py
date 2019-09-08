def dialogue(nom_personnage, message):
    print("{} : {}".format(nom_personnage, message))
def choix(nom_personnagec, messagec):
    input("{} : {}".format(nom_personnagec, messagec))

print("Bienvenue au cinéma Dooji Cinema, veuillez commander votre ticket et n'hésitez pas à faire un tour vers de quoi manger, boire")
dialogue("Stella", "Bonjour je me nomme Stella je suis la personne qui travail au cinéma")
dialogue("Vous", "Ok, merci beaucoup")
dialogue("Stella", "Pour les tickets, soit c'est un par un ou on a des formules comme groupe pour 5 personnes, soit étudiant moins chère.")

age = int(input("Quel est votre âge ?"))

    
if age <= 18:
    print("Vous êtes étudiant donc votre place coûte 6.5 euros")
    prix_total = 6.5
    
elif age > 18:
    print("Vous êtes adulte, si vous êtes plus de 5 personnes prenez un forfait groupe sinon si vous êtes seul prenez 1 ticket")
    prix_total = 12.5
    
    
forfait = input("Forfait groupe (5 personnes) ou un ticket (1 seul personne)")

if forfait == "un ticket":
    print("Vous avez acheté un ticket donc cela fais {} euros".format(prix_total))
    print(prix_total)
    
elif forfait == "forfait groupe":
    print("Vous avez acheté un forfait de groupe cela fait 12.5 euros de plus")
    prix_total += 12.5
    print(prix_total)
    
else:
    print("Avez-vous bien mis un ticket ou forfait groupe on prend donc un seul ticket du coup !")
    
    
manger = input("Voulez-vous manger ?")

if manger == "oui":
    print("Merci je vais vous dire les différents aliments !")
    print("On a des chips, popcorn, bonbon et chocolat que voulez-vous ?")

mange = input(">  ")

if mange == "chocolat":
    print("Vous avez pris du chocolat lequel voulez-vous entre Lion, Kit-Kat et Crunch ?")
    mange = input(">  ")

if mange == "Crunch":
    print("Vous avez pris du Crunch cela fait 2.5 euros de plus")
    prix_total += 2.5
    print("Voulez-vous autre chose ?")
    mange = input(">  ")
    
if mange == "Kit-Kat":
    print("Vous avez pris du Kit-Kat cela fait 2.5 euros de plus")
    print("Voulez-vous autre chose ?")
    prix_total += 2.5
    mange = input(">  ")
    
if mange == "Lion":
    print("Vous avez pris du Kit-Kat cela fait 1.5 euros de plus")
    print("Voulez-vous autre chose ?")
    prix_total += 1.5
    mange = input(">  ")
    
if mange == "chips":
    print("Voici votre paquet de chips on a que barbecue revenez à la version 3 cela vous fait 4.5 euros en plus !")
    print("Voulez-vous autre chose ?")
    prix_total += 4.5
    mange = input(">  ")
    
if mange == "bonbon":
    print("Vous voulez quoi Dragibus, Tagada, Chupa-Chups")
    mange = input(">  ")
    
if mange == "Dragibus":
    print("Voilà vos Dragibus cela vous fait 1.50 euros en plus")
    print("Voulez-vous autre chose ?")
    prix_total += 1.5

if mange == "Tagada":
    print("Voilà vos Tagada cela vous fait 1.50 euros en plus")
    print("Voulez-vous autre chose ?")
    prix_total += 1.5
    mange = input(">  ")
    
if mange == "Chupa-Chups":
    print("Voilà votre sucette à la fraise pour plus de goût revenez à la version 3 cela vous fait 1.50 euros en plus")
    print("Voulez-vous autre chose ?")
    prix_total += 1.5
    mange = input(">  ")
    
if mange == "popcorn":
    print("Voilà vos popcorn petit cela vous fait 3.5 euros en plus, revenez à la V3 pour avoir différentes tailles de popcorn")
    prix_total += 3.5

if manger == "oui":
    print("Cet option n'est pas disponible pour le moment revenez à la version 3 !")
    
if manger == "non":
    print("Pas grave passons aux boissons !")

boire = input("Voulez-vous boire ?")

if boire == "oui":
    print("Voici les boissons : Fanta, Coca-Cola, Seven Up, Oasis, Ice Tea, Orangina.")
    mange = input(">  ")
    
if mange == "Fanta":
    print("Voici votre Fanta orange cela fera 2.50 euros de plus, plus de Fanta disponible dans la V3")
    prix_total += 2.5
    
if mange == "Coca-Cola":
    print("Voici votre Coca-Cola cela fera 2.50 euros de plus, plus de Coca-Cola disponible dans la V3")
    prix_total += 2.5
    
if mange == "Seven Up":
    print("Voici votre Seven Up cela fera 2.50 euros de plus, plus de Seven Up disponible dans la V3")
    prix_total += 2.5
    
if mange == "Oasis":
    print("Voici votre Oasis cela fera 2.50 euros de plus, plus de Oasis disponible dans la V3")
    prix_total += 2.5
    
if mange == "Ice Tea":
    print("Voici votre Ice Tea cela fera 2.50 euros de plus, plus de Ice Tea disponible dans la V3")
    prix_total += 2.5
    
if mange == "Orangina":
    print("Voici votre Orangina cela fera 2.50 euros de plus, plus de Orangina disponible dans la V3")
    prix_total += 2.5
    
if boire == "non":
    print("Tant pis !")
    
print("Merci beaucoup, bonne séance à vous !")
    
print(prix_total)

print("Le prix du tout vous fera comme indiqué sur la machine {} euros".format(prix_total))
    
    
    
    

    
