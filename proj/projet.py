import time
from fltk import *
import random
import os
from PIL import Image #pip install pillow
import copy
import pygame #pip install pygame


dico_age = {
    "âge_primitif":{
        "pv_base_ultime": [1000,1000],
        "frappe_aerienne":50,
        "nombre_frappe_aerienne":7,
        "cout_frappe_aerienne":2000,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[7000,"âge_antique"],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 100,
                "degats": 15,
                "vitesse_de_frappe": 0.15,
                "vitesse_de_marche": 0.04,
                "portee": 2,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 130,
                "cout_exp": 130,
                "joueur": None,
                "pos":None,
                "age":"âge_primitif"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 130,
                "degats": 15,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.04,
                "portee": 20,
                "temps_construction": 0.8,
                "taille":6,
                "cout_or": 160,
                "cout_exp": 160,
                "joueur": None,
                "pos":None,
                "age":"âge_primitif"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 175,
                "degats": 40,
                "vitesse_de_frappe": 0.5,
                "vitesse_de_marche": 0.2,
                "portee": 2,
                "temps_construction": 2,
                "taille":10,
                "cout_or": 180,
                "cout_exp": 180,
                "joueur": None,
                "pos":None,
                "age":"âge_primitif"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 350,
                "degats": 45,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.2,
                "portee": 20,
                "temps_construction": 3,
                "taille":20,
                "cout_or": 300,
                "cout_exp": 300,
                "joueur": None,
                "pos":None,
                "age":"âge_primitif"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 315,
                "degats": 30,
                "vitesse_frappe": 0.5,
                "portee": 50,
                "age":"âge_primitif"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 480,
                "degats": 50,
                "vitesse_frappe": 0.8,
                "portee": 40,
                "age":"âge_primitif"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 420,
                "degats": 40,
                "vitesse_frappe": 0.7,
                "portee": 45,
                "age":"âge_primitif"
            }
        }
    },
    "âge_antique":{
        "pv_base_ultime": [1500,1500],
        "frappe_aerienne":100,
        "nombre_frappe_aerienne":9,
        "cout_frappe_aerienne":3000,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[8500,"âge_médiéval"],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 110,
                "degats": 15,
                "vitesse_de_frappe": 0.3,
                "vitesse_de_marche": 0.04,
                "portee": 2,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 130,
                "cout_exp": 130,
                "joueur": None,
                "pos":None,
                "age":"âge_antique"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 160,
                "degats": 30,
                "vitesse_de_frappe": 0.1,
                "vitesse_de_marche": 0.04,
                "portee": 25,
                "temps_construction": 1.5,
                "taille":7,
                "cout_or": 160,
                "cout_exp": 160,
                "joueur": None,
                "pos":None,
                "age":"âge_antique"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 200,
                "degats": 35,
                "vitesse_de_frappe": 0.3,
                "vitesse_de_marche": 0.2,
                "portee": 2,
                "temps_construction": 2,
                "taille":6,
                "cout_or": 180,
                "cout_exp": 180,
                "joueur": None,
                "pos":None,
                "age":"âge_antique"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 300,
                "degats": 35,
                "vitesse_de_frappe": 0.08,
                "vitesse_de_marche": 0.04,
                "portee": 2,
                "temps_construction": 1,
                "taille":20,
                "cout_or": 250,
                "cout_exp": 250,
                "joueur": None,
                "pos":None,
                "age":"âge_antique"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 500,
                "degats": 50,
                "vitesse_frappe": 0.5,
                "portee": 50,
                "age":"âge_antique"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 600,
                "degats": 65,
                "vitesse_frappe": 0.8,
                "portee": 40,
                "age":"âge_antique"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 715,
                "degats": 50,
                "vitesse_frappe": 0.9,
                "portee": 50,
                "age":"âge_antique"
            }
        }
    },
    "âge_médiéval":{
        "pv_base_ultime": [2000,2000],
        "frappe_aerienne":150,
        "nombre_frappe_aerienne":11,
        "cout_frappe_aerienne":4000,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[9000,"âge_militaire"],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 150,
                "degats": 15,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.1,
                "portee": 2,
                "temps_construction": 0.8,
                "taille":6,
                "cout_or": 140,
                "cout_exp": 140,
                "joueur": None,
                "pos":None,
                "age":"âge_médiéval"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 150,
                "degats": 35,
                "vitesse_de_frappe": 0.08,
                "vitesse_de_marche": 0.08,
                "portee": 25,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 165,
                "cout_exp": 165,
                "joueur": None,
                "pos":None,
                "age":"âge_médiéval"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 210,
                "degats": 40,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.05,
                "portee": 30,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 170,
                "cout_exp": 170,
                "joueur": None,
                "pos":None,
                "age":"âge_médiéval"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 400,
                "degats": 40,
                "vitesse_de_frappe": 0.3,
                "vitesse_de_marche": 0.2,
                "portee": 20,
                "temps_construction": 3,
                "taille":6,
                "cout_or": 280,
                "cout_exp": 280,
                "joueur": None,
                "pos":None,
                "age":"âge_médiéval"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 650,
                "degats": 65,
                "vitesse_frappe": 0.4,
                "portee": 50,
                "age":"âge_médiéval"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 700,
                "degats": 100,
                "vitesse_frappe": 0.7,
                "portee": 40,
                "age":"âge_médiéval"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 800,
                "degats": 80,
                "vitesse_frappe": 0.4,
                "portee": 45,
                "age":"âge_médiéval"
            }
        }
    },
    "âge_militaire":{
        "pv_base_ultime": [2500,2500],
        "frappe_aerienne":160,
        "nombre_frappe_aerienne":12,
        "cout_frappe_aerienne":4500,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[10000,"âge_apocalypse"],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 140,
                "degats": 30,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.1,
                "portee": 2,
                "temps_construction": 0.8,
                "taille":6,
                "cout_or": 120,
                "cout_exp": 120,
                "joueur": None,
                "pos":None,
                "age":"âge_militaire"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 160,
                "degats": 40,
                "vitesse_de_frappe": 0.1,
                "vitesse_de_marche": 0.2,
                "portee": 30,
                "temps_construction": 2,
                "taille":6,
                "cout_or": 160,
                "cout_exp": 160,
                "joueur": None,
                "pos":None,
                "age":"âge_militaire"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 250,
                "degats": 50,
                "vitesse_de_frappe": 0.5,
                "vitesse_de_marche": 0.1,
                "portee": 20,
                "temps_construction": 2.5,
                "taille":10,
                "cout_or": 250,
                "cout_exp": 250,
                "joueur": None,
                "pos":None,
                "age":"âge_militaire"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 450,
                "degats": 50,
                "vitesse_de_frappe": 0.3,
                "vitesse_de_marche": 0.1,
                "portee": 35,
                "temps_construction": 3,
                "taille":20,
                "cout_or": 320,
                "cout_exp": 320,
                "joueur": None,
                "pos":None,
                "age":"âge_militaire"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 1000,
                "degats": 70,
                "vitesse_frappe": 0.6,
                "portee": 55,
                "age":"âge_militaire"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 1200,
                "degats": 60,
                "vitesse_frappe": 0.4,
                "portee": 50,
                "age":"âge_militaire"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 1400,
                "degats": 80,
                "vitesse_frappe": 0.7,
                "portee": 50,
                "age":"âge_militaire"
            }
        }
    },
    "âge_apocalypse":{
        "pv_base_ultime": [3000,3000],
        "frappe_aerienne":210,
        "nombre_frappe_aerienne":13,
        "cout_frappe_aerienne":5000,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[11000,"âge_futur"],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 200,
                "degats": 25,
                "vitesse_de_frappe": 0.1,
                "vitesse_de_marche": 0.04,
                "portee": 2,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 130,
                "cout_exp": 130,
                "joueur": None,
                "pos":None,
                "age":"âge_apocalypse"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 210,
                "degats": 45,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.2,
                "portee": 40,
                "temps_construction": 2,
                "taille":6,
                "cout_or": 200,
                "cout_exp": 200,
                "joueur": None,
                "pos":None,
                "age":"âge_apocalypse"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 275,
                "degats": 45,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.05,
                "portee": 2,
                "temps_construction": 1,
                "taille":6,
                "cout_or": 200,
                "cout_exp": 200,
                "joueur": None,
                "pos":None,
                "age":"âge_apocalypse"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 450,
                "degats": 45,
                "vitesse_de_frappe": 0.3,
                "vitesse_de_marche": 0.1,
                "portee": 40,
                "temps_construction": 3,
                "taille":20,
                "cout_or": 350,
                "cout_exp": 350,
                "joueur": None,
                "pos":None,
                "age":"âge_apocalypse"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 1600,
                "degats": 80,
                "vitesse_frappe": 0.7,
                "portee": 30,
                "age":"âge_apocalypse"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 1800,
                "degats": 110,
                "vitesse_frappe": 0.4,
                "portee": 30,
                "age":"âge_apocalypse"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 2000,
                "degats": 120,
                "vitesse_frappe": 0.6,
                "portee": 40,
                "age":"âge_apocalypse"
            }
        }
    },
    "âge_futur":{
        "pv_base_ultime": [3500,3500],
        "frappe_aerienne":300,
        "nombre_frappe_aerienne":15,
        "cout_frappe_aerienne":6000,
        "recharge_frappe_aerienne":[45,0],
        "cout_evolution":[0,None],
        "or_recolte":1,
        "exp_recolte":1,
        "amelioration":[300,[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000],[300,400,600,1000,2000]],
        "unites":{
            "infanterie": {
                "type_unite": "infanterie",
                "points_de_vie": 220,
                "degats": 50,
                "vitesse_de_frappe": 0.1,
                "vitesse_de_marche": 0.04,
                "portee": 2,
                "temps_construction": 1,
                "taille":12,
                "cout_or": 150,
                "cout_exp": 150,
                "joueur": None,
                "pos":None,
                "age":"âge_futur"
            },
            "soutien": {
                "type_unite": "soutien",
                "points_de_vie": 250,
                "degats": 55,
                "vitesse_de_frappe": 0.08,
                "vitesse_de_marche": 0.08,
                "portee": 45,
                "temps_construction": 1.5,
                "taille":6,
                "cout_or": 170,
                "cout_exp": 170,
                "joueur": None,
                "pos":None,
                "age":"âge_futur"
            },
            "anti_blindage": {
                "type_unite": "anti_blindage",
                "points_de_vie": 300,
                "degats": 70,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.1,
                "portee": 30,
                "temps_construction": 3,
                "taille":20,
                "cout_or": 300,
                "cout_exp": 300,
                "joueur": None,
                "pos":None,
                "age":"âge_futur"
            },
            "lourd": {
                "type_unite": "lourd",
                "points_de_vie": 475,
                "degats": 70,
                "vitesse_de_frappe": 0.2,
                "vitesse_de_marche": 0.1,
                "portee": 45,
                "temps_construction": 3,
                "taille":10,
                "cout_or": 400,
                "cout_exp": 400,
                "joueur": None,
                "pos":None,
                "age":"âge_futur"
            }
        },
        "cout_tourelle":[150,300,400,600],
        "tourelles":{
            "tourelle_canon": {
                "type_tourelle":"tourelle_canon",
                "prix": 2200,
                "degats": 50,
                "vitesse_frappe": 0.7,
                "portee": 50,
                "age":"âge_futur"
            },
            "tourelle_missile": {
                "type_tourelle":"tourelle_missile",
                "prix": 2400,
                "degats": 60,
                "vitesse_frappe": 0.7,
                "portee": 50,
                "age":"âge_futur"
            },
            "tourelle_fleche": {
                "type_tourelle":"tourelle_fleche",
                "prix": 3000,
                "degats": 85,
                "vitesse_frappe": 1,
                "portee": 50,
                "age":"âge_futur"
            }
        }
    },
}






def achat_unite(type_unite,joueur,Or,joueur_age,Age,liste_attente):
    """Cette fonction prend en argument le type de l'unite qu'on veut acheter,le joueur qui l'achete,l'Or des joueurs,l'Age des joueurs, et la liste des unités en attente.
       En effet cette fonction soustrait le cout de l'unité au joueur qui l'a payer. Cette fonction ne renvoie rien."""
    if Or[joueur]>=joueur_age[joueur][Age[joueur]]["unites"][type_unite]["cout_or"]:
        Or[joueur]-=joueur_age[joueur][Age[joueur]]["unites"][type_unite]["cout_or"]
        liste_attente[joueur].append(copy.deepcopy(joueur_age[joueur][Age[joueur]]["unites"][type_unite]))
        liste_attente[joueur][-1]["joueur"]=joueur

