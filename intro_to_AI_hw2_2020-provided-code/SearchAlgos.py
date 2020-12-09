"""Search Algos: MiniMax, AlphaBeta
"""
from dataclasses import dataclass

from utils import ALPHA_VALUE_INIT, BETA_VALUE_INIT
from time import time
import numpy as np
#TODO: you can import more modules, if needed


class SearchAlgos:
    def __init__(self, utility, succ, perform_move):
        """The constructor for all the search algos.
        You can code these functions as you like to, 
        and use them in MiniMax and AlphaBeta algos as learned in class
        :param utility: The utility function.
        :param succ: The succesor function.
        :param perform_move: The perform move function.
        """
        self.utility = utility
        self.succ = succ
        self.perform_move = perform_move


    def search(self, state, depth, maximizing_player):
        pass


@dataclass(frozen=True)
class State:
    # def __init__(self, board, players_score, player_positions, curr_player, penalty_score):
    #     self.board = board
    #     self.players_score = players_score
    #     self.player_positions = player_positions
    #     self.curr_player = curr_player
    #     self.penalty = penalty_score
    board: np.array
    players_score: tuple
    player_positions: tuple
    curr_player: int
    penalty: int
    direction : tuple




class MiniMax(SearchAlgos):

    def __init__(self, utility, succ, perform_move, start_time, time_limit, heuristic):
        SearchAlgos.__init__(self, utility, succ, perform_move)
        self.start_time = start_time
        self.time_limit = time_limit
        self.heuristic = heuristic

    def search(self, state, depth, maximizing_player) -> (float, State):
        """Start the MiniMax algorithm.
        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """

        if time() - self.start_time > self.time_limit:
            return -1, state.direction

        if depth == 0:
            return self.utility(state, maximizing_player), state.direction #TODO: change this later

        children = self.succ(state)

        if len(children) == 0:
            scores = state.players_score
            scores[state.curr_player] = max(state.players_score[state.curr_player] - state.penalty, 0)
            state = State(state.board.copy(), scores, state.player_positions, state.curr_player, state.penalty, state.direction)
            return self.utility(state, maximizing_player), state.direction

        if maximizing_player:
            curr_max = float("-inf")
            direction = state.direction
            for child in children:
                value, direction = self.search(child, 1 - maximizing_player, depth-1)
                if value > curr_max:
                    curr_max, direction = value, child.direction
            return curr_max, direction
        else:
            curr_min = float("inf")
            for child in children:
                value, direction = self.search(child, 1 - maximizing_player, depth-1)
                if value < curr_min:
                    curr_min, direction = value, child.direction
            return curr_min, None



class AlphaBeta(SearchAlgos):

    def search(self, state, depth, maximizing_player, alpha=ALPHA_VALUE_INIT, beta=BETA_VALUE_INIT):
        """Start the AlphaBeta algorithm.
        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :param alpha: alpha value
        :param: beta: beta value
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError
