from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

vitesse = Vector2D(1,1)
shoot = Vector2D(1,1)
act1 = SoccerAction(vitesse,shoot)
act2 = SoccerAction(2*vitesse,2*shoot)
#print (act1.acceleration, act1.shoot)
# Possibilite de combiner les actions :
act_new = act1 + act2

#Stratégie Fonceur
class Fonceur(Strategy):
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)

    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
        vb= state.ball.position                             #position du ballon (vecteur 2d)
        v1= state.player_state(idteam,idplayer).position    #position du joueur (vecteur 2d)
        if (idteam==1):
            v2= Vector2D(150,45)
        if (idteam==2):
            v2= Vector2D(0,45)
        return SoccerAction(vb-v1,v2-vb)    
        #return SoccerAction(vitesse,shoot)
        
#Stratégie Défenseur
class Défenseur(Strategy):
    def __init__(self,name="ma strategie"):
        Strategy.__init__(self,name)

    def compute_strategy(self,state,idteam,idplayer):
        #faire qqe chose d intelligent
        vb= state.ball.position                             #position du ballon (vecteur 2d)
        v1= state.player_state(idteam,idplayer).position    #position du joueur (vecteur 2d)
        v3=vb-v1
        if (idteam==1):
            v2= Vector2D(150,45)
            if (vb.x>75):
                v3=0
        if (idteam==2):
            v2= Vector2D(0,45)
            if (vb.x<75):
                v3=0
        return SoccerAction(v3,v2-vb)    
        #return SoccerAction(vitesse,shoot)           

# Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))

# Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

#Choix de Strat
team1.add("Zlatan",Fonceur())
team2.add("Paul",Défenseur())

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)