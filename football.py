from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction, PlayerState, Ball
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator import mdpsoccer
from tools import *
import math

#Strategie Aleatoire
class Aleatoire(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))
         
#Strategie Fonceur
class Fonceur(Strategy):
     def __init__(self):
         Strategy.__init__(self,"Fonceur")
         self.comportement=Comportement(Attaque_fonceur_base,Attaque_fonceur_base,Selection_1)
     def compute_strategy(self,state,id_team,id_player):
         return Joueur(MyState(state,id_team,id_player),self.comportement)

#Strategie Passeur
class Passeur(Strategy):
     def __init__(self):
         Strategy.__init__(self,"Passeur")
         self.comportement=Comportement(Attaque_passeur,Attaque_passeur,Selection_1)
     def compute_strategy(self,state,id_team,id_player):
         return Joueur(MyState(state,id_team,id_player),self.comportement)
     
#Strategie Campeur-Defenseur
class Campeur_proche(Strategy):
     def __init__(self):
         Strategy.__init__(self,"Campeur_proche")
         self.comportement=Comportement(Attaque_dribbleur_2v2,Attaque_campeur_proche_2v2,Selection_2)
     def compute_strategy(self,state,id_team,id_player):
         return Joueur(MyState(state,id_team,id_player),self.comportement) 
         
#Strategie Fonceur-Dribbleur
class Fonceur_dribbleur(Strategy):
     def __init__(self):
         Strategy.__init__(self,"Fonceur_dribbleur")
         self.comportement=Comportement(Attaque_fonceur_1v1,Attaque_dribbleur_1v1,Selection_3)
     def compute_strategy(self,state,id_team,id_player):
         return Joueur(MyState(state,id_team,id_player),self.comportement)
         
#Strategie Passeur-Defenseur
class Gardien(Strategy):
     def __init__(self):
         Strategy.__init__(self,"Gardien")
         self.comportement=Comportement(Attaque_fonceur_2v2,Defense_gardien_2v2,Selection_1)
     def compute_strategy(self,state,id_team,id_player):
         return Joueur(MyState(state,id_team,id_player),self.comportement)