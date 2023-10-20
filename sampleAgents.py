# sampleAgents.py
# parsons/07-oct-2017
#
# Version 1.1
#
# Some simple agents to work with the PacMan AI projects from:
#
# http://ai.berkeley.edu/
#
# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.
#
# As required by the licensing agreement for the PacMan AI we have:
#
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agents here are extensions written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import util
import math

# RandomAgent
#
# A very simple agent. Just makes a random pick every time that it is
# asked for an action.
class RandomAgent(Agent):

    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # Random choice between the legal options.
        return api.makeMove(random.choice(legal), legal)

# RandomishAgent
#
# A tiny bit more sophisticated. Having picked a direction, keep going
# until that direction is no longer possible. Then make a random
# choice.
class RandomishAgent(Agent):

    # Constructor
    #
    # Create a variable to hold the last action
    def __init__(self):
         self.last = Directions.STOP
    
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # If we can repeat the last action, do it. Otherwise make a
        # random choice.
        if self.last in legal:
            return api.makeMove(self.last, legal)
        else:
            pick = random.choice(legal)
            # Since we changed action, record what we did
            self.last = pick
            return api.makeMove(pick, legal)

# SensingAgent
#
# Doesn't move, but reports sensory data available to Pacman
class SensingAgent(Agent):

    def getAction(self, state):

        # Demonstrates the information that Pacman can access about the state
        # of the game.

        # What are the current moves available
        legal = api.legalActions(state)
        print "Legal moves: ", legal

        # Where is Pacman?
        pacman = api.whereAmI(state)
        print "Pacman position: ", pacman

        # Where are the ghosts?
        print "Ghost positions:"
        theGhosts = api.ghosts(state)
        for i in range(len(theGhosts)):
            print theGhosts[i]

        # How far away are the ghosts?
        print "Distance to ghosts:"
        for i in range(len(theGhosts)):
            print util.manhattanDistance(pacman,theGhosts[i])

        # Where are the capsules?
        print "Capsule locations:"
        print api.capsules(state)
        
        # Where is the food?
        print "Food locations: "
        print api.food(state)

        # Where are the walls?
        print "Wall locations: "
        print api.walls(state)
        
        # getAction has to return a move. Here we pass "STOP" to the
        # API to ask Pacman to stay where they are.
        return api.makeMove(Directions.STOP, legal)

class GoWestAgent(Agent):
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # Random choice between the legal options.
        move = "West"
        if move not in legal:
            move = random.choice(legal)
        return api.makeMove(move, legal)

class HungryAgent(Agent):

    def getAction(self, state):

        # Demonstrates the information that Pacman can access about the state
        # of the game.

        # # What are the current moves available
        # legal = api.legalActions(state)
        # print "Legal moves: ", legal

        # # Where is Pacman?
        # pacman = api.whereAmI(state)
        # print "Pacman position: ", pacman

        # # Where are the ghosts?
        # print "Ghost positions:"
        # theGhosts = api.ghosts(state)
        # for i in range(len(theGhosts)):
        #     print theGhosts[i]

        # # How far away are the ghosts?
        # print "Distance to ghosts:"
        # for i in range(len(theGhosts)):
        #     print util.manhattanDistance(pacman,theGhosts[i])

        # # Where are the capsules?
        # print "Capsule locations:"
        # print api.capsules(state)
        
        # # Where is the food?
        # print "Food locations: "
        # print api.food(state)

        # # Where are the walls?
        # print "Wall locations: "
        # print api.walls(state)
        
        # Find location of nearest food
        pacman = api.whereAmI(state)
        food = api.food(state)
        for meal in food :
            if meal[0] == pacman[0] :
                if meal[1] == pacman[1] + 1 :
                    return api.makeMove("North", api.legalActions(state))
                if meal[1] == pacman[1] - 1 :
                    return api.makeMove("South", api.legalActions(state))
            if meal[1] == pacman[1] :
                if meal[0] == pacman[0] + 1 :
                    return api.makeMove("East", api.legalActions(state))
                if meal[0] == pacman[0] - 1 :
                    return api.makeMove("West", api.legalActions(state))
            if meal[0] > pacman[0] :
                if meal[1] > pacman[1] :
                    if "East" in api.legalActions(state) :
                        if random.choice([True, False]) :
                            break
                        return api.makeMove("East", api.legalActions(state))
                        if "North" in api.legalActions(state) :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("North", api.legalActions(state))
                        else :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("South", api.legalActions(state))
                else :
                    if "East" in api.legalActions(state) :
                        if random.choice([True, False]) :
                            break
                        return api.makeMove("East", api.legalActions(state))
                        if "South" in api.legalActions(state) :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("South", api.legalActions(state))
                        else :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("North", api.legalActions(state))
            else :
                if meal[1] > pacman[1] :
                    if "West" in api.legalActions(state) :
                        if random.choice([True, False]) :
                            break
                        return api.makeMove("West", api.legalActions(state))
                        if "North" in api.legalActions(state) :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("North", api.legalActions(state))
                        else :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("South", api.legalActions(state))
                else :
                    if "West" in api.legalActions(state) :
                        if random.choice([True, False]) :
                            break
                        return api.makeMove("West", api.legalActions(state))
                        if "South" in api.legalActions(state) :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("South", api.legalActions(state))
                        else :
                            if random.choice([True, False]) :
                                break
                            return api.makeMove("North", api.legalActions(state))