def combat_verif(liste_terrain,joueur_age):
    """Cette fonction prend en argument la liste de toutes les cases du terrain, ainsi que la liste joueur_age qui comporte toutes les statistiques des deux joueurs.
       En effet cette fonction parcours toutes les cases du terrains pour verifier si deux unité ennemis entre elles se retrouve face à face et renvoie la position de
       l'unité de gauche dans le face à face. S'il n'y a pas de face à face la fonction renvoie None."""
    for i in range(len(liste_terrain)-1):
        if (liste_terrain[i]!=None and liste_terrain[i]!=True) and (liste_terrain[i+1]!=None and liste_terrain[i+1]!=True):
            if liste_terrain[i]["joueur"]!=liste_terrain[i+1]["joueur"]:
                liste_terrain[i]["vitesse_de_frappe"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_frappe"]
                liste_terrain[i+1]["vitesse_de_frappe"]=joueur_age[liste_terrain[i+1]["joueur"]][liste_terrain[i+1]["age"]]["unites"][liste_terrain[i+1]["type_unite"]]["vitesse_de_frappe"]
                return i
    return None

def verif_projectile(liste_terrain,combattant,screen,liste_projectile,joueur_age,Or,Exp,Age,liste_unite_terrain,liste_objet):
    """Cette fonction prend en argument la liste de toutes les cases du terrain, la position du combattant de gauche dans le face à face à distance, la possition de l'ecran (0, 1 oo 2),
       la liste des projectile qui doivent etre afficher, la liste des deux dico correspondant à toutes les statistiques des deux joueurs, l'Or des deux joueurs, l'Exp des deux joueurs,
       l'Age des deux joueurs, la liste qui comporte le nombre d'unité par camp sur le terrain, et la liste objet qui comporte tout les tags des objets afficher sur l'ecran.
       En effet, cette fonction verifie si unité ennemi est placer dans la porté d'une unité. Dans ce cas la le projectile sera afficher avec la fonction anime_projectile. Et avec le temps de recharge,
       une fois qu'il sera à 0, l'unité attaquera a distance l'unité ennemi. Cette fonction ne renvoie rien."""
    for i in range(len(liste_terrain)-1):
        if combattant!=None and combattant!=True:   #verifie que l'unité ne fait pas partie d'un face à face car il y a deja la fonction combat qui s'occupe de cette configuration
            if i==combattant or i==combattant+1:
                continue
        if liste_terrain[i]!=None and liste_terrain[i]!=True:
            if liste_terrain[i]["joueur"]==0:  # verification pour toutes les unités du joueur 0
                for k in range(i+1,int(i+liste_terrain[i]["portee"]+1)):   # verification dans la porter de l'unité s'il y a une unité ennemi
                    if k>(len(liste_terrain)-1):  # verification pour attaquer la base ennemi
                        if i!=len(liste_terrain)-2:  #verification que l'unité se retrouve pas coller a la base ennemi
                            if liste_terrain[i]["vitesse_de_frappe"]<=0.1 and liste_terrain[i]["vitesse_de_frappe"]>0.08: # condition pour que 0.1s avant le coup, l'animation demarre ainsi que le bruitage de projectile
                                dico_son["son_projectile.ogg"].play()
                                liste_projectile.append([2,i,len(liste_terrain)-1,0,None])
                        if liste_terrain[i]["vitesse_de_frappe"]<=0: #lorsque la vitesse de frappe est à 0 c'est que l'unité peut attaquer
                            son_choix=random.choice([0,1])   # deux sons possible pour la mort de l'adversaire si c'est un humain ou alors 2 son pour les deux char du jeu
                            if son_choix==0:
                                dico_son["son_hit.ogg"].play()      
                            else:
                                dico_son["son_hit2.ogg"].play()
                            joueur_age[1][Age[1]]["pv_base_ultime"][0]-= liste_terrain[i]["degats"]
                            refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
                            liste_terrain[i]["vitesse_de_frappe"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_frappe"]
                        else:
                            liste_terrain[i]["vitesse_de_frappe"]-=0.02
                        break
                    if liste_terrain[k]!=None and liste_terrain[k]!=True:   # verification pour les unité ennemi se trouvant sur le terrain
                        if liste_terrain[i]["joueur"]!=liste_terrain[k]["joueur"]:
                            if liste_terrain[i]["vitesse_de_frappe"]<=0.1 and liste_terrain[i]["vitesse_de_frappe"]>0.08:
                                dico_son["son_projectile.ogg"].play()
                                liste_projectile.append([2,i,k,0,None]) # liste qui correspond a une logique pour retenir la position de l'adversaire et demarrer l'animation (joueur0(0,1) ou joueur1(1,2),tourelle,pose_cible,phase,co-projectile)
                            if liste_terrain[i]["vitesse_de_frappe"]<=0:
                                son_choix=random.choice([0,1])
                                if son_choix==0:
                                    dico_son["son_hit.ogg"].play()
                                else:
                                    dico_son["son_hit2.ogg"].play()
                                liste_terrain[k]["points_de_vie"]-= liste_terrain[i]["degats"]
                                if liste_terrain[k]["points_de_vie"]>0: # S'il lui reste de la vie on refresh la barre
                                    refresh_barre_de_vie(screen,liste_terrain,k,liste_objet,joueur_age)
                                liste_terrain[i]["vitesse_de_frappe"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_frappe"]
                                if liste_terrain[k]["points_de_vie"]<=0:  # s'il n'a plus de vie alors nous le supprimons
                                    if liste_terrain[k]["type_unite"]=="lourd" and liste_terrain[k]["age"]=="âge_militaire":
                                        dico_son["son_mort_char2.ogg"].play()
                                    elif liste_terrain[k]["type_unite"]=="anti_blindage" and liste_terrain[k]["age"]=="âge_futur":
                                        dico_son["son_mort_char.ogg"].play()
                                    else:
                                        son_choix=random.choice([0,1,2])
                                        if son_choix==0:
                                            dico_son["son_mort.ogg"].play()
                                        if son_choix==1:
                                            dico_son["son_mort2.ogg"].play()
                                        if son_choix==2:
                                            dico_son["son_mort3.ogg"].play()
                                    Or[0]+=joueur_age[0][Age[0]]["or_recolte"]*liste_terrain[k]["cout_or"]   # gain or et exp qui correspond au cout de l'unité ennemis multiplier a notre coeff gain or exp
                                    Exp[0]+=joueur_age[0][Age[0]]["exp_recolte"]*liste_terrain[k]["cout_exp"]
                                    liste_unite_terrain[liste_terrain[k]["joueur"]]-=1
                                    for j in range(k,k+liste_terrain[k]["taille"]): # supprimer toute la "hit box" de l'unité morte
                                        if j >len(liste_terrain)-1:
                                            break
                                        liste_terrain[j]=None 
                            else:
                                liste_terrain[i]["vitesse_de_frappe"]-=0.02
                            break
            else: # meme chose pour les unité du joueur 1
                for k in range(i-1,int(i-liste_terrain[i]["portee"]-1),-1):
                    if k<0:
                        if i!=1:
                            if liste_terrain[i]["vitesse_de_frappe"]<=0.1 and liste_terrain[i]["vitesse_de_frappe"]>0.08:
                                dico_son["son_projectile.ogg"].play()
                                liste_projectile.append([3,i,0,0,None])
                        if liste_terrain[i]["vitesse_de_frappe"]<=0:
                            son_choix=random.choice([0,1])
                            if son_choix==0:
                                dico_son["son_hit.ogg"].play()
                            else:
                                dico_son["son_hit2.ogg"].play()
                            joueur_age[0][Age[0]]["pv_base_ultime"][0]-= liste_terrain[i]["degats"]
                            refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
                            liste_terrain[i]["vitesse_de_frappe"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_frappe"]
                        else:
                            liste_terrain[i]["vitesse_de_frappe"]-=0.02
                        break
                    if liste_terrain[k]!=None and liste_terrain[k]!=True:
                        if liste_terrain[i]["joueur"]!=liste_terrain[k]["joueur"]:
                            if liste_terrain[i]["vitesse_de_frappe"]<=0.1 and liste_terrain[i]["vitesse_de_frappe"]>0.08:
                                dico_son["son_projectile.ogg"].play()
                                liste_projectile.append([3,i,k,0,None]) #joueur,tourelle,pose_cible,phase,co-projectile
                            if liste_terrain[i]["vitesse_de_frappe"]<=0:
                                son_choix=random.choice([0,1])
                                if son_choix==0:
                                    dico_son["son_hit.ogg"].play()
                                else:
                                    dico_son["son_hit2.ogg"].play()
                                liste_terrain[k]["points_de_vie"]-= liste_terrain[i]["degats"]
                                if liste_terrain[k]["points_de_vie"]>0:
                                    refresh_barre_de_vie(screen,liste_terrain,k,liste_objet,joueur_age)
                                liste_terrain[i]["vitesse_de_frappe"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_frappe"]
                                if liste_terrain[k]["points_de_vie"]<=0:
                                    if liste_terrain[k]["type_unite"]=="lourd" and liste_terrain[k]["age"]=="âge_militaire":
                                        dico_son["son_mort_char2.ogg"].play()
                                    elif liste_terrain[k]["type_unite"]=="anti_blindage" and liste_terrain[k]["age"]=="âge_futur":
                                        dico_son["son_mort_char.ogg"].play()
                                    else:
                                        son_choix=random.choice([0,1,2])
                                        if son_choix==0:
                                            dico_son["son_mort.ogg"].play()
                                        if son_choix==1:
                                            dico_son["son_mort2.ogg"].play()
                                        if son_choix==2:
                                            dico_son["son_mort3.ogg"].play()
                                    Or[1]+=joueur_age[1][Age[1]]["or_recolte"]*liste_terrain[k]["cout_or"]
                                    Exp[1]+=joueur_age[1][Age[1]]["exp_recolte"]*liste_terrain[k]["cout_exp"]
                                    liste_unite_terrain[liste_terrain[k]["joueur"]]-=1
                                    for i in range(k-(liste_terrain[k]["taille"]-1),k+1):
                                        if i <0:
                                            break
                                        liste_terrain[i]=None
                            else:
                                liste_terrain[i]["vitesse_de_frappe"]-=0.02
                            break

def combat(liste_terrain,combattant,screen,liste_objet,joueur_age):
    """Cette fonction prend en argument la liste_terrain cité precedemment,combattant correspondant à la position de l'unité de gauche dans le face a face, la position de l'ecran dans screen,
       la liste des objet sur la fenetre, et la liste de dico joueur_age cité precedemment. Cette fonction verifie si les unités en face à face peuvent attaquer celui d'en face. Si une 
       unité meurt elle est supprimer de la liste_terrain. Cette fonction ne renvoie rien."""
    if liste_terrain[combattant]!=None and liste_terrain[combattant]!=True:
        if liste_terrain[combattant]["vitesse_de_frappe"]<=0:
            son_choix=random.choice([0,1])
            if son_choix==0:
                dico_son["son_hit.ogg"].play()
            else:
                dico_son["son_hit2.ogg"].play()
            if liste_terrain[combattant]["joueur"]==0:
                liste_terrain[combattant+1]["points_de_vie"]-= liste_terrain[combattant]["degats"]
                if liste_terrain[combattant+1]["points_de_vie"]>0:
                    refresh_barre_de_vie(screen,liste_terrain,combattant+1,liste_objet,joueur_age)
            else:
                liste_terrain[combattant-1]["points_de_vie"]-= liste_terrain[combattant]["degats"]
                if liste_terrain[combattant-1]["points_de_vie"]>0:
                    refresh_barre_de_vie(screen,liste_terrain,combattant-1,liste_objet,joueur_age)
            liste_terrain[combattant]["vitesse_de_frappe"]=joueur_age[liste_terrain[combattant]["joueur"]][liste_terrain[combattant]["age"]]["unites"][liste_terrain[combattant]["type_unite"]]["vitesse_de_frappe"]
        liste_terrain[combattant]["vitesse_de_frappe"]-=0.02

def result_combat(liste_terrain,combattant,liste_unite_terrain,Or,Exp,joueur_age,Age):
    """Cette fonction prend en argument la liste_terrain, le combattant positionner à gauche dans le face a face, la liste_unite_terrain correspondant
       au nombre d'unité du joueur 0 et du joueur 1 sur le terrain, l'Or des deux joueurs, leurs Exp, leurs Age et la liste de dico joueur_age.
       En effet, cette fonction sert à verifier s'il y a un vainqueur ou deux mort lors d'un combat pour pouvoir l'arreter. Cette fonction renvoie
       1 si le combat est terminé, 0 sinon."""
    if liste_terrain[combattant]["points_de_vie"]<=0:
        if liste_terrain[combattant]["type_unite"]=="lourd" and liste_terrain[combattant]["age"]=="âge_militaire":
            dico_son["son_mort_char2.ogg"].play()
        elif liste_terrain[combattant]["type_unite"]=="anti_blindage" and liste_terrain[combattant]["age"]=="âge_futur":
            dico_son["son_mort_char.ogg"].play()
        else:
            son_choix=random.choice([0,1,2])
            if son_choix==0:
                dico_son["son_mort.ogg"].play()
            if son_choix==1:
                dico_son["son_mort2.ogg"].play()
            if son_choix==2:
                dico_son["son_mort3.ogg"].play()
        Or[1]+=joueur_age[1][Age[1]]["or_recolte"]*liste_terrain[combattant]["cout_or"]
        Exp[1]+=joueur_age[1][Age[1]]["exp_recolte"]*liste_terrain[combattant]["cout_exp"]
        liste_unite_terrain[liste_terrain[combattant]["joueur"]]-=1
        for i in range(combattant-(liste_terrain[combattant]["taille"]-1),combattant+1): # supprime la "hit box" de l'unité mort
            if i <0:
                continue
            liste_terrain[i]=None
    if liste_terrain[combattant+1]["points_de_vie"]<=0:
        if liste_terrain[combattant+1]["type_unite"]=="lourd" and liste_terrain[combattant+1]["age"]=="âge_militaire":
            dico_son["son_mort_char2.ogg"].play()
        elif liste_terrain[combattant+1]["type_unite"]=="anti_blindage" and liste_terrain[combattant+1]["age"]=="âge_futur":
            dico_son["son_mort_char.ogg"].play()
        else:
            son_choix=random.choice([0,1,2])
            if son_choix==0:
                dico_son["son_mort.ogg"].play()
            if son_choix==1:
                dico_son["son_mort2.ogg"].play()
            if son_choix==2:
                dico_son["son_mort3.ogg"].play()
        Or[0]+=joueur_age[0][Age[0]]["or_recolte"]*liste_terrain[combattant+1]["cout_or"]
        Exp[0]+=joueur_age[0][Age[0]]["exp_recolte"]*liste_terrain[combattant+1]["cout_exp"]
        liste_unite_terrain[liste_terrain[combattant+1]["joueur"]]-=1
        for j in range(combattant+1,(combattant+1)+liste_terrain[combattant+1]["taille"]):  # supprime la "hit box" de l'unité morte
            if j >len(liste_terrain)-1:
                break
            liste_terrain[j]=None
    if liste_terrain[combattant]==None or liste_terrain[combattant+1]==None: # la verification de si l'une des deux unité ou les deux sont morte pour pouvoir arreter le combat
        return 1
    return 0
    
def verif_pose(liste_attente,liste_terrain,liste_unite_terrain):
    """Cette fonction prend comme argument la liste des unités en attente, la liste des cases du terrain, la liste comportant le nombre d'unité
    du joueur0 et du joueur1. En effet cette fonction sert à verifier si une unité prete à etre poser sur le terrain à assez de place. Cette fonction
    est detailler dans les commentaires et ne renvoie rien."""
    pose,pose2=True,True
    if liste_unite_terrain[0]<10: # max de 10 unités sur le terrain
        if len(liste_attente[0])>0:
            if liste_attente[0][0]["temps_construction"]<=0:
                for i in range(liste_attente[0][0]["taille"]): # la variable pose devient False s'il y a pas assez de place pour l'unité d'etre poé
                    if liste_terrain[i]!=None:
                        pose=False
                if pose==False:  # s'il n'y a pas assez de place alors on verifie si la position 0 est vide pour pouvoir defendre la base si oui alors l'unité est poser meme si sa "hit box" est plus grande
                    if liste_terrain[0]==None:
                        liste_terrain[0]=liste_attente[0][0]
                        liste_terrain[0]["pose"]=0
                        liste_attente[0].pop(0)
                        liste_unite_terrain[0]+=1
                if pose==True: # sinon l'unite est simplement poser
                    for k in range(liste_attente[0][0]["taille"]-1):
                        liste_terrain[k]=True
                    liste_terrain[liste_attente[0][0]["taille"]-1]=liste_attente[0][0]
                    liste_terrain[liste_attente[0][0]["taille"]-1]["pose"]=liste_attente[0][0]["taille"]-1
                    liste_attente[0].pop(0)
                    liste_unite_terrain[0]+=1
    if liste_unite_terrain[1]<10: # meme chose pour la liste attente coté joueur 1
        if len(liste_attente[1])>0:
            if liste_attente[1][0]["temps_construction"]<=0:
                for j in range(-(liste_attente[1][0]["taille"]),0):
                    if liste_terrain[j]!=None:
                        pose2=False
                if pose2==False:
                    if liste_terrain[-1]==None:
                        liste_terrain[-1]=liste_attente[1][0]
                        liste_terrain[-1]["pose"]=len(liste_terrain)-1
                        liste_attente[1].pop(0)
                        liste_unite_terrain[1]+=1
                if pose2==True:
                    for l in range(-(liste_attente[1][0]["taille"])+1,0):
                        liste_terrain[l]=True
                    liste_terrain[-(liste_attente[1][0]["taille"])]=liste_attente[1][0]
                    liste_terrain[-(liste_attente[1][0]["taille"])]["pose"]=len(liste_terrain)-(liste_attente[1][-1]["taille"])
                    liste_attente[1].pop(0)
                    liste_unite_terrain[1]+=1

def temps_maj(liste_attente,liste_terrain,liste_unite_terrain,joueur_age,Age,liste_objet,screen):
    """Cette fonction prend en argument, la liste des unité en attente, la liste des cases du terrain, la loste du nombre d'unité des deux joueurs, le dico
       des deux joueurs expliquer precedemment, l'Age des deux joueurs, la liste des objets afficher sur la fenetre et la position de l'ecran.
       En effet cette fonction met a jour le temps par cran de 0.02s. Elle soustrait cette intervales à toutes les statistiques de temps de chargement.
       Cette fonction ne renvoie rien"""
    if len(liste_attente[0])>0:
        if liste_attente[0][0]["temps_construction"]>0:
            liste_attente[0][0]["temps_construction"]-=0.02
        else:
            verif_pose(liste_attente,liste_terrain,liste_unite_terrain)
    if len(liste_attente[1])>0:
        if liste_attente[1][0]["temps_construction"]>0:
            liste_attente[1][0]["temps_construction"]-=0.02
        else:
            verif_pose(liste_attente,liste_terrain,liste_unite_terrain)
    for i in range (len(liste_terrain)):
        if liste_terrain[i]!=None and liste_terrain[i]!=True:
            if (liste_terrain[i]["joueur"]==0 and (i==(len(liste_terrain)-1) or liste_terrain[i+1]!=None)) or (liste_terrain[i]["joueur"]==1 and (i==0 or liste_terrain[i-1]!=None)):
                liste_terrain[i]["vitesse_de_marche"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_marche"]
            liste_terrain[i]["vitesse_de_marche"]-=0.02
            if liste_terrain[i]["points_de_vie"]>0:
                refresh_barre_de_vie(screen,liste_terrain,i,liste_objet,joueur_age)
            if liste_terrain[i]["points_de_vie"]<=0:
                if liste_terrain[i]["type_unite"]=="lourd" and liste_terrain[i]["age"]=="âge_militaire":
                    dico_son["son_mort_char2.ogg"].play()
                elif liste_terrain[i]["type_unite"]=="anti_blindage" and liste_terrain[i]["age"]=="âge_futur":
                    dico_son["son_mort_char.ogg"].play()
                else:
                    son_choix=random.choice([0,1,2])
                    if son_choix==0:
                        dico_son["son_mort.ogg"].play()
                    if son_choix==1:
                        dico_son["son_mort2.ogg"].play()
                    if son_choix==2:
                        dico_son["son_mort3.ogg"].play()
                if liste_terrain[i]["joueur"]==1:
                    for k in range(i,i+liste_terrain[i]["taille"]):
                        if k >len(liste_terrain)-1:
                            break
                        liste_terrain[k]=None
                if liste_terrain[i]["joueur"]==0:
                    for l in range(i-(liste_terrain[i]["taille"]-1),i+1):
                        if l <0:
                            break
                        liste_terrain[l]=None
    if joueur_age[0][Age[0]]["recharge_frappe_aerienne"][1]>0:
        joueur_age[0][Age[0]]["recharge_frappe_aerienne"][1]-=0.02
    if joueur_age[1][Age[1]]["recharge_frappe_aerienne"][1]>0:
        joueur_age[1][Age[1]]["recharge_frappe_aerienne"][1]-=0.02

def verfication_deplacement(liste_terrain,joueur_age):
    """Cette fonction prend en argument la liste des cases du terrain et la liste des deux dico des deux joueurs.
       En effet cette fonction verifie s'il est possible pour une unité d'avancer. Cette fonction ne renvoie rien"""
    for i in range(len(liste_terrain)):
        if liste_terrain[i]!=None and liste_terrain[i]!=True:
            if liste_terrain[i]["vitesse_de_marche"]<=0:
                liste_terrain[i]["vitesse_de_marche"]=joueur_age[liste_terrain[i]["joueur"]][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["vitesse_de_marche"]
                if liste_terrain[i]["joueur"]==0 and i!=(len(liste_terrain)-2):
                    if liste_terrain[i+1]==None:
                        liste_terrain[i+1]= copy.deepcopy(liste_terrain[i])
                        liste_terrain[i+1]["pose"]=i+1
                        if i-(liste_terrain[i]["taille"]-1)>=0:
                            liste_terrain[i-(liste_terrain[i]["taille"]-1)]=None
                        for j in range(i-(liste_terrain[i+1]["taille"]-2),i+1):
                            if j<0:
                                continue
                            liste_terrain[j]=True
                else:
                    if liste_terrain[i]["joueur"]==1 and i!=1:
                        if liste_terrain[i-1]==None:
                            liste_terrain[i-1]= copy.deepcopy(liste_terrain[i])
                            liste_terrain[i-1]["pose"]=i-1
                            if i+(liste_terrain[i-1]["taille"]-1)<=len(liste_terrain)-1:
                                liste_terrain[i+(liste_terrain[i-1]["taille"]-1)]=None
                            for j in range(i,i+(liste_terrain[i-1]["taille"]-1)):
                                if j>len(liste_terrain)-1:
                                    continue
                                liste_terrain[j]=True

def verif_tourelle(liste_terrain,liste_tourelle,screen,liste_projectile,Age,Or,Exp,joueur_age,liste_objet,liste_unite_terrain):
    """Cette fonction prend en argument beaucoup de liste vu precedemment et la liste_tourelle qui comporte toutes les tourelles que possede les joueurs.
       En effet cette fonction verifie si dans la porté des tourelles se trouve des ennemies dans quel cas elles tirent dessus. Cette fonction ne renvoie rien"""
    for p in range(4): # pour les quatre emplacement possible de tourelle
        if liste_tourelle[0][p]!=None: # pour le joueur 0
            for i in range(1,int(liste_tourelle[0][p]["portee"]+1)): # verifie toutes les cases dans la porté de la tourelle
                if liste_terrain[i]!=None and liste_terrain[i]!=True:
                    if liste_terrain[i]["joueur"]!=0: # verifie dans le cas où c'est une unité appartenant au joueur 1
                        if liste_tourelle[0][p]["vitesse_frappe"]<=0.1 and liste_tourelle[0][p]["vitesse_frappe"]>0.08: # commence l'animation du projectile et le bruit du lancer
                            dico_son["son_projectile.ogg"].play()
                            liste_projectile.append([0,p,liste_terrain[i]["pose"],0,None]) # liste qui correspond a une logique pour retenir la position de l'adversaire et demarrer l'animation (joueur0(0,1) ou joueur1(1,2),tourelle,pose_cible,phase,co-projectile)
                        if liste_tourelle[0][p]["vitesse_frappe"]<=0:
                            liste_terrain[i]["points_de_vie"]-=liste_tourelle[0][p]["degats"] # fonction tres tres similaire à la fonction verif_projectile donc les commentaires decrivant l'algo se trouve la-bas
                            if liste_terrain[i]["points_de_vie"]>0:
                                refresh_barre_de_vie(screen,liste_terrain,i,liste_objet,joueur_age)
                            liste_tourelle[0][p]["vitesse_frappe"]=joueur_age[0][liste_tourelle[0][p]["age"]]["tourelles"][liste_tourelle[0][p]["type_tourelle"]]["vitesse_frappe"]
                            if liste_terrain[i]["points_de_vie"]<=0:
                                if liste_terrain[i]["type_unite"]=="lourd" and liste_terrain[i]["age"]=="âge_militaire":
                                    dico_son["son_mort_char2.ogg"].play()
                                elif liste_terrain[i]["type_unite"]=="anti_blindage" and liste_terrain[i]["age"]=="âge_futur":
                                    dico_son["son_mort_char.ogg"].play()
                                else:
                                    son_choix=random.choice([0,1,2])
                                    if son_choix==0:
                                        dico_son["son_mort.ogg"].play()
                                    if son_choix==1:
                                        dico_son["son_mort2.ogg"].play()
                                    if son_choix==2:
                                        dico_son["son_mort3.ogg"].play()
                                Or[0]+=joueur_age[0][Age[0]]["or_recolte"]*liste_terrain[i]["cout_or"]
                                Exp[0]+=joueur_age[0][Age[0]]["exp_recolte"]*liste_terrain[i]["cout_exp"]
                                liste_unite_terrain[liste_terrain[i]["joueur"]]-=1
                                for k in range(i,i+liste_terrain[i]["taille"]):
                                    if k >len(liste_terrain)-1:
                                        break
                                    liste_terrain[k]=None
                            break
                        else:
                            liste_tourelle[0][p]["vitesse_frappe"]-=0.02
                            break
    for q in range(4):   # pareille pour le joueur1
        if liste_tourelle[1][q]!=None:
            for i in range(-1,int(-(liste_tourelle[1][q]["portee"]+1)),-1):
                if liste_terrain[i]!=None and liste_terrain[i]!=True:
                    if liste_terrain[i]["joueur"]!=1:
                        if liste_tourelle[1][q]["vitesse_frappe"]<=0.1 and liste_tourelle[1][q]["vitesse_frappe"]>0.08:
                            dico_son["son_projectile.ogg"].play()
                            liste_projectile.append([1,q,liste_terrain[i]["pose"],0,None])
                        if liste_tourelle[1][q]["vitesse_frappe"]<=0:
                            liste_terrain[i]["points_de_vie"]-=liste_tourelle[1][q]["degats"]
                            if liste_terrain[i]["points_de_vie"]>0:
                                refresh_barre_de_vie(screen,liste_terrain,i,liste_objet,joueur_age)
                            liste_tourelle[1][q]["vitesse_frappe"]=joueur_age[1][liste_tourelle[1][q]["age"]]["tourelles"][liste_tourelle[1][q]["type_tourelle"]]["vitesse_frappe"]
                            if liste_terrain[i]["points_de_vie"]<=0:
                                if liste_terrain[i]["type_unite"]=="lourd" and liste_terrain[i]["age"]=="âge_militaire":
                                    dico_son["son_mort_char2.ogg"].play()
                                elif liste_terrain[i]["type_unite"]=="anti_blindage" and liste_terrain[i]["age"]=="âge_futur":
                                    dico_son["son_mort_char.ogg"].play()
                                else:
                                    son_choix=random.choice([0,1,2])
                                    if son_choix==0:
                                        dico_son["son_mort.ogg"].play()
                                    if son_choix==1:
                                        dico_son["son_mort2.ogg"].play()
                                    if son_choix==2:
                                        dico_son["son_mort3.ogg"].play()
                                Or[1]+=joueur_age[1][Age[1]]["or_recolte"]*liste_terrain[i]["cout_or"]
                                Exp[1]+=joueur_age[1][Age[1]]["exp_recolte"]*liste_terrain[i]["cout_exp"]
                                liste_unite_terrain[liste_terrain[i]["joueur"]]-=1
                                for l in range(i-(liste_terrain[i]["taille"]-1),i+1):
                                    if l <0:
                                        continue
                                    liste_terrain[l]=None
                            break
                        else:
                            liste_tourelle[1][q]["vitesse_frappe"]-=0.02
                            break

def fonction_meteorite(liste_meteorite,screen,liste_terrain,liste_objet_meteorite,Age,Or,Exp,joueur_age,liste_unite_terrain):
    """Cette fonction prend en argument la liste des meteorites qui doivent etre afficher, des parametres expliquer precedement, la liste_objet_meteorite
       correspondant a la liste contenant toutes les images de meteorite. En effet cette fonction sert à afficher une animation de meteorite qui tombe du ciel
       avec 50 frame espacer de 0.02s. Cette fonction retire de la vie au unité toucher par l'attaque. Cette fonction ne renvoie rien."""
    for elt in liste_objet_meteorite:
        while elt in liste_objet_meteorite:
            efface(elt)
            liste_objet_meteorite.remove(elt)
    for i in range(len(liste_meteorite)):
        if i==0:
            chemin=str('\\')+ str(Age[0]) + str('\\ ')
            chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
            chemin_fichier = os.path.join(chemin_courant, 'meteore.png')
        else:
            chemin=str('\\')+ str(Age[1]) + str('\\ ')
            chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
            chemin_fichier = os.path.join(chemin_courant, 'meteore.png')
        for j in range(len(liste_meteorite[i])):
            for k in range(len(liste_meteorite[i][j])):
                if screen==0:
                    image(420+(j*50+liste_meteorite[i][j][k][0]+5)*10,(((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1], chemin_fichier,largeur=150, hauteur=150,tag=str(420+(j*50+liste_meteorite[i][j][k][0]+5)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_objet_meteorite.append(str(420+(j*50+liste_meteorite[i][j][k][0]+5)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_meteorite[i][j][k]=(liste_meteorite[i][j][k][0],liste_meteorite[i][j][k][1]+1)
                if screen==1:
                    image((j*50+liste_meteorite[i][j][k][0]+5-55)*10,(((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1], chemin_fichier,largeur=150, hauteur=150,tag=str((j*50+liste_meteorite[i][j][k][0]+5-55)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_objet_meteorite.append(str((j*50+liste_meteorite[i][j][k][0]+5-55)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_meteorite[i][j][k]=(liste_meteorite[i][j][k][0],liste_meteorite[i][j][k][1]+1)
                if screen==2:
                    image((j*50+liste_meteorite[i][j][k][0]+5-150)*10,(((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1], chemin_fichier,largeur=150, hauteur=150,tag=str((j*50+liste_meteorite[i][j][k][0]+5-150)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_objet_meteorite.append(str((j*50+liste_meteorite[i][j][k][0]+5-150)*10)+str((((hauteur_fenetre()//5)*4)/50)*liste_meteorite[i][j][k][1]))
                    liste_meteorite[i][j][k]=(liste_meteorite[i][j][k][0],liste_meteorite[i][j][k][1]+1)
                if liste_meteorite[i][j][k][1]==50:  # lorsque l'animation est terminer 
                    for p in range(j*50+liste_meteorite[i][j][k][0],j*50+liste_meteorite[i][j][k][0]+10):
                        if liste_terrain[p]!=None:
                            ii=p
                            if i==0:
                                while liste_terrain[ii]==True: # verifie avec un systeme l'unité se trouvant en tete de la "hit box" de l'unité
                                    if ii<1:
                                        break
                                    ii-=1
                                if liste_terrain[ii]!=None and liste_terrain[ii]!=True:
                                    if liste_terrain[ii]["joueur"]!=0:
                                        liste_terrain[ii]["points_de_vie"]-=joueur_age[0][Age[0]]["frappe_aerienne"]
                                        if liste_terrain[ii]["points_de_vie"]<=0:
                                            if liste_terrain[ii]["type_unite"]=="lourd" and liste_terrain[ii]["age"]=="âge_militaire":
                                                dico_son["son_mort_char2.ogg"].play()
                                            elif liste_terrain[ii]["type_unite"]=="anti_blindage" and liste_terrain[ii]["age"]=="âge_futur":
                                                dico_son["son_mort_char.ogg"].play()
                                            else:
                                                son_choix=random.choice([0,1,2])
                                                if son_choix==0:
                                                    dico_son["son_mort.ogg"].play()
                                                if son_choix==1:
                                                    dico_son["son_mort2.ogg"].play()
                                                if son_choix==2:
                                                    dico_son["son_mort3.ogg"].play()
                                            Or[0]+=joueur_age[0][Age[0]]["or_recolte"]*liste_terrain[ii]["cout_or"]
                                            Exp[0]+=joueur_age[0][Age[0]]["exp_recolte"]*liste_terrain[ii]["cout_exp"]
                                            liste_unite_terrain[liste_terrain[ii]["joueur"]]-=1
                                            for h in range(ii,ii+liste_terrain[ii]["taille"]):
                                                if h >len(liste_terrain)-1:
                                                    break
                                                liste_terrain[h]=None
                            if i==1: # meme chose pour les unités du joueur 0 touchées
                                while liste_terrain[ii]==True:
                                    if ii>len(liste_terrain)-2:
                                        break
                                    ii+=1
                                if liste_terrain[ii]!=None and liste_terrain[ii]!=True:
                                    if liste_terrain[ii]["joueur"]!=1:
                                        liste_terrain[ii]["points_de_vie"]-=joueur_age[1][Age[1]]["frappe_aerienne"]
                                        if liste_terrain[ii]["points_de_vie"]<=0:
                                            if liste_terrain[ii]["type_unite"]=="lourd" and liste_terrain[ii]["age"]=="âge_militaire":
                                                dico_son["son_mort_char2.ogg"].play()
                                            elif liste_terrain[ii]["type_unite"]=="anti_blindage" and liste_terrain[ii]["age"]=="âge_futur":
                                                dico_son["son_mort_char.ogg"].play()
                                            else:
                                                son_choix=random.choice([0,1,2])
                                                if son_choix==0:
                                                    dico_son["son_mort.ogg"].play()
                                                if son_choix==1:
                                                    dico_son["son_mort2.ogg"].play()
                                                if son_choix==2:
                                                    dico_son["son_mort3.ogg"].play()
                                            Or[1]+=joueur_age[1][Age[1]]["or_recolte"]*liste_terrain[ii]["cout_or"]
                                            Exp[1]+=joueur_age[1][Age[1]]["exp_recolte"]*liste_terrain[ii]["cout_exp"]
                                            liste_unite_terrain[liste_terrain[ii]["joueur"]]-=1
                                            for _ in range(ii-(liste_terrain[ii]["taille"]-1),ii+1):
                                                if _ <0:
                                                    continue
                                                liste_terrain[_]=None
                if liste_meteorite[i][j][k][1]==51: # on sort lorsqu'on arrive à la phase 51
                    liste_meteorite[i][j]=[]
                    break

def clic_vers_case(x, y,i,j):
    """permet de convertir les coordonnées d'un clic en coordonnées (ligne,colonne)"""
    larg_case,haut_case=largeur_fenetre()/j,hauteur_fenetre()/i
    return int(y / haut_case), int(x / larg_case)

def evenement(i,j,mode):
    """cette fonction prend en argument le nombre de carreau par laquelle la fenetre est decouper en ligne colonne (i,j), et mode qui correspond à un evenement libre ou
    un evenement qui stop le conctionnement du code jusqu'a la prochaine action de l'utilisateur. Cette fonction renvoie les coordonnees du clic gauche, ou la fermeture de la fenetre."""
    if mode==0:
        ev = attend_ev()
    else:
        ev = donne_ev()
    tev = type_ev(ev)
    if tev == "Quitte":
        ferme_fenetre()
        return 'Quitte'
    if tev == "ClicGauche":
        return clic_vers_case(abscisse(ev), ordonnee(ev),i,j)

def amelioration(liste_attente,liste_amelioration,joueur,joueur_age,Age,liste_terrain,liste_tourelle,ping=None):
    """Cette fonction prend en argument la liste des unité en attente, la liste_amelioration qui correspond au stade des amelioration des deux joueurs,
       ainsi que plusieurs parametre vu auparavant, et la variable ping qui sert à ameliorer suelement une amelioration precise,
       Si ping est pas preciser lors de l'appelle de la fonction il devient None et ameliore la totalité des ameliorations. Cette fonction ne renvoie rien"""
    if ping==None or ping==1:
        for i in range(0,liste_amelioration[joueur][1]):
            joueur_age[joueur][Age[joueur]]["unites"]["infanterie"]["degats"]=joueur_age[joueur][Age[joueur]]["unites"]["infanterie"]["degats"]*1.2
    if ping==None or ping==2:
        for i in range(0,liste_amelioration[joueur][2]):
            joueur_age[joueur][Age[joueur]]["unites"]["soutien"]["degats"]=joueur_age[joueur][Age[joueur]]["unites"]["soutien"]["degats"]*1.2
    if ping==None or ping==3:
        for i in range(0,liste_amelioration[joueur][3]):
            joueur_age[joueur][Age[joueur]]["unites"]["anti_blindage"]["degats"]=joueur_age[joueur][Age[joueur]]["unites"]["anti_blindage"]["degats"]*1.2
    if ping==None or ping==4:
        for i in range(0,liste_amelioration[joueur][4]):
            joueur_age[joueur][Age[joueur]]["unites"]["lourd"]["degats"]=joueur_age[joueur][Age[joueur]]["unites"]["lourd"]["degats"]*1.2
    if ping==None or ping==5:
        for i in range(0,liste_amelioration[joueur][5]):
            for eltt in liste_tourelle[joueur]:
                if eltt!=None:
                    eltt["degats"]=int(eltt["degats"]*1.2)
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_canon"]["degats"]=joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_canon"]["degats"]*1.2
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_fleche"]["degats"]=joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_fleche"]["degats"]*1.2
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_missile"]["degats"]=joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_missile"]["degats"]*1.2
    if ping==None or ping==6:
        for i in range(0,liste_amelioration[joueur][6]):
            joueur_age[joueur][Age[joueur]]["unites"]["soutien"]["portee"]=(joueur_age[joueur][Age[joueur]]["unites"]["soutien"]["portee"]*1.2)//1
    if ping==None or ping==7:
        for i in range(0,liste_amelioration[joueur][7]):
            for elt in liste_tourelle[joueur]:
                if elt!=None:
                    elt["portee"]=int(elt["portee"]*1.2)
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_canon"]["portee"]=int(joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_canon"]["portee"]*1.2)
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_fleche"]["portee"]=int(joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_fleche"]["portee"]*1.2)
            joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_missile"]["portee"]=int(joueur_age[joueur][Age[joueur]]["tourelles"]["tourelle_missile"]["portee"]*1.2)
    if ping==None or ping==8:
        for i in range(0,liste_amelioration[joueur][8]):
            for j in range(0,len(liste_terrain)):
                if liste_terrain[j]!=None and liste_terrain[j]!=True:
                    if liste_terrain[j]["type_unite"]=="infanterie" and liste_terrain[j]["joueur"]==joueur:
                        liste_terrain[j]["points_de_vie"]=int(liste_terrain[j]["points_de_vie"]*1.2)
            for elt in liste_attente[joueur]:
                if elt["type_unite"]=="infanterie" and elt["joueur"]==joueur:
                    elt["points_de_vie"]=int(elt["points_de_vie"]*1.2)
            for eelt in joueur_age[joueur]:
                joueur_age[joueur][eelt]["unites"]["infanterie"]["points_de_vie"]=int(joueur_age[joueur][eelt]["unites"]["infanterie"]["points_de_vie"]*1.2)
    if ping==None or ping==9:
        for i in range(0,liste_amelioration[joueur][9]):
            for j in range(0,len(liste_terrain)):
                if liste_terrain[j]!=None and liste_terrain[j]!=True:
                    if liste_terrain[j]["type_unite"]=="anti_blindage" and liste_terrain[j]["joueur"]==joueur:
                        liste_terrain[j]["points_de_vie"]=int(liste_terrain[j]["points_de_vie"]*1.2)
            for elt in liste_attente[joueur]:
                if elt["type_unite"]=="anti_blindage" and elt["joueur"]==joueur:
                    elt["points_de_vie"]=int(elt["points_de_vie"]*1.2)
            for eelt in joueur_age[joueur]:
                joueur_age[joueur][eelt]["unites"]["anti_blindage"]["points_de_vie"]=int(joueur_age[joueur][eelt]["unites"]["anti_blindage"]["points_de_vie"]*1.2)
    if ping==None or ping==10:
        for i in range(0,liste_amelioration[joueur][10]):
            for j in range(0,len(liste_terrain)):
                if liste_terrain[j]!=None and liste_terrain[j]!=True:
                    if liste_terrain[j]["type_unite"]=="lourd" and liste_terrain[j]["joueur"]==joueur:
                        liste_terrain[j]["points_de_vie"]=int(liste_terrain[j]["points_de_vie"]*1.2)
            for elt in liste_attente[joueur]:
                if elt["type_unite"]=="lourd" and elt["joueur"]==joueur:
                    elt["points_de_vie"]=int(elt["points_de_vie"]*1.2)
            for eelt in joueur_age[joueur]:
                joueur_age[joueur][eelt]["unites"]["lourd"]["points_de_vie"]=int(joueur_age[joueur][eelt]["unites"]["lourd"]["points_de_vie"]*1.2)
    if ping==None or ping==11:
        for i in range(0,liste_amelioration[joueur][11]):
            joueur_age[joueur][Age[joueur]]["or_recolte"]+=0.2

def essayer_amelioration(index_amelioration, index_cout, joueur_age, Age, Or, liste_amelioration, liste_attente, liste_terrain, liste_tourelle, dico_son):
    """Cette fonction prend en argument plusieurs variable dans le but d'obtimiser les repetitions pour les achat d'amelioration dans la fonction jeu avec
    un algorithme logique. Cette fonction sert alors au joueur 0 d'acheter une amelioration. Cette fonction ne renvoie rien."""
    if liste_amelioration[0][index_amelioration] != 5:
        cout = joueur_age[0][Age[0]]["amelioration"][index_cout][liste_amelioration[0][index_amelioration]]
        if Or[0] >= cout:
            dico_son["son_amelioration.ogg"].play()
            Or[0] -= cout
            liste_amelioration[0][index_amelioration] += 1
            amelioration(liste_attente, liste_amelioration, 0, joueur_age, Age, liste_terrain, liste_tourelle, index_amelioration)
        else:
            dico_son["son_erreur.ogg"].play()

def jeu(niveau,langue,joueur_age,dico_langue):
    """Cette fonction est la plus importante du jeu. En effet elle regroupe une enorme partie des fonctions vu precedemment. Elle prend en argument le niveau de l'ia,
       la langue du jeu, la liste de dico correspondant aux statistique des joueurs, et le dico langues avec tout les mots afficher dans le jeu avec les 5 langues differentes.
       Cette fonction est detailler avec des commentaire aux endroit important. Cette fonction renvoie le gagnant de la partie ou alors le char "Quitte" en cas d'arret.
       Elle peut aussi retourner au menu en renvoyant la langue utiliser."""
    pygame.mixer.stop()
    dico_son["son_clic.ogg"].play()
    dico_son["son_jeu.gg"].play(20)
    Or=[2500,2500] # initialisation de l'Or des deux joueurs
    Exp=[1000,1000] # initialisation de l'Exp des deux joueurs
    Age=["âge_primitif","âge_primitif"] # Age des deux joueurs qui evolue pendant la partie
    liste_attente = [[],[]] # la liste de liste qui comporte les unité en attente d'etre placer sur le terrain
    liste_terrain=[None]*300 # initialisation du terrain de 300 cases
    liste_unite_terrain = [0,0] # liste du nombre d'unité sur le terrain par joueur
    liste_tourelle=[[None,None,None,None],[None,None,None,None]] # liste de liste des emplacement qui comporte des dico de tourelle par joueurs
    liste_projectile=[] # liste des projectile en cours d'etre animer
    liste_objet=[] # liste de tout les objet qui sont afficher sur la fenetre
    liste_objet_projectile=[] # liste des projectile afficher sur la fenetre
    liste_objet_meteorite=[] # liste des meteorite afficher sur la fenetre
    dico_age_niv={"âge_primitif":0,"âge_antique":1,"âge_médiéval":2,"âge_militaire":3,"âge_apocalypse":4,"âge_futur":5} # dico qui sert a convertir un age en int
    Combat=None # variable qui sert à comporter la position de l'unité se trouvant a gauche d'un affrontement au corps a corps
    temps_ref=time.time() # saisie du temps pour pouvoir determiner des intervales
    screen=0 # position de l'ecran 
    nombre_tourelle=[0,0] # nombre de tourelles des deux joueurs
    liste_meteorite=[[[],[],[],[],[],[]],[[],[],[],[],[],[]]] # liste qui comporte les meteorite des deux joueurs
    frappe=[0,0] # liste avec le nombre de frappe aerienne des deux joueurs
    temps_ia=[[2,1,1,0.5],[2,1,1,0.5]] # le temps que met une ia pour prendre une decision par niveau ( le niveau correspond a la position dans cette liste)
    choix_emplacement_tourelle=[] # prend la position de la tourelle que l'on veut payer
    choix_vendre_tourelle=[]# prend la position de la tourelle que l'on veut vendre
    liste_amelioration=[[False,0,0,0,0,0,0,0,0,0,0,0],[False,0,0,0,0,0,0,0,0,0,0,0]] # liste de liste de l'avancer des ameliorations des deux joueurs
    while joueur_age[0][Age[0]]["pv_base_ultime"][0]>0 and joueur_age[1][Age[1]]["pv_base_ultime"][0]>0: # boucle temps que l'une des bases n'est pas detruite
        Or_joueur=Or[0] # variable pour savoir si la quantité d'or du joueur 0 à changer sur un tour du while et si oui alors il refresh le compte sur le ligne 2156
        action=evenement(36,36,1) # prend un evenement (clic gauche)
        if action=='Quitte':
            return 'Quitte'
        if action!=None:
            if action[1]>=1 and action[1]<5 and action[0]>=33 and action[0]<35: # retour menu
                dico_son["son_clic.ogg"].play()
                return langue
            if action[1]>=33 and action[1]<36 and action[0]>=18 and action[0]<21: # naviguer vers la droite
                if screen!=2:
                    screen+=1
                    dico_son["son_clic.ogg"].play()
                    efface_tout()
                    while len(liste_objet)!=0:
                        liste_objet.pop()
            if action[1]>=1 and action[1]<3 and action[0]>=18 and action[0]<21: # naviguer vers la gauche
                if screen!=0:
                    screen-=1
                    dico_son["son_clic.ogg"].play()
                    efface_tout()
                    while len(liste_objet)!=0:
                        liste_objet.pop()
            if action[1]>=0 and action[1]<len(liste_terrain) and action[0]>=0 and action[0]<5:
                choix_emplacement_tourelle=[]
                choix_vendre_tourelle=[]
            if action[1]>=26 and action[1]<28 and action[0]>=2 and action[0]<4: # payer la frappe aerienne
                if Exp[0]>=joueur_age[0][Age[0]]["cout_frappe_aerienne"]:
                    if joueur_age[0][Age[0]]["recharge_frappe_aerienne"][1]<=0:
                        dico_son["son_clic.ogg"].play()
                        joueur_age[0][Age[0]]["recharge_frappe_aerienne"][1]=joueur_age[0][Age[0]]["recharge_frappe_aerienne"][0]
                        Exp[0]-=joueur_age[0][Age[0]]["cout_frappe_aerienne"]
                        frappe[0]=3
                    else:
                        dico_son["son_erreur.ogg"].play()
                else:
                    dico_son["son_erreur.ogg"].play()
            if len(liste_attente[0])<5:
                if action[1]>=1 and action[1]<3 and action[0]>=2 and action[0]<4: # payer l'unite infanterie
                    if Or[0]>=joueur_age[0][Age[0]]["unites"]["infanterie"]["cout_or"]:
                        dico_son["son_payer.ogg"].play()
                        achat_unite("infanterie",0,Or,joueur_age,Age,liste_attente)
                    else:
                        dico_son["son_erreur.ogg"].play()
                if action[1]>=3 and action[1]<5 and action[0]>=2 and action[0]<4: # payer l'unite soutien
                    if Or[0]>=joueur_age[0][Age[0]]["unites"]["soutien"]["cout_or"]:
                        dico_son["son_payer.ogg"].play()
                        achat_unite("soutien",0,Or,joueur_age,Age,liste_attente)
                    else:
                        dico_son["son_erreur.ogg"].play()
                if action[1]>=5 and action[1]<7 and action[0]>=2 and action[0]<4: # payer l'unite anti_blindage
                    if Or[0]>=joueur_age[0][Age[0]]["unites"]["anti_blindage"]["cout_or"]:
                        dico_son["son_payer.ogg"].play()
                        achat_unite("anti_blindage",0,Or,joueur_age,Age,liste_attente)
                    else:
                        dico_son["son_erreur.ogg"].play()
                if action[1]>=7 and action[1]<9 and action[0]>=2 and action[0]<4: # payer l'unite lourd
                    if liste_amelioration[0][0]==True:
                        if Or[0]>=joueur_age[0][Age[0]]["unites"]["lourd"]["cout_or"]:
                            dico_son["son_payer.ogg"].play()
                            achat_unite("lourd",0,Or,joueur_age,Age,liste_attente)
                        else:
                            dico_son["son_erreur.ogg"].play()
                    else:
                        dico_son["son_erreur.ogg"].play()
            if action[1]>=13 and action[1]<15 and action[0]>=2 and action[0]<4: # achat d'une tourelle_canon
                dico_son["son_clic.ogg"].play()
                for ii in range(0,nombre_tourelle[0]):
                    if liste_tourelle[0][ii]==None:
                        choix_emplacement_tourelle.append(ii)
                        choix_tourelle="tourelle_canon"
            if action[1]>=15 and action[1]<17 and action[0]>=2 and action[0]<4: # achat d'une tourelle_fleche
                dico_son["son_clic.ogg"].play()
                for ii in range(0,nombre_tourelle[0]):
                    if liste_tourelle[0][ii]==None:
                        choix_emplacement_tourelle.append(ii)
                        choix_tourelle="tourelle_fleche"
            if action[1]>=17 and action[1]<19 and action[0]>=2 and action[0]<4: # achat d'une tourelle_missile
                dico_son["son_clic.ogg"].play()
                for ii in range(0,nombre_tourelle[0]):
                    if liste_tourelle[0][ii]==None:
                        choix_emplacement_tourelle.append(ii)
                        choix_tourelle="tourelle_missile"
            if len(choix_emplacement_tourelle)>0:
                if action[1]>=6 and action[1]<8 and action[0]>=18 and action[0]<20: # placement de la tourelle en position 0
                    if 0 in choix_emplacement_tourelle:
                        if Or[0]>=joueur_age[0][Age[0]]["tourelles"][choix_tourelle]["prix"]:
                            dico_son["son_payer.ogg"].play()
                            liste_tourelle[0][0]=copy.deepcopy(joueur_age[0][Age[0]]["tourelles"][choix_tourelle])
                            Or[0]-=liste_tourelle[0][0]["prix"]
                            choix_emplacement_tourelle=[]
                        else:
                            dico_son["son_erreur.ogg"].play()
                if action[1]>=6 and action[1]<8 and action[0]>=15 and action[0]<17: # placement de la tourelle en position 1
                    if 1 in choix_emplacement_tourelle:
                        if Or[0]>=joueur_age[0][Age[0]]["tourelles"][choix_tourelle]["prix"]:
                            dico_son["son_payer.ogg"].play()
                            liste_tourelle[0][1]=copy.deepcopy(joueur_age[0][Age[0]]["tourelles"][choix_tourelle])
                            Or[0]-=liste_tourelle[0][1]["prix"]
                            choix_emplacement_tourelle=[]
                        else:
                            dico_son["son_erreur.ogg"].play()
                if action[1]>=6 and action[1]<8 and action[0]>=12 and action[0]<14: # placement de la tourelle en position 2
                    if 2 in choix_emplacement_tourelle:
                        if Or[0]>=joueur_age[0][Age[0]]["tourelles"][choix_tourelle]["prix"]:
                            dico_son["son_payer.ogg"].play()
                            liste_tourelle[0][2]=copy.deepcopy(joueur_age[0][Age[0]]["tourelles"][choix_tourelle])
                            Or[0]-=liste_tourelle[0][2]["prix"]
                            choix_emplacement_tourelle=[]
                        else:
                            dico_son["son_erreur.ogg"].play()
                if action[1]>=3 and action[1]<5 and action[0]>=15 and action[0]<17: # placement de la tourelle en position 3
                    if 3 in choix_emplacement_tourelle:
                        if Or[0]>=joueur_age[0][Age[0]]["tourelles"][choix_tourelle]["prix"]:
                            dico_son["son_payer.ogg"].play()
                            liste_tourelle[0][3]=copy.deepcopy(joueur_age[0][Age[0]]["tourelles"][choix_tourelle])
                            Or[0]-=liste_tourelle[0][3]["prix"]
                            choix_emplacement_tourelle=[]
                        else:
                            dico_son["son_erreur.ogg"].play()
            if action[1]>=19 and action[1]<21 and action[0]>=2 and action[0]<4: # achete un emplacement de tourelle
                if nombre_tourelle[0]>=0 and nombre_tourelle[0]<4:
                    if Or[0]>=joueur_age[0][Age[0]]["cout_tourelle"][nombre_tourelle[0]]:
                        dico_son["son_payer.ogg"].play()
                        Or[0]-=joueur_age[0][Age[0]]["cout_tourelle"][nombre_tourelle[0]]
                        nombre_tourelle[0]+=1
                    else:
                        dico_son["son_erreur.ogg"].play()
                else:
                    dico_son["son_erreur.ogg"].play()
            if action[1]>=21 and action[1]<23 and action[0]>=2 and action[0]<4: # vendre une tourelle
                dico_son["son_clic.ogg"].play()
                for ii in range(0,nombre_tourelle[0]):
                    if liste_tourelle[0][ii]!=None:
                        choix_vendre_tourelle.append(ii)
            if len(choix_vendre_tourelle)>0:
                if action[1]>=6 and action[1]<8 and action[0]>=18 and action[0]<20: # choix de la tourelle vendu en position 0
                    if 0 in choix_vendre_tourelle:
                        dico_son["son_debloque.ogg"].play()
                        Or[0]+=liste_tourelle[0][0]["prix"]//2
                        liste_tourelle[0][0]=None
                        choix_vendre_tourelle=[]
                        liste_objet.remove("tourelle00")
                        efface("tourelle00")
                if action[1]>=6 and action[1]<8 and action[0]>=15 and action[0]<17: # choix de la tourelle vendu en position 1
                    if 1 in choix_vendre_tourelle:
                        dico_son["son_debloque.ogg"].play()
                        Or[0]+=liste_tourelle[0][1]["prix"]//2
                        liste_tourelle[0][1]=None
                        choix_vendre_tourelle=[]
                        liste_objet.remove("tourelle01")
                        efface("tourelle01")
                if action[1]>=6 and action[1]<8 and action[0]>=12 and action[0]<14: # choix de la tourelle vendu en position 2
                    if 2 in choix_vendre_tourelle:
                        dico_son["son_debloque.ogg"].play()
                        Or[0]+=liste_tourelle[0][2]["prix"]//2
                        liste_tourelle[0][2]=None
                        choix_vendre_tourelle=[]
                        liste_objet.remove("tourelle02")
                        efface("tourelle02")
                if action[1]>=3 and action[1]<5 and action[0]>=15 and action[0]<17: # choix de la tourelle vendu en position 3
                    if 3 in choix_vendre_tourelle:
                        dico_son["son_debloque.ogg"].play()
                        Or[0]+=liste_tourelle[0][3]["prix"]//2
                        liste_tourelle[0][3]=None
                        choix_vendre_tourelle=[]
                        liste_objet.remove("tourelle03")
                        efface("tourelle03")
            if action[1]>=24 and action[1]<26 and action[0]>=2 and action[0]<4: # payement de l'evolution
                if joueur_age[0][Age[0]]["cout_evolution"][1]!=None:
                    if Exp[0]>=joueur_age[0][Age[0]]["cout_evolution"][0]:
                        dico_son["son_evolution.ogg"].play()
                        Exp[0]-=joueur_age[0][Age[0]]["cout_evolution"][0]
                        pv=joueur_age[0][Age[0]]["pv_base_ultime"][0]
                        pv_max=joueur_age[0][Age[0]]["pv_base_ultime"][1]
                        Age[0]=joueur_age[0][Age[0]]["cout_evolution"][1]
                        joueur_age[0][Age[0]]["pv_base_ultime"][0]=pv+(joueur_age[0][Age[0]]["pv_base_ultime"][1]-pv_max)
                        efface_tout()
                        while len(liste_objet)!=0:
                            liste_objet.pop()
                        refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
                        liste_amelioration[0][0]=False
                        amelioration(liste_attente,liste_amelioration,0,joueur_age,Age,liste_terrain,liste_tourelle)
                    else:
                        dico_son["son_erreur.ogg"].play()
                else:
                    dico_son["son_erreur.ogg"].play()
            if action[1]==29 and action[0]==2: # deverouille l'unité lourd
                if liste_amelioration[0][0]!=True:
                    if Or[0]>=joueur_age[0][Age[0]]["amelioration"][0]:
                        dico_son["son_debloque.ogg"].play()
                        Or[0]-=joueur_age[0][Age[0]]["amelioration"][0]
                        liste_amelioration[0][0]=True
                    else:
                        dico_son["son_erreur.ogg"].play()
            actions = [(30, 2, 0, 1), (31, 2, 0, 2), (32, 2, 0, 3), (33, 2, 0, 4), (34, 2, 0, 5),(29, 3, 0, 6), (30, 3, 0, 7), (31, 3, 0, 8), (32, 3, 0, 9), (33, 3, 0, 10), (34, 3, 0, 11)]
            for action_id, action_type, amelioration_group, index_amelioration in actions: # en fonction du clic ça paye l'amelioration correspondante
                if action[1] == action_id and action[0] == action_type:
                    essayer_amelioration(index_amelioration, amelioration_group + 1, joueur_age, Age, Or, liste_amelioration, liste_attente, liste_terrain, liste_tourelle, dico_son)
        for i in range(2): # fait les 3 vagues de meteorite
            if frappe[i]!=0:
                if liste_meteorite[i]==[[],[],[],[],[],[]]:
                    for _ in range(joueur_age[i][Age[i]]["nombre_frappe_aerienne"]):
                        liste_meteorite[i][random.choice([0,1,2,3,4,5])].append((random.choice([0,10,20,30,40]),0))
                    frappe[i]-=1
                    dico_son["son_meteore.ogg"].play()
        temps_courant=time.time() # prend un deuxieme temps
        affichage_jeu(liste_terrain,screen,liste_meteorite,nombre_tourelle,langue,dico_age_niv,Age,liste_objet,joueur_age,liste_tourelle,liste_projectile,liste_objet_projectile,liste_objet_meteorite,liste_unite_terrain,Or,Exp,dico_langue,liste_amelioration)
        attente(0.02)
        temps_ia[0][niveau]-=0.02
        if temps_ia[0][niveau]<=0: # fait le choix de l'ia
            ia(Or,Exp,liste_tourelle,nombre_tourelle,frappe,liste_amelioration,screen,niveau,liste_unite_terrain,Age,joueur_age,liste_attente,liste_objet,liste_terrain)
            temps_ia[0][niveau]=temps_ia[1][niveau]
        if temps_courant-temps_ref>=0.02: # toutes les 0.02s, tout est mis a jour
            verfication_deplacement(liste_terrain,joueur_age) # on verifie d'abord le deplacement de toutes les unités
            verif_tourelle(liste_terrain,liste_tourelle,screen,liste_projectile,Age,Or,Exp,joueur_age,liste_objet,liste_unite_terrain) # ensuite si les tourelles peuvent tirer
            verif_projectile(liste_terrain,Combat,screen,liste_projectile,joueur_age,Or,Exp,Age,liste_unite_terrain,liste_objet) # ensuite si les unité peuvent tirer 
            if Combat==None:
                Combat=combat_verif(liste_terrain,joueur_age) # verifie si il y a un combat en face à face au corps à corps
            if Combat!=None:
                if liste_terrain[Combat]==None or liste_terrain[Combat]==True or liste_terrain[Combat+1]==None or liste_terrain[Combat+1]==True: # si un deux deux combattant est mort la variable Combat redeviens None
                    Combat=None
                else:
                    combat(liste_terrain,Combat,screen,liste_objet,joueur_age) #Si la variable combat est pas None alors on appelle combat avec le combattant de gauche
                    combat(liste_terrain,Combat+1,screen,liste_objet,joueur_age)#Et le combattant de droite
                    if result_combat(liste_terrain,Combat,liste_unite_terrain,Or,Exp,joueur_age,Age)==1: # on prend le resultat de result_combat et change la variable Combat en conséquence 
                        Combat=None
            temps_maj(liste_attente,liste_terrain,liste_unite_terrain,joueur_age,Age,liste_objet,screen) # on met a jour le temps de toutes les statistiques de chargement (deplacement,tire,frappe,meteorite,liste_attente,ect)
            if Or[0]!=Or_joueur:
                while "txt" in liste_objet:
                    efface("txt")
                    liste_objet.remove("txt")
            temps_ref=temps_courant
    if joueur_age[0][Age[0]]["pv_base_ultime"][0]<=0: # si le joueur 1 à gagner
        return menu_fin(langue,"perdu",dico_langue)
    return menu_fin(langue,"gagne",dico_langue) # si le joueur 0 à gagnger






def ia_initialisation(dico_ia,niveau,stat,cout):
    """Cette fonction prend en argument le dico qui correspond à toutes les statistiques de jeu de l'ia, le niveau de l'ia, lemultiplicateur stat et le diviseur cout.
       En effet cette fonction applique le multiplicateur stat et le diviseur cout aux statistiques de l'ia pour debuter la partie avec des statistiques correspondant à son niveau.
       Cette fonction ne renvoie rien."""
    for elt in dico_ia:
        dico_ia[elt]["pv_base_ultime"][1]=int(dico_ia[elt]["pv_base_ultime"][1]*stat)
        dico_ia[elt]["pv_base_ultime"][0]=int(dico_ia[elt]["pv_base_ultime"][0]*stat)
        dico_ia[elt]["recharge_frappe_aerienne"][0]=int(dico_ia[elt]["recharge_frappe_aerienne"][0]*cout)
        dico_ia[elt]["recharge_frappe_aerienne"][1]=int(dico_ia[elt]["recharge_frappe_aerienne"][1]*cout)
        dico_ia[elt]["cout_frappe_aerienne"]=int(dico_ia[elt]["cout_frappe_aerienne"]*cout)
        dico_ia[elt]["cout_evolution"][0]=int(dico_ia[elt]["cout_evolution"][0]*cout)
        for i in range(4):
            dico_ia[elt]["cout_tourelle"][i]=int(dico_ia[elt]["cout_tourelle"][i]*cout)
        dico_ia[elt]["or_recolte"]=int(dico_ia[elt]["or_recolte"]*stat)
        dico_ia[elt]["exp_recolte"]=int(dico_ia[elt]["exp_recolte"]*stat)
        for elt2 in dico_ia[elt]["unites"]:
            dico_ia[elt]["unites"][elt2]["points_de_vie"]=int(dico_ia[elt]["unites"][elt2]["points_de_vie"]*stat)
            dico_ia[elt]["unites"][elt2]["degats"]=int(dico_ia[elt]["unites"][elt2]["degats"]*stat)
            dico_ia[elt]["unites"][elt2]["vitesse_de_frappe"]=dico_ia[elt]["unites"][elt2]["vitesse_de_frappe"]*cout
            dico_ia[elt]["unites"][elt2]["vitesse_de_marche"]=dico_ia[elt]["unites"][elt2]["vitesse_de_marche"]*cout
            dico_ia[elt]["unites"][elt2]["portee"]=dico_ia[elt]["unites"][elt2]["portee"]*stat
            dico_ia[elt]["unites"][elt2]["temps_construction"]=dico_ia[elt]["unites"][elt2]["temps_construction"]*cout
            dico_ia[elt]["unites"][elt2]["cout_or"]=int(dico_ia[elt]["unites"][elt2]["cout_or"]*cout)
        for elt3 in dico_ia[elt]["tourelles"]:
            dico_ia[elt]["tourelles"][elt3]["prix"]=int(dico_ia[elt]["tourelles"][elt3]["prix"]*cout)
            dico_ia[elt]["tourelles"][elt3]["degats"]=int(dico_ia[elt]["tourelles"][elt3]["degats"]*stat)
            dico_ia[elt]["tourelles"][elt3]["vitesse_frappe"]=dico_ia[elt]["tourelles"][elt3]["vitesse_frappe"]*cout
            dico_ia[elt]["tourelles"][elt3]["portee"]=dico_ia[elt]["tourelles"][elt3]["portee"]*stat
            dico_ia[elt]["frappe_aerienne"]=int(dico_ia[elt]["frappe_aerienne"]*stat)
        for j in range(1,12):
            for k in range(5):
                dico_ia[elt]["amelioration"][j][k]*=cout
        if niveau==2:
            dico_ia[elt]["nombre_frappe_aerienne"]=int(dico_ia[elt]["nombre_frappe_aerienne"]*1.5)
        if niveau==3:
            dico_ia[elt]["nombre_frappe_aerienne"]=int(dico_ia[elt]["nombre_frappe_aerienne"]*2)

def ia(Or,Exp,liste_tourelle,nombre_tourelle,frappe,liste_amelioration,screen,niveau,liste_unite_terrain,Age,joueur_age,liste_attente,liste_objet,liste_terrain):
    """Cette fonction prend en argument des argument citer precedemment et le nombre de frappe aerienne restante dans le parametre frappe.
       En effet cette fonction determine aleatoirement les choix du joueur 1 en fonction de la difficulté choisis dans le parametre niveau.
       Cette fonction ne renvoie rien"""
    if niveau==0:
        choix=random.choice([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,random.choice([11,12,13,14,15,16,17,18,19,20,21,22])]) #liste des choix possible pour le niveau facile
    if niveau==1:
        choix=random.choice([0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9,10,10,10,10,10,random.choice([11,12,13,14,15,16,17,18,19,20,21,22])])#liste des choix possible pour le niveau intermediaire
    if niveau==2 or niveau==3:
        choix=random.choice([0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9,10,10,10,10,10,random.choice([11,12,13,14,15,16,17,18,19,20,21,22]),random.choice([11,12,13,14,15,16,17,18,19,20,21,22]),random.choice([11,12,13,14,15,16,17,18,19,20,21,22]),random.choice([11,12,13,14,15,16,17,18,19,20,21,22]),random.choice([11,12,13,14,15,16,17,18,19,20,21,22])])#liste des choix possible pour le niveau difficile et impossible
    if choix==1: # Achat de la frappe aerienne 
        if (niveau==2 and liste_unite_terrain[0]>=5) or niveau==1 or niveau==0 or (niveau==3 and liste_unite_terrain[0]>=5):
                if Exp[1]>=joueur_age[1][Age[1]]["cout_frappe_aerienne"]:
                    if joueur_age[1][Age[1]]["recharge_frappe_aerienne"][1]<=0:
                        joueur_age[1][Age[1]]["recharge_frappe_aerienne"][1]=joueur_age[1][Age[1]]["recharge_frappe_aerienne"][0]
                        Exp[1]-=joueur_age[1][Age[1]]["cout_frappe_aerienne"]
                        frappe[1]=3
    if len(liste_attente[1])<5:
        if choix==2: # achat unite infanterie
            achat_unite("infanterie",1,Or,joueur_age,Age,liste_attente)
        if choix==3: # achat unite soutien
            achat_unite("soutien",1,Or,joueur_age,Age,liste_attente)
        if choix==4: # achat unite anti_blindage
            achat_unite("anti_blindage",1,Or,joueur_age,Age,liste_attente)
        if choix==5: # achat unite lourd
            if liste_amelioration[1][0]==True:
                achat_unite("lourd",1,Or,joueur_age,Age,liste_attente)
    if choix==6: # achat d'un support tourelle
        if nombre_tourelle[1]>=0 and nombre_tourelle[1]<4:
            if Or[1]>=joueur_age[1][Age[1]]["cout_tourelle"][nombre_tourelle[1]]:
                Or[1]-=joueur_age[0][Age[1]]["cout_tourelle"][nombre_tourelle[1]]
                nombre_tourelle[1]+=1
    if choix==7 or choix==8 or choix==9 : # achat d'une tourelle
        if choix==7:
            choix_tourelle="tourelle_canon"
        if choix==8:
            choix_tourelle="tourelle_fleche"
        if choix==9:
            choix_tourelle="tourelle_missile"
        for ii in range(0,nombre_tourelle[1]):
            if liste_tourelle[1][ii]==None:
                if Or[1]>=joueur_age[1][Age[1]]["tourelles"][choix_tourelle]["prix"]:
                        liste_tourelle[1][ii]=copy.deepcopy(joueur_age[1][Age[1]]["tourelles"][choix_tourelle])
                        Or[1]-=liste_tourelle[1][ii]["prix"]
                        break
    if choix==10: # achat de l'evolution
        if joueur_age[1][Age[1]]["cout_evolution"][1]!=None:
            if Exp[1]>=joueur_age[1][Age[1]]["cout_evolution"][0]:
                dico_son["son_evolution.ogg"].play()
                Exp[1]-=joueur_age[0][Age[0]]["cout_evolution"][0]
                pv=joueur_age[1][Age[1]]["pv_base_ultime"][0]
                pv_max=joueur_age[1][Age[1]]["pv_base_ultime"][1]
                Age[1]=joueur_age[1][Age[1]]["cout_evolution"][1]
                joueur_age[1][Age[1]]["pv_base_ultime"][0]=pv+(joueur_age[1][Age[1]]["pv_base_ultime"][1]-pv_max)
                efface_tout()
                while len(liste_objet)!=0:
                    liste_objet.pop()
                refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
                liste_amelioration[1][0]=False
                amelioration(liste_attente,liste_amelioration,1,joueur_age,Age,liste_terrain,liste_tourelle)
    if choix==11: # achat de l'amelioration qui permet de debloquer l'unite lourd
        if Or[1]>=joueur_age[1][Age[1]]["amelioration"][0]:
            Or[1]-=joueur_age[1][Age[1]]["amelioration"][0]
            liste_amelioration[1][0]=True
    if (niveau==3 and liste_unite_terrain[0]<liste_unite_terrain[1]) or niveau==0 or niveau==1 or niveau==2: #condition pour le niv impossible, s'il y a moins d'unité ennemi sur le terrain alors il se permet d'acheter une amelioration
        if choix>=12 and choix<23: # choix pour une amelioration (11 differentes)
            if liste_amelioration[1][choix-11]!=5:
                if Or[1]>=joueur_age[1][Age[1]]["amelioration"][choix-11][liste_amelioration[1][choix-11]]:
                    Or[1]-=joueur_age[1][Age[1]]["amelioration"][choix-11][liste_amelioration[1][choix-11]]
                    liste_amelioration[1][choix-11]+=1
                    amelioration(liste_attente,liste_amelioration,1,joueur_age,Age,liste_terrain,liste_tourelle,choix-11)






def refresh_barre_de_vie(screen,liste_terrain,i,liste_objet,joueur_age):
    """Cette fonction prend en argument la position de l'ecran screen, la liste des cases du terrain dans liste_terrain, la position sur le terrain de l'unité avec i,
       la liste des objet afficher sur la page avec liste_objet, la liste des deux dico cité dans les fonctions precedentes. Cette fonction reaffiche l'unité ainsi que sa vie restante
       grace à un calcule vie_actuelle diviser par la vie_totale de l'unité. Cette fonction ne renvoie rien"""
    while "perso"+str(i) in liste_objet:
        efface("perso"+str(i))
        liste_objet.remove("perso"+str(i))
    chemin=str('\\')+ str(liste_terrain[i]["age"]) + str('\\ ')
    chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
    chemin_fichier = os.path.join(chemin_courant, liste_terrain[i]["type_unite"]+str(liste_terrain[i]["joueur"])+'.png')
    if screen==0:
        if liste_terrain[i]["joueur"]==0:
            image(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle((((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle((((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
        if liste_terrain[i]["joueur"]==1:
            image(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle((((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle((((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
    if screen==1:
        if liste_terrain[i]["joueur"]==0:
            image((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle(((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle(((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
        if liste_terrain[i]["joueur"]==1:
            image((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle(((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle(((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
    if screen==2:
        if liste_terrain[i]["joueur"]==0:
            image((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle(((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle(((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
        if liste_terrain[i]["joueur"]==1:
            image((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
            rectangle(((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
            rectangle(((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
    liste_objet.append("perso"+str(i))

def anime_projectile(liste_projectile,screen,liste_objet_projectile,Age,liste_terrain):
    """Cette fonction prend en argument la liste des projectile à animer, la position de l'ecran, la liste des projectile present sur la fenetre, l'Age des deux joueurs,
       la liste des cases du terrain. En effet cette fonction anime 4 images de projectile d'un point A à un point B sur 4 intervale de 0.02s. Cette fonction est purement graphique ce
       qui importe peu de vous expliquer comment l'image est afficher dans toutes les configuration possible. C'est seulement des calcules de largeur et hauteur de fenetre, par rapport au tireur et
       à la cible. Cette fonction ne renvoie rien"""
    for elt in liste_objet_projectile:
        efface(elt)
        liste_objet_projectile.remove(elt)
    for elt in liste_projectile:
        if elt[0]==0 or elt[0]==2:
            chemin=str('\\')+ str(Age[0]) + str('\\ ')
            chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
            chemin_fichier = os.path.join(chemin_courant, 'projectile.png')
        else:
            chemin=str('\\')+ str(Age[1]) + str('\\ ')
            chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
            chemin_fichier = os.path.join(chemin_courant, 'projectile.png')
        if screen==0:
            if elt[3]==0:
                if elt[0]==0:
                    if elt[1]==0:
                        image(8*(largeur_fenetre()/36),20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(8*(largeur_fenetre()/36))+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(8*(largeur_fenetre()/36))+str(20*(hauteur_fenetre()/36)))
                        elt[4]=(8*(largeur_fenetre()/36),20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image(8*(largeur_fenetre()/36),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(8*(largeur_fenetre()/36))+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(8*(largeur_fenetre()/36))+str(17*(hauteur_fenetre()/36)))
                        elt[4]=(8*(largeur_fenetre()/36),17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image(8*(largeur_fenetre()/36),14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(8*(largeur_fenetre()/36))+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(8*(largeur_fenetre()/36))+str(14*(hauteur_fenetre()/36)))
                        elt[4]=(8*(largeur_fenetre()/36),14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image(5*(largeur_fenetre()/36),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(5*(largeur_fenetre()/36))+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(5*(largeur_fenetre()/36))+str(17*(hauteur_fenetre()/36)))
                        elt[4]=(5*(largeur_fenetre()/36),17*(hauteur_fenetre()/36))
                if elt[0]==1:
                    if elt[1]==0:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(20*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre())+str(14*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre(),14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre(),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre(),17*(hauteur_fenetre()/36))
                if elt[0]==2:
                    elt[4]=(420+elt[1]*10,(hauteur_fenetre()//5)*4-100)
                if elt[0]==3:
                    elt[4]=(420+elt[1]*10,(hauteur_fenetre()//5)*4-100)
            if liste_terrain[elt[2]]==None or liste_terrain[elt[2]]==True:
                if elt[0]==0 or 2:
                    elt[2]-=1
                else:
                    elt[2]+=1
            if elt[3]==1:
                image(elt[4][0]+(420+elt[2]*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+(420+elt[2]*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                liste_objet_projectile.append(str(elt[4][0]+(420+elt[2]*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                elt[4]=(elt[4][0]+(420+elt[2]*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5)
            if elt[3]==2:
                image(elt[4][0]+(420+elt[2]*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+(420+elt[2]*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                liste_objet_projectile.append(str(elt[4][0]+(420+elt[2]*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                elt[4]=(elt[4][0]+(420+elt[2]*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4)
            if elt[3]==3:
                image(elt[4][0]+(420+elt[2]*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+(420+elt[2]*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                liste_objet_projectile.append(str(elt[4][0]+(420+elt[2]*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                elt[4]=(elt[4][0]+(420+elt[2]*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3)
            if elt[3]==4:
                image(elt[4][0]+(420+elt[2]*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+(420+elt[2]*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                liste_objet_projectile.append(str(elt[4][0]+(420+elt[2]*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                elt[4]=(elt[4][0]+(420+elt[2]*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2)
            if elt[3]!=5:
                elt[3]+=1
                break
            if elt[3]==5:
                liste_projectile.remove(elt)
        if screen==1:
            if elt[3]==0:
                if elt[0]==0:
                    if elt[1]==0:
                        image((8*(largeur_fenetre()/36))-960,20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-960)+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-960)+str(20*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-960,20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image((8*(largeur_fenetre()/36))-960,17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-960)+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-960)+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-960,17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image((8*(largeur_fenetre()/36))-960,14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-960)+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-960)+str(14*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-960,14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image((5*(largeur_fenetre()/36))-960,17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((5*(largeur_fenetre()/36))-960)+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((5*(largeur_fenetre()/36))-960)+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((5*(largeur_fenetre()/36))-960,17*(hauteur_fenetre()/36))
                if elt[0]==1:
                    if elt[1]==0:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(20*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(14*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(8*(largeur_fenetre()/36)))+largeur_fenetre()//2,14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre()//2,17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre()//2)+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((largeur_fenetre()-(5*(largeur_fenetre()/36)))+largeur_fenetre()//2,17*(hauteur_fenetre()/36))
                if elt[0]==2:
                    elt[4]=((elt[1]-55)*10,(hauteur_fenetre()//5)*4-100)
                if elt[0]==3:
                    elt[4]=((elt[1]-55)*10,(hauteur_fenetre()//5)*4-100)
            if liste_terrain[elt[2]]==None or liste_terrain[elt[2]]==True:
                if elt[0]==0 or 2:
                    elt[2]-=1
                else:
                    elt[2]+=1
            if elt[3]==1:
                image(elt[4][0]+((elt[2]-55)*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                elt[4]=(elt[4][0]+((elt[2]-55)*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5)
            if elt[3]==2:
                image(elt[4][0]+((elt[2]-55)*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                elt[4]=(elt[4][0]+((elt[2]-55)*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4)
            if elt[3]==3:
                image(elt[4][0]+((elt[2]-55)*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                elt[4]=(elt[4][0]+((elt[2]-55)*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3)
            if elt[3]==4:
                image(elt[4][0]+((elt[2]-55)*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-55)*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                elt[4]=(elt[4][0]+((elt[2]-55)*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2)
            if elt[3]!=5:
                elt[3]+=1
                break
            if elt[3]==5:
                liste_projectile.remove(elt)
        if screen==2:
            if elt[3]==0:
                if elt[0]==0:
                    if elt[1]==0:
                        image((8*(largeur_fenetre()/36))-largeur_fenetre(),20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(20*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-largeur_fenetre(),20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image((8*(largeur_fenetre()/36))-largeur_fenetre(),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-largeur_fenetre(),17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image((8*(largeur_fenetre()/36))-largeur_fenetre(),14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((8*(largeur_fenetre()/36))-largeur_fenetre())+str(14*(hauteur_fenetre()/36)))
                        elt[4]=((8*(largeur_fenetre()/36))-largeur_fenetre(),14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image((5*(largeur_fenetre()/36))-largeur_fenetre(),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str((5*(largeur_fenetre()/36))-largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str((5*(largeur_fenetre()/36))-largeur_fenetre())+str(17*(hauteur_fenetre()/36)))
                        elt[4]=((5*(largeur_fenetre()/36))-largeur_fenetre(),17*(hauteur_fenetre()/36))
                if elt[0]==1:
                    if elt[1]==0:
                        image(largeur_fenetre()-(8*(largeur_fenetre()/36)),20*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(20*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(20*(hauteur_fenetre()/36)))
                        elt[4]=(largeur_fenetre()-(8*(largeur_fenetre()/36)),20*(hauteur_fenetre()/36))
                    if elt[1]==1:
                        image(largeur_fenetre()-(8*(largeur_fenetre()/36)),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(17*(hauteur_fenetre()/36)))
                        elt[4]=(largeur_fenetre()-(8*(largeur_fenetre()/36)),17*(hauteur_fenetre()/36))
                    if elt[1]==2:
                        image(largeur_fenetre()-(8*(largeur_fenetre()/36)),14*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(14*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(largeur_fenetre()-(8*(largeur_fenetre()/36)))+str(14*(hauteur_fenetre()/36)))
                        elt[4]=(largeur_fenetre()-(8*(largeur_fenetre()/36)),14*(hauteur_fenetre()/36))
                    if elt[1]==3:
                        image(largeur_fenetre()-(5*(largeur_fenetre()/36)),17*(hauteur_fenetre()/36), chemin_fichier,largeur=20, hauteur=20,tag=str(largeur_fenetre()-(5*(largeur_fenetre()/36)))+str(17*(hauteur_fenetre()/36)))
                        liste_objet_projectile.append(str(largeur_fenetre()-(5*(largeur_fenetre()/36)))+str(17*(hauteur_fenetre()/36)))
                        elt[4]=(largeur_fenetre()-(5*(largeur_fenetre()/36)),17*(hauteur_fenetre()/36))
                if elt[0]==2:
                    elt[4]=((elt[1]-150)*10,(hauteur_fenetre()//5)*4-100)
                if elt[0]==3:
                    elt[4]=((elt[1]-150)*10,(hauteur_fenetre()//5)*4-100)
            if liste_terrain[elt[2]]==None or liste_terrain[elt[2]]==True:
                if elt[0]==0 or 2:
                    elt[2]-=1
                else:
                    elt[2]+=1
            if elt[3]==1:
                image(elt[4][0]+((elt[2]-150)*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/5)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5))
                elt[4]=(elt[4][0]+((elt[2]-150)*10-elt[4][0])/5,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/5)
            if elt[3]==2:
                image(elt[4][0]+((elt[2]-150)*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/4)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4))
                elt[4]=(elt[4][0]+((elt[2]-150)*10-elt[4][0])/4,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/4)
            if elt[3]==3:
                image(elt[4][0]+((elt[2]-150)*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/3)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3))
                elt[4]=(elt[4][0]+((elt[2]-150)*10-elt[4][0])/3,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/3)
            if elt[3]==4:
                image(elt[4][0]+((elt[2]-150)*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2, chemin_fichier,largeur=20, hauteur=20,tag=str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                liste_objet_projectile.append(str(elt[4][0]+((elt[2]-150)*10-elt[4][0])/2)+str(elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2))
                elt[4]=(elt[4][0]+((elt[2]-150)*10-elt[4][0])/2,elt[4][1]-(elt[4][1]-(hauteur_fenetre()//5)*4)/2)
            if elt[3]!=5:
                elt[3]+=1
                break
            if elt[3]==5:
                liste_projectile.remove(elt)

def affichage_jeu(liste_terrain,screen,liste_meteorite,nombre_tourelle,langue,dico_age_niv,Age,liste_objet,joueur_age,liste_tourelle,liste_projectile,liste_objet_projectile,liste_objet_meteorite,liste_unite_terrain,Or,Exp,dico_langue,liste_amelioration):
    """Cette fonction prend en argument toutes les variables, tableau, dico du jeu pour pouvroi afficher se qu'il se passe en temps reel avec des condition bien precise.
       C'est une fonction purement graphique. Cette fonction ne renvoie rien."""
    if screen==0:  # lorsqu'on est placer sur l'ecran en position 0
        if dico_age_niv[Age[0]]>=dico_age_niv[Age[1]]:
            chemin=str('\\')+ str(Age[0]) + str('\\ ')
        else:
            chemin=str('\\')+ str(Age[1]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'fond0.png')
        if "fond"+str(chemin) not in liste_objet:
            for elt in dico_age_niv:
                if elt==chemin[1:-2]:
                    break
                if "fond"+str('\\')+ str(elt) + str('\\ ') in liste_objet:
                    efface("fond"+str('\\')+ str(elt) + str('\\ '))
                    liste_objet.remove("fond"+str('\\')+ str(elt) + str('\\ '))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="fond"+str(chemin))
            liste_objet.append("fond"+str(chemin))
        chemin=str('\\')+ str(Age[0]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'base_barre.png')
        if "base_barre"+Age[0] not in liste_objet:
            for elt in dico_age_niv:
                if elt==Age[0]:
                    break
                if elt in liste_objet:
                    efface("base_barre"+str(elt))
                    liste_objet.remove("base_barre"+str(elt))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="base_barre"+Age[0])
            liste_objet.append("base_barre"+Age[0])
        for ii in range(len(liste_terrain)//2,len(liste_terrain)):
            if "perso"+str(ii) in liste_objet:
                efface("perso"+str(ii))
                liste_objet.remove("perso"+str(ii))
        for i in range(len(liste_terrain)//2):  # affiche toutes les unités sur le terrain de la case 0 à 150
            if liste_terrain[i]!=None and liste_terrain[i]!=True:
                if i>=0 and i<=len(liste_terrain)//2:
                    chemin=str('\\')+ str(liste_terrain[i]["age"]) + str('\\ ')
                    chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                    chemin_fichier = os.path.join(chemin_courant, liste_terrain[i]["type_unite"]+str(liste_terrain[i]["joueur"])+'.png')
                    if liste_terrain[i]["joueur"]==0:
                        if "perso"+str(i) not in liste_objet:
                            image(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle((((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle((((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+(((420+(i+1)*10)+(420+((i+1)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
                    else:
                        if "perso"+str(i) not in liste_objet:
                            image(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle((((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle((((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+(((420+i*10)+(420+(i+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
            else:
                while "perso"+str(i) in liste_objet:
                    efface("perso"+str(i))
                    liste_objet.remove("perso"+str(i))
        for j in range(4): #affiche toutes les tourelles appartenant au joueurs 0 ainsi que les supports de tourelles
            if nombre_tourelle[0]>j:
                chemin=str('\\')+ str(Age[0]) + str('\\ ')
                chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                chemin_fichier = os.path.join(chemin_courant, 'support0.png')
                if j==0:
                    if "etourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((20*(hauteur_fenetre()/36))+18*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle0"+str(j))
                        liste_objet.append("etourelle0"+str(j))
                if j==1:
                    if "etourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle0"+str(j))
                        liste_objet.append("etourelle0"+str(j))
                if j==2:
                    if "etourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((14*(hauteur_fenetre()/36))+12*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle0"+str(j))
                        liste_objet.append("etourelle0"+str(j))
                if j==3:
                    if "etourelle0"+str(j) not in liste_objet:
                        image(((3*(largeur_fenetre()/36))+(5*(largeur_fenetre()/36)))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle0"+str(j))
                        liste_objet.append("etourelle0"+str(j))
            if liste_tourelle[0][j]!=None:
                chemin=str('\\')+ str(liste_tourelle[0][j]["age"]) + str('\\ ')
                chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                chemin_fichier = os.path.join(chemin_courant, liste_tourelle[0][j]["type_tourelle"]+'0.png')
                if j==0:
                    if "tourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((20*(hauteur_fenetre()/36))+18*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle0"+str(j))
                        liste_objet.append("tourelle0"+str(j))
                if j==1:
                    if "tourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle0"+str(j))
                        liste_objet.append("tourelle0"+str(j))
                if j==2:
                    if "tourelle0"+str(j) not in liste_objet:
                        image(((6*(largeur_fenetre()/36))+(8*(largeur_fenetre()/36)))//2,((14*(hauteur_fenetre()/36))+12*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle0"+str(j))
                        liste_objet.append("tourelle0"+str(j))
                if j==3:
                    if "tourelle0"+str(j) not in liste_objet:
                        image(((3*(largeur_fenetre()/36))+(5*(largeur_fenetre()/36)))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle0"+str(j))
                        liste_objet.append("tourelle0"+str(j))
        refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
    if screen==1: # meme chose pour la position 1 de l'ecran ce qui exclu les bases, les tourelles
        for iii in range(27*(len(liste_terrain)//150)):
            if "perso"+str(iii) in liste_objet:
                efface("perso"+str(iii))
                liste_objet.remove("perso"+str(iii))
        for jjj in range(len(liste_terrain)-(27*(len(liste_terrain)//150)),len(liste_terrain)):
            if "perso"+str(jjj) in liste_objet:
                efface("perso"+str(jjj))
                liste_objet.remove("perso"+str(jjj))
        if dico_age_niv[Age[0]]>=dico_age_niv[Age[1]]:
            chemin=str('\\')+ str(Age[0]) + str('\\ ')
        else:
            chemin=str('\\')+ str(Age[1]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'fond1.png')
        if "fond"+str(chemin) not in liste_objet:
            for elt in dico_age_niv:
                if elt==chemin:
                    break
                if elt in liste_objet:
                    efface("fond"+str(elt))
                    liste_objet.remove("fond"+str(elt))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="fond"+str(chemin))
            liste_objet.append("fond"+str(chemin))
        chemin=str('\\')+ str(Age[0]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'barre.png')
        if "barre"+Age[0] not in liste_objet:
            for elt in dico_age_niv:
                if elt==Age[0]:
                    break
                if elt in liste_objet:
                    efface("barre"+str(elt))
                    liste_objet.remove("barre"+str(elt))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="barre"+Age[0])
            liste_objet.append("barre"+Age[0])
        for i in range(27*(len(liste_terrain)//150),len(liste_terrain)-(27*(len(liste_terrain)//150))): # affiche toutes les cases de 54 à 246
            if liste_terrain[i]!=None and liste_terrain[i]!=True:
                if i>54 and i<=246:
                    chemin=str('\\')+ str(liste_terrain[i]["age"]) + str('\\ ')
                    chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                    chemin_fichier = os.path.join(chemin_courant, liste_terrain[i]["type_unite"]+str(liste_terrain[i]["joueur"])+'.png')
                    if liste_terrain[i]["joueur"]==0:
                        if "perso"+str(i) not in liste_objet:
                            image((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle(((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle(((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-54)*10)+(((i-54)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
                    else:
                        if "perso"+str(i) not in liste_objet:
                            image((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle(((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle(((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-55)*10)+(((i-55)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
            else:
                if "perso"+str(i) in liste_objet:
                    efface("perso"+str(i))
                    liste_objet.remove("perso"+str(i))
    if screen==2: # meme chose que le screen 0 mais pour le coté droit du terrain avec la base ennemi
        if dico_age_niv[Age[0]]>=dico_age_niv[Age[1]]:
            chemin=str('\\')+ str(Age[0]) + str('\\ ')
        else:
            chemin=str('\\')+ str(Age[1]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'fond2.png')
        if "fond"+str(chemin) not in liste_objet:
            for elt in dico_age_niv:
                if elt==chemin[1:-2]:
                    break
                if "fond"+str('\\')+ str(elt) + str('\\ ') in liste_objet:
                    efface("fond"+str('\\')+ str(elt) + str('\\ '))
                    liste_objet.remove("fond"+str('\\')+ str(elt) + str('\\ '))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="fond"+str(chemin))
            liste_objet.append("fond"+str(chemin))
        chemin=str('\\')+ str(Age[1]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'base.png')
        if "base"+Age[1] not in liste_objet:
            for elt in dico_age_niv:
                if elt==Age[1]:
                    break
                if elt in liste_objet:
                    efface("base"+str(elt))
                    liste_objet.remove("base"+str(elt))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="base"+Age[1])
            liste_objet.append("base"+Age[1])
        chemin=str('\\')+ str(Age[0]) + str('\\ ')
        chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
        chemin_fichier = os.path.join(chemin_courant, 'barre.png')
        if "barre"+Age[0] not in liste_objet:
            for elt in dico_age_niv:
                if elt==Age[0]:
                    break
                if elt in liste_objet:
                    efface("barre"+str(elt))
                    liste_objet.remove("barre"+str(elt))
            image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag="barre"+Age[0])
            liste_objet.append("barre"+Age[0])
        for jj in range(len(liste_terrain)//2):
            if "perso"+str(jj) in liste_objet:
                efface("perso"+str(jj))
                liste_objet.remove("perso"+str(jj))
        for i in range(len(liste_terrain)//2,len(liste_terrain)): # affiche toutes les cases de 150 à 299
            if liste_terrain[i]!=None and liste_terrain[i]!=True:
                if i>=150 and i<len(liste_terrain):
                    chemin=str('\\')+ str(liste_terrain[i]["age"]) + str('\\ ')
                    chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                    chemin_fichier = os.path.join(chemin_courant, liste_terrain[i]["type_unite"]+str(liste_terrain[i]["joueur"])+'.png')
                    if liste_terrain[i]["joueur"]==0:
                        if "perso"+str(i) not in liste_objet:
                            image((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle(((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle(((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[0][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-149)*10)+(((i-149)-liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
                    else:
                        if "perso"+str(i) not in liste_objet:
                            image((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2,(((hauteur_fenetre()//5)*4)+((hauteur_fenetre()//5)*4-200))/2, chemin_fichier,largeur=10*2*liste_terrain[i]["taille"], hauteur=200,tag="perso"+str(i))
                            rectangle(((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)+40,((hauteur_fenetre()//5)*4)-205,remplissage="red",epaisseur=3,tag="perso"+str(i))
                            rectangle(((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-195,((((liste_terrain[i]["points_de_vie"]*100)/joueur_age[1][liste_terrain[i]["age"]]["unites"][liste_terrain[i]["type_unite"]]["points_de_vie"])/100)*80)+((((i-150)*10)+(((i-150)+liste_terrain[i]["taille"])*10))/2)-40,((hauteur_fenetre()//5)*4)-205,remplissage="green",epaisseur=0,tag="perso"+str(i)+str())
                            liste_objet.append("perso"+str(i))
            else:
                if "perso"+str(i) in liste_objet:
                    efface("perso"+str(i))
                    liste_objet.remove("perso"+str(i))
        for j in range(4):
            if nombre_tourelle[1]>j:
                chemin=str('\\')+ str(Age[1]) + str('\\ ')
                chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                chemin_fichier = os.path.join(chemin_courant, 'support1.png')
                if j==0:
                    if "etourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((20*(hauteur_fenetre()/36))+18*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle1"+str(j))
                        liste_objet.append("etourelle1"+str(j))
                if j==1:
                    if "etourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle1"+str(j))
                        liste_objet.append("etourelle1"+str(j))
                if j==2:
                    if "etourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((14*(hauteur_fenetre()/36))+12*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle1"+str(j))
                        liste_objet.append("etourelle1"+str(j))
                if j==3:
                    if "etourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(3*(largeur_fenetre()/36)))+(largeur_fenetre()-(5*(largeur_fenetre()/36))))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="etourelle1"+str(j))
                        liste_objet.append("etourelle1"+str(j))
            if liste_tourelle[1][j]!=None:
                chemin=str('\\')+ str(liste_tourelle[1][j]["age"]) + str('\\ ')
                chemin_courant = os.path.dirname(r'..\proj\image'+chemin)
                chemin_fichier = os.path.join(chemin_courant, liste_tourelle[1][j]["type_tourelle"]+'1.png')
                if j==0:
                    if "tourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((20*(hauteur_fenetre()/36))+18*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle1"+str(j))
                        liste_objet.append("tourelle1"+str(j))
                if j==1:
                    if "tourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle1"+str(j))
                        liste_objet.append("tourelle1"+str(j))
                if j==2:
                    if "tourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(6*(largeur_fenetre()/36)))+(largeur_fenetre()-(8*(largeur_fenetre()/36))))//2,((14*(hauteur_fenetre()/36))+12*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle1"+str(j))
                        liste_objet.append("tourelle1"+str(j))
                if j==3:
                    if "tourelle1"+str(j) not in liste_objet:
                        image(((largeur_fenetre()-(3*(largeur_fenetre()/36)))+(largeur_fenetre()-(5*(largeur_fenetre()/36))))//2,((17*(hauteur_fenetre()/36))+15*(hauteur_fenetre()/36))//2, chemin_fichier,largeur=2*(largeur_fenetre()//36), hauteur=2*(hauteur_fenetre()//36),tag="tourelle1"+str(j))
                        liste_objet.append("tourelle1"+str(j))
        refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age)
    if "txt" not in liste_objet: # affiche l'or et l'exp e n bas a droite de l'ecran en temps reel
        texte(largeur_fenetre()-500,hauteur_fenetre()-50, str(dico_langue[langue][5])+": "+str(int(Or[0])),taille=30, couleur="yellow", ancrage='center',police='Courier',tag="txt")
        texte(largeur_fenetre()-200,hauteur_fenetre()-50, str(dico_langue[langue][6])+": "+str(int(Exp[0])),taille=30, couleur="blue", ancrage='center',police='Courier',tag="txt")
        texte(160,hauteur_fenetre()-50, str(dico_langue[langue][4]),taille=30, couleur="black", ancrage='center',police='Courier',tag="txt")
        liste_objet.append("txt")
    if "bloquer" not in liste_objet: # affiche le petit cadenas sur la troupe verouiller si elle n'est pas deverouiller
        if liste_amelioration[0][0]!=True:
            chemin_courant = os.path.dirname(r'..\proj\image\menu\ ')
            chemin_fichier = os.path.join(chemin_courant, 'cadenas.png')
            image(8*largeur_fenetre()/36,3*hauteur_fenetre()/36+2, chemin_fichier,largeur=int(1.5*(largeur_fenetre()//36)), hauteur=int(1.5*(hauteur_fenetre()//36)),tag="bloquer")
            liste_objet.append("bloquer")
    if liste_amelioration[0][0]==True:
        if "bloquer" in liste_objet:
            efface("bloquer")
            liste_objet.remove("bloquer")
    anime_projectile(liste_projectile,screen,liste_objet_projectile,Age,liste_terrain) # affiche l'animation de tout les projectile se trouvant dans la liste_projectile
    fonction_meteorite(liste_meteorite,screen,liste_terrain,liste_objet_meteorite,Age,Or,Exp,joueur_age,liste_unite_terrain) # affiche l'animation de toutes les meteorites se trouvant dans la liste_meteorite

def refresh_barre_de_vie_base(screen,liste_objet,joueur_age,Age):
    """Cette fonction prend en argument la position de l'ecran, les objet se trouvant sur la fenetre, le dico_age et l'Age des deux joueurs.
       En effet cette fonction met à jour la vie des bases des deux joueurs de la meme maniere que la fonction refresh_barre_de_vie.
       cette fonction ne renvoie rien."""
    while "pv_base" in liste_objet:
        efface("pv_base")
        liste_objet.remove("pv_base")
    if screen==0:
        if "pv_base" not in liste_objet:
            rectangle(10,(hauteur_fenetre()/5)*4,410,(hauteur_fenetre()/5)*4-30,remplissage="red",epaisseur=5,tag="pv_base")
            rectangle(10,(hauteur_fenetre()/5)*4,((((joueur_age[0][Age[0]]["pv_base_ultime"][0]*100)/joueur_age[0][Age[0]]["pv_base_ultime"][1])/100)*400)+10,(hauteur_fenetre()/5)*4-30,remplissage="green",epaisseur=0,tag="pv_base")
            texte(100,(hauteur_fenetre()/5)*4-14, str(int(joueur_age[0][Age[0]]["pv_base_ultime"][0]))+"/"+str(int(joueur_age[0][Age[0]]["pv_base_ultime"][1])), couleur="white", ancrage='center',police='Courier',tag="pv_base")
            liste_objet.append("pv_base")
    if screen==2:
        if "pv_base" not in liste_objet:
            rectangle(largeur_fenetre()-410,(hauteur_fenetre()/5)*4,largeur_fenetre()-10,(hauteur_fenetre()/5)*4-30,remplissage="red",epaisseur=5,tag="pv_base")
            rectangle(largeur_fenetre()-10-((((joueur_age[1][Age[1]]["pv_base_ultime"][0]*100)/joueur_age[1][Age[1]]["pv_base_ultime"][1])/100)*400),(hauteur_fenetre()/5)*4,largeur_fenetre()-10,(hauteur_fenetre()/5)*4-30,remplissage="green",epaisseur=0,tag="pv_base")
            texte(largeur_fenetre()-100,(hauteur_fenetre()/5)*4-14, str(int(joueur_age[1][Age[1]]["pv_base_ultime"][0]))+"/"+str(int(joueur_age[1][Age[1]]["pv_base_ultime"][1])), couleur="white", ancrage='center',police='Courier',tag="pv_base")
            liste_objet.append("pv_base")
    liste_objet.append("pv_base")







def menu_fin(langue,fin,dico_langue):
    """Cette fonction prend en argument la langue utiliser, la fin (gagner ou perdu), ainsi que le dico de tout les mots afficher dans le jeu
       dans toutes les langues. Cette fonction affiche le menu de fin en fonction du gagnant et retourne la fonction la langue pour retourner dans la boucle du main."""
    i,j=12,9
    chemin_courant = os.path.dirname(r'..\proj\image\menu\ ')
    if fin=='perdu':
        chemin_fichier = os.path.join(chemin_courant, 'menu_perdu.png')
    if fin=='gagne':
        chemin_fichier = os.path.join(chemin_courant, 'menu_gagne.png')
    image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre(),tag='fond')
    chemin_fichier = os.path.join(chemin_courant, 'bouton_menu.png')
    image(largeur_fenetre()/2,9*(hauteur_fenetre()/12), chemin_fichier,largeur=3*(largeur_fenetre()//9), hauteur=2*(hauteur_fenetre()//12),tag='fond')
    if fin=='perdu':
        chemin_fichier = os.path.join(chemin_courant, 'perdu.png')
    if fin=='gagne':
        chemin_fichier = os.path.join(chemin_courant, 'gagne.png')
    image(largeur_fenetre()/2,4*(hauteur_fenetre()/12), chemin_fichier,largeur=7*(largeur_fenetre()//9), hauteur=6*(hauteur_fenetre()//12),tag='fond')
    if fin=='perdu':
        texte(largeur_fenetre()/2,4*(hauteur_fenetre()/12), str(dico_langue[langue][8]),taille=150, couleur="black", ancrage='center',police='Courier')
    if fin=='gagne':
        texte(largeur_fenetre()/2,4*(hauteur_fenetre()/12), str(dico_langue[langue][7]),taille=150, couleur="black", ancrage='center',police='Courier')
    texte(largeur_fenetre()/2,9*(hauteur_fenetre()/12), str(dico_langue[langue][4]),taille=80, couleur="white", ancrage='center',police='Courier')
    while 1:
        action=evenement(i,j,0)
        if action=='Quitte':
            return 'Quitte'
        for k in range(8,10):
            for l in range(3,6):
                if action==(k,l):
                    dico_son["son_clic.ogg"].play()
                    return langue

def menu(joueur_age,son=0,langue="france"):
        """Cette fonction prend en argument la liste de dico joueur_age, la variable son pour savoir si il faut relancer la musique du menu
        (0->non lancé,1->deja lancer), et la langue du jeu initaliser à francais"""
        i,j=16,16
        dico_langue={"france":["Jouer","Langue","Francais","Menu","Quitter","OR","EXP","Gagner !","Perdu !","Impossible","Difficile","Intermédiaire","Facile"],"anglais":["Play","Language","English","Menu","Quit","GOLD","XP","Win !","Lost !","Impossible","Hard","Intermediate","Easy"],"allemand":["Spielen","Sprache","Deutsch","Menü","Beenden","GOLD","EP","Gewinnen !","Verloren !","Unmöglich","Schwer","Mittelstufe","Einfach"],"espagnole":["Jugar","Lengua","Español","Menú","Salir","ORO","XP","Ganar !","Perdido !","Imposible","Difícil","Intermedio","Fácil"],"portugais":["Jogar","Língua","Português","Menu","Sair","OURO","XP","Ganhar !","Perdido !","Impossível","Difícil","Intermediário","Fácil"]}
        dico_ia_niv={"0":(1,1),"1":(1.3,0.8),"2":(1.6,0.6),"3":(2,0.4)}
        if son==0:
            dico_son["son_menu.ogg"].play(10)
        chemin_courant = os.path.dirname(r'..\proj\image\menu\ ')
        chemin_fichier = os.path.join(chemin_courant, 'fond_menu.png')
        image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
        chemin_fichier = os.path.join(chemin_courant, 'bouton_play.png')
        image(6.5*(largeur_fenetre()/16), 10*(hauteur_fenetre()/16), chemin_fichier,largeur=5*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, str(langue)+'.png')
        image(11*(largeur_fenetre()/16), 10*(hauteur_fenetre()/16), chemin_fichier,largeur=largeur_fenetre()//8, hauteur=hauteur_fenetre()//8)
        chemin_fichier = os.path.join(chemin_courant, 'age_of_war2.png')
        image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
        chemin_fichier = os.path.join(chemin_courant, 'bouton_exit.png')
        image(largeur_fenetre()/2, 13*(hauteur_fenetre()/16), chemin_fichier,largeur=6*(largeur_fenetre()//16), hauteur=hauteur_fenetre()//8)
        texte(6.5*(largeur_fenetre()/16),10*(hauteur_fenetre()/16), str(dico_langue[langue][0]),taille=40, couleur="white", ancrage='center',police='Courier')
        texte(largeur_fenetre()/2,13*(hauteur_fenetre()/16), str(dico_langue[langue][4]),taille=40, couleur="white", ancrage='center',police='Courier')
        while True:
            action=evenement(i,j,0)
            if action=='Quitte':
                return 'Quitte'
            for k in range(9,11):
                for l in range(4,9):
                    if action==(k,l):
                        dico_son["son_clic.ogg"].play()
                        return menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv) # rentre dans le menu de selection des niveaux
            for kk in range(9,11):
                for ll in range(10,12):
                    if action==(kk,ll):
                        dico_son["son_clic.ogg"].play()
                        res= menu_langue(langue,dico_langue) # rentre dans le mennu de selection de la langue du jeu
                        return res
            for kkk in range(12,14):
                for lll in range(5,11):
                    if action==(kkk,lll):
                        dico_son["son_clic.ogg"].play()
                        ferme_fenetre()
                        return 'Quitte' # quitte le jeu

def menu_langue(langue,dico_langue):
        """Cette fonction prend en argument la langue du jeu et le dico des mots afficher dans le jeu en toutes les langues.
           Cette fonction affiche le menu pour selectionner les langues. Cette fonction retourne le menu avec la nouvelle langue."""
        i,j=16,16
        chemin_courant = os.path.dirname(r'..\proj\image\menu\ ')
        chemin_fichier = os.path.join(chemin_courant, 'menu_langue.png')
        image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
        chemin_fichier = os.path.join(chemin_courant, 'france.png')
        image(2*(largeur_fenetre()/16), 8*(hauteur_fenetre()/16), chemin_fichier,largeur=2*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'anglais.png')
        image(5*(largeur_fenetre()/16), 8*(hauteur_fenetre()/16), chemin_fichier,largeur=2*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'allemand.png')
        image(8*(largeur_fenetre()/16), 8*(hauteur_fenetre()/16), chemin_fichier,largeur=2*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'espagnole.png')
        image(11*(largeur_fenetre()/16), 8*(hauteur_fenetre()/16), chemin_fichier,largeur=2*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'portugais.png')
        image(14*(largeur_fenetre()/16), 8*(hauteur_fenetre()/16), chemin_fichier,largeur=2*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'bouton_exit.png')
        image(largeur_fenetre()/2,12*(hauteur_fenetre()/16), chemin_fichier,largeur=4*(largeur_fenetre()//16), hauteur=2*(hauteur_fenetre()//16))
        chemin_fichier = os.path.join(chemin_courant, 'feuille.png')
        image(largeur_fenetre()/2,4*(hauteur_fenetre()/16), chemin_fichier,largeur=6*(largeur_fenetre()//16), hauteur=4*(hauteur_fenetre()//16))
        texte(largeur_fenetre()/2,4*(hauteur_fenetre()/16), str(dico_langue[langue][1])+": "+str(dico_langue[langue][2]),taille=40, couleur="black", ancrage='center',police='Courier')
        texte(largeur_fenetre()/2,12*(hauteur_fenetre()/16), str(dico_langue[langue][3]),taille=40, couleur="white", ancrage='center',police='Courier')
        mise_a_jour()
        while True:
            action=evenement(i,j,0)
            if action=='Quitte':
                dico_son["son_clic.ogg"].play()
                return 'Quitte'
            for k in range(7,9):
                for l in range(1,3):
                    if action==(k,l):
                        dico_son["son_clic.ogg"].play()
                        return menu_langue("france",dico_langue)
            for kk in range(7,9):
                for ll in range(4,6):
                    if action==(kk,ll):
                        dico_son["son_clic.ogg"].play()
                        return menu_langue("anglais",dico_langue)
            for kkk in range(7,9):
                for lll in range(7,9):
                    if action==(kkk,lll):
                        dico_son["son_clic.ogg"].play()
                        return menu_langue("allemand",dico_langue)
            for kk in range(7,9):
                for ll in range(10,12):
                    if action==(kk,ll):
                        dico_son["son_clic.ogg"].play()
                        return menu_langue("espagnole",dico_langue)
            for kkk in range(7,9):
                for lll in range(13,15):
                    if action==(kkk,lll):
                        dico_son["son_clic.ogg"].play()
                        return menu_langue("portugais",dico_langue)
            for k in range(11,13):
                for l in range(6,11):
                    if action==(k,l):
                        dico_son["son_clic.ogg"].play()
                        return menu(joueur_age,1,langue)

def menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv,ind=0):
    """Cette fonction prend en argument la langue du jeu, la liste de dico des statistiques des joueurs, le dico qui comporte tout les mots affichés
       dans le jeu dans toutes les lengues, le dico de l'ia qui sera choisis et initialiser pour lancer le jeu, et la variable ind qui correspond 
       à un compteur pour la roulette de niveau. Cette fonction retourne le resultat de la fonction jeu."""
    i,j=6,6
    liste_niv=["niv0","niv1","niv2","niv3"]
    chemin_courant = os.path.dirname(r'..\proj\image\menu\ ')
    chemin_fichier = os.path.join(chemin_courant, 'menu_langue.png')
    image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    chemin_fichier = os.path.join(chemin_courant, 'fleche_gauche.png')
    image(1.5*(largeur_fenetre()/6),hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre()//6, hauteur=hauteur_fenetre()//3)
    chemin_fichier = os.path.join(chemin_courant, 'fleche_droite.png')
    image(4.5*(largeur_fenetre()/6),hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre()//6, hauteur=hauteur_fenetre()//3)
    chemin_fichier = os.path.join(chemin_courant, liste_niv[ind]+'.png')
    image(largeur_fenetre()/2,hauteur_fenetre()/2, chemin_fichier,largeur=largeur_fenetre()//3, hauteur=hauteur_fenetre()//3)
    chemin_fichier = os.path.join(chemin_courant, 'gagne.png')
    image(largeur_fenetre()/2,5*(hauteur_fenetre()/6), chemin_fichier,largeur=3*(largeur_fenetre()//6), hauteur=hauteur_fenetre()//6)
    texte(largeur_fenetre()/2,5*(hauteur_fenetre()/6), str(dico_langue[langue][-1-ind]),taille=70, couleur="black", ancrage='center',police='Courier')
    while 1:
        action=evenement(i,j,0)
        if action=='Quitte':
            dico_son["son_clic.ogg"].play()
            return 'Quitte'
        for k in range(2,4):
            for l in range(2,4):
                if action==(k,l):
                    efface_tout()
                    dico_son["son_clic.ogg"].play()
                    ia_initialisation(joueur_age[1],int(liste_niv[ind][3]),dico_ia_niv[liste_niv[ind][3]][0],dico_ia_niv[liste_niv[ind][3]][1]) # initialise l'ia pour lancer le jeu avec la bonne difficulté
                    gagnant=jeu(int(liste_niv[ind][3]),langue,joueur_age,dico_langue)
                    return gagnant # retourne le gagnant
        if action==(2,1) or action==(3,1):
            efface_tout()
            dico_son["son_clic.ogg"].play()
            if ind==0:
                return menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv,3)
            return menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv,ind-1)
        if action==(2,4) or action==(3,4):
            efface_tout()
            dico_son["son_clic.ogg"].play()
            if ind==3:
                return menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv,0)
            return menu_niveau(langue,joueur_age,dico_langue,dico_ia_niv,ind+1)





pygame.init()
dico_son={"son_jeu.gg":pygame.mixer.Sound("son_jeu.ogg"),"son_menu.ogg":pygame.mixer.Sound("son_menu.ogg"),"son_amelioration.ogg":pygame.mixer.Sound("son_amelioration.ogg"),"son_clic.ogg":pygame.mixer.Sound("son_clic.ogg"),"son_debloque.ogg":pygame.mixer.Sound("son_debloque.ogg"),"son_erreur.ogg":pygame.mixer.Sound("son_erreur.ogg"),"son_evolution.ogg":pygame.mixer.Sound("son_evolution.ogg"),"son_hit.ogg":pygame.mixer.Sound("son_hit.ogg"),"son_hit2.ogg":pygame.mixer.Sound("son_hit2.ogg"),"son_meteore.ogg":pygame.mixer.Sound("son_meteore.ogg"),"son_mort.ogg":pygame.mixer.Sound("son_mort.ogg"),"son_mort_char.ogg":pygame.mixer.Sound("son_mort_char.ogg"),"son_mort_char2.ogg":pygame.mixer.Sound("son_mort_char2.ogg"),"son_mort3.ogg":pygame.mixer.Sound("son_mort3.ogg"),"son_mort2.ogg":pygame.mixer.Sound("son_mort2.ogg"),"son_payer.ogg":pygame.mixer.Sound("son_payer.ogg"),"son_projectile.ogg":pygame.mixer.Sound("son_projectile.ogg")}
cree_fenetre(1920, 1080,frequence=60, redimension=True) # cree la fenetre graphique
langue="france" # langue par default
while 1: # boucle du jeu
    pygame.mixer.stop()
    joueur_age = [copy.deepcopy(dico_age), copy.deepcopy(dico_age)] # la liste des deux dico avec les statistiques des deux joueurs
    langue=menu(joueur_age,0,langue) # lance le menu et retourne la langue en cas de retour au menu a pres une fin de partie ou autre
    if langue=='Quitte':
        break
    
    