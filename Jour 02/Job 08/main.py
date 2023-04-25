def afficher_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
afficher_aliments("fruits","hiver")
afficher_aliments("fruits", "ete")
afficher_aliments("legume","hiver")
afficher_aliments("legume","ete")
