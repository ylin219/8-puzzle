#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: yiran Lin
# email:ylin219@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    def __init__(self,board,predecessor,move):
        """contructs a new Sate object by initializing the following four
           attributes.
        """
        self.board=board
        self.predecessor=predecessor
        self.move=move
        self.num_moves=0
        if self.predecessor!=None:
            self.num_moves=self.predecessor.num_moves+1

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s

    def is_goal(self):
        """return True if the called State object is a goal state, and False
           otherwise.
        """
        return self.board.tiles ==GOAL_TILES

    def generate_successors(self):
        """creates and return a list of State objects for all successor state
           of the called State object.
        """
        successors=[]
        for m in MOVES:
            b=self.board.copy()
            if b.move_blank(m)==True:
                newstate=State(b,self,m)
                successors+=[newstate]
        return successors
  
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True

    def print_moves_to(self):
        """prints the sequence of moves that lead from the initial state to
           the called State object.
        """
        if self.move=='init':
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank',self.move+':')
            print(self.board)

