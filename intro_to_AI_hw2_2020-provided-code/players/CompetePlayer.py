"""
Player for the competition
"""
from players.AbstractPlayer import AbstractPlayer
#TODO: you can import more modules, if needed


class Player(AbstractPlayer):
    def __init__(self, game_time, penalty_score):
        AbstractPlayer.__init__(self, game_time, penalty_score) # keep the inheritance of the parent's (AbstractPlayer) __init__()
        #TODO: initialize more fields, if needed, and the wanted algorithm from SearchAlgos.py


    def set_game_params(self, board):
        """Set the game parameters needed for this player.
        This function is called before the game starts.
        (See GameWrapper.py for more info where it is called)
        input:
            - board: np.array, a 2D matrix of the board.
        No output is expected.
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError
    

    def make_move(self, time_limit, players_score):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement, chosen from self.directions
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError


    def set_rival_move(self, pos):
        """Update your info, given the new position of the rival.
        input:
            - pos: tuple, the new position of the rival.
        No output is expected
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError


    def update_fruits(self, fruits_on_board_dict):
        """Update your info on the current fruits on board (if needed).
        input:
            - fruits_on_board_dict: dict of {pos: value}
                                    where 'pos' is a tuple describing the fruit's position on board,
                                    'value' is the value of this fruit.
        No output is expected.
        """
        #TODO: erase the following line and implement this function. In case you choose not to use this function, 
        # use 'pass' instead of the following line.
        raise NotImplementedError


    ########## helper functions in class ##########
    #TODO: add here helper functions in class, if needed


    ########## helper functions for the search algorithm ##########
    #TODO: add here the utility, succ, and perform_move functions used in AlphaBeta algorithm

# def heuristic_distance_from_goal(board, pos, goal):
#     queue = deque([(pos, 0)])
#     seen = {pos}
#     while queue:
#         pos, distance = queue.popleft()
#         if goal(board[pos]):
#             return 0.75 if distance == 1 else 1 / distance
#         for d in utils.get_directions():
#             i = pos[0] + d[0]
#             j = pos[1] + d[1]
#             if 0 <= i < len(board) and 0 <= j < len(board[0]) and (
#                     board[i][j] not in [-1, 1, 2]) and (i, j) not in seen:
#                 queue.append(((i, j), distance + 1))
#                 seen.add((i, j))
#     return 0