def distance_toilettes(marches, hauteur):
    hauteur_m = hauteur / 100  
    distance_jour = marches * hauteur_m * 5  
    distance_semaine = distance_jour * 7  
    return round(distance_semaine, 2)  
marches = 50
hauteur = 20
distance = distance_toilettes(marches, hauteur)
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance} m par semaine.")