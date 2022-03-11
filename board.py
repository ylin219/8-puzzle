#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: yiran Lin
# email:ylin219@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c]=int(digitstr[3*r+c])
                if int(digitstr[3*r+c])==0:
                    self.blank_r=r
                    self.blank_c=c
    

    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object"""
        s=''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]==0:
                    s+='_ '
                else:
                    s+=str(self.tiles[r][c])+' '
            s+='\n'
        return s

    def move_blank(self,direction):
        """takes as input a string direction that specifies the direction in
           which the blank should move, and that attempts to modify the contents
           of the called Board object accordingly. return True or False to
           indicate whether the requested move was possible.
        """
        if direction not in ['up','down','left','right']:
            print('unknown direction:',direction)
            return False
        else:
            newrow=0
            newcol=0
            if direction=='up':
                if self.blank_r-1 <0:
                    return False
                else:
                    newrow=self.blank_r-1
                    newcol=self.blank_c
            elif direction=='down':
                if self.blank_r+1>len(self.tiles)-1:
                    return False
                else:
                    newrow=self.blank_r+1
                    newcol=self.blank_c
            elif direction=='left':
                if self.blank_c-1<0:
                    return False
                else:
                    newrow=self.blank_r
                    newcol=self.blank_c-1
            elif direction=='right':
                if self.blank_c+1>len(self.tiles[0])-1:
                    return False
                else:
                    newrow=self.blank_r
                    newcol=self.blank_c+1
        newcor=self.tiles[newrow][newcol]
        self.tiles[newrow][newcol]=0
        self.tiles[self.blank_r][self.blank_c]=newcor
        self.blank_r=newrow
        self.blank_c=newcol
        return True

    def digit_string(self):
        """returns a string of digits that corresponds to the current contents
           of the called Board object's tiles atrribute.
        """
        s=''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s+=str(self.tiles[r][c])
        return s

    def copy(self):
        """returns a newly-contructed Board object that is a deep copy of the
           called object.
        """
        copyboard=Board(self.digit_string())
        return copyboard

    def num_misplaced(self):
        """counts and return the number of tiles in the called Board object
           that are not where they should be in the goal state.
        """
        stringdigit=self.digit_string()
        count=0
        for i in range(len(stringdigit)):
            if stringdigit[i]!=str(i):
                count+=1
        return count-1

    def man(self):
        """return the misplaced number."""
        s=[]
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s+=[[self.tiles[r][c],r,c]]
        s=sorted(s)
        return s
                      
    
    def __eq__(self,other):
        """overloads the == operator, creating a version of the operator that
           works for Board objects. Return True if the called object and the
           arugent have the same value for the tiles attribute, and False
           otherwise.
        """
        if self.digit_string()==other.digit_string():
            return True
        else:
            return False
        
