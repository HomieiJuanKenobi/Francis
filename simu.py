from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction, PlayerState, Ball
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator import mdpsoccer
from football import *
import math
#============================================================================== 
#class Observer(object):
#    MAX_STEP=50
#    def __init__(self,simu):
#        self.simu = simu
#        self.simu.listeners += self 
#        #ajout de lobserver
#    def begin_match(self,team1,team2,state):
#        #initialisation des parametres ...
#        self.last, self.cpt, self.cpt_tot = 0, 0, 0, 
#    def begin_round(self,team1,team2,state):
#        self.simu.state.states[(1,0)].position = Vector2D(130,45)
#        self.simu.state.ball.position = Vector2D(130,45)
#        self.last = self.simu.step
#    def update_round(self,team1,team2,state):
#        if self.simu.step>self.last+self.MAX_STEP: 
#            self.simu.end_round()
#    def end_round(self,team1,team2,state):
#        if state.goal>0: 
#            self.cpt+=1
#            self.cpt_tot+=1
#            self.res= self.cpt*1./self.cpt_tot
#        print(self.res)
##        if self.simu.step == self.MAX_STEP: #fin de la simu
##            print(self.res)
##            self.simu.end_match()
#============================================================================== 
##Simulation
##Creation d'une equipe
#team1 = SoccerTeam(name="team1",login="etu1")
#team2 = SoccerTeam(name="team2",login="etu2")
#
##Choix de Strat
##team1.add("Fonceur_dribbleur",Fonceur_dribbleur())
#team1.add("Campeur_proche",Campeur_proche())
#team1.add("Gardien",Gardien())
#team2.add("Gardien",Gardien())
#team2.add("Fonceur",Fonceur())
#
##Creation d'une partie
#simu = Simulation(team1,team2, max_steps=2000)
##Jouer et afficher la partie
##Observer(simu)
#show_simu(simu) 
#============================================================================== 
#states_1= {(1,0): PlayerState(position=Vector2D(,0),vitesse= Vector2D(0,0)),
#           (2,0): PlayerState(position=Vector2D(0,0),vitesse= Vector2D(0,0))}
#           
#monstate=SoccerState(states=states_1,ball=Ball(Vector2D((settings.GAME_WIDTH)/2,(settings.GAME_HEIGHT)/2),Vector2D()))
#team1 = SoccerTeam(name="team1",login="etu1")
#team2 = SoccerTeam(name="team2",login="etu2")
#team1.add("Campeur_proche",Campeur_proche())
#team2.add("Fonceur",Fonceur())
#simu=Simulation(team1, team2, initial_state=monstate, max_steps=20)
#show_simu(simu)
#
##reset()
##get_initial_state()
# 
#==============================================================================