class GameLogic:
    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game

    '''
    def placeStone(self):
        # keep track of intersections on the board
        # check if intersection is free
            # if it is, call other methods, to check the rules and
            # if they are false, allow to place the stone in the intersection
            # if not, deny placing stone and user can place somewhere else.
        
                
    def capture(self):
        # keep track of intersections on the board
        # check if a piece of a color (A) placed on the board makes a piece of another color (B) to be
        # completely surrounded
            # if it does, check if piece A is being surrounded by pieces of the same color as the
            # piece to be captured (B)
                # --> if it is, remove piece of color B and apply KO
                # --> if it is not, just remove piece of color B
    
    def eye(self):
        # keep track of intersections on the board
        # if there is an empty intersection entirely surrounded by pieces of the same color, there is
        # an eye of this color --> which is "independently alive"
        # otherwise, if there is an empty intersection surrounded by pieces of both colors, it is not
        # "independently alive" --> which means that it can interfere in both ways (affect both)
        
    # def suicide(self):
        # keep track of intersections on the board
        # check for eyes that are independently alive
        # do not allow a piece to be placed into an opponent's eye that is independently alive
            # --> player must place piece on another intersection or pass
    
    def seki(self):
        # keep track of intersections on the board
        # prevent from being captured, by creating eyes that are not independently alive
    
    def ko(self):
        # keep track of the current state of the board for each player
                # read as --> keep track of the state of the board of the two last moves
        # if player 1 captures a piece, it is not possible for player 2 to regain their territory/position
        # right after. It is necessary to wait at least one turn to make a move that will return the board
        # to a state it was before
        #the board cannot return to the state it was before immediately after a move is made  
        
    def endGame(self):
        # check for passes
        # if there are two consecutive passes, the game is over
        
    '''