class CornerSeekingAgent:
    def __init__(self):
        self.initran = False
        self.targetCorner = (0,0)
        self.currentPos = (0,0)
    def getAction(self, state):
        if self.initran == False:
            cornerList = api.corners(state)
            currentPos = api.whereAmI(state)
            # a^2 + b^2 = c^2 so find the distance to each corner and pick the smallest
            currentDistance = 99999999
            for corner in cornerList :
                cornerDistance = math.sqrt((corner[0] - currentPos[0])**2 + (corner[1] - currentPos[1])**2)
                print str(self.targetCorner) + " is target corner"
                if cornerDistance < currentDistance :
                    currentDistance = cornerDistance
                    self.targetCorner = corner
            # Now we have the closest corner, we need to move towards it
            self.currentPos = api.whereAmI(state)
            if self.targetCorner[0] > 1 and self.targetCorner[1] > 1 :
                self.targetCorner = (self.targetCorner[0] - 1, self.targetCorner[1] -1)
            elif self.targetCorner[0] > 1 and self.targetCorner[1] < 1 :
                self.targetCorner = (self.targetCorner[0] - 1, self.targetCorner[1] + 1)
            elif self.targetCorner[0] < 1 and self.targetCorner[1] > 1 :
                self.targetCorner = (self.targetCorner[0] + 1, self.targetCorner[1] - 1)
            else:
                self.targetCorner = (self.targetCorner[0] + 1, self.targetCorner[1] + 1)
            self.initran = True
        self.currentPos = api.whereAmI(state)
        print str(self.currentPos) + " is current pos"
        if self.targetCorner[0] > self.currentPos[0] :
            if "East" in api.legalActions(state) :
                return api.makeMove("East", api.legalActions(state))
            elif "North" in api.legalActions(state) :
                return api.makeMove("North", api.legalActions(state))
            elif "South" in api.legalActions(state) :
                return api.makeMove("South", api.legalActions(state))
        if self.targetCorner[0] < self.currentPos[0] :
            if "West" in api.legalActions(state) :
                return api.makeMove("West", api.legalActions(state))
            elif "North" in api.legalActions(state) :
                return api.makeMove("North", api.legalActions(state))
            elif "South" in api.legalActions(state) :
                return api.makeMove("South", api.legalActions(state))
        if self.targetCorner[1] > self.currentPos[1] :
            if "North" in api.legalActions(state) :
                return api.makeMove("North", api.legalActions(state))
            elif "East" in api.legalActions(state) :
                return api.makeMove("East", api.legalActions(state))
            elif "West" in api.legalActions(state) :
                return api.makeMove("West", api.legalActions(state))
        if self.targetCorner[1] < self.currentPos[1] :
            if "South" in api.legalActions(state) :
                return api.makeMove("South", api.legalActions(state))
            elif "East" in api.legalActions(state) :
                return api.makeMove("East", api.legalActions(state))
            elif "West" in api.legalActions(state) :
                return api.makeMove("West", api.legalActions(state))