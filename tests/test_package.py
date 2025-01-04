# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:27:41 2025

@author: hlocke
"""

import pyai_abalone
import numpy as np


def check_list(some_list, entry_type):
    assert isinstance(some_list, list)
    for entry in some_list:
        assert isinstance(entry, entry_type)


def test_numpy_abalone():
    abal = pyai_abalone.NumpyAbalone()

    pot_states, move_ids = abal.calc_nonlosing_moves()
    check_list(pot_states, np.ndarray)
    check_list(move_ids, int)

    abal.set_board_state(pot_states[0])
    pot_states = abal.calc_possible_moves()
    check_list(pot_states, np.ndarray)

def test_magister_play():
    magi_zero = pyai_abalone.get_trained_magister_zero()
    
    # test with limited depth
    magi_play = pyai_abalone.MagisterPlay(
        model=magi_zero,
        starting_position=pyai_abalone.constants.BELGIAN_DAISY,
        prob_sum=0.95,
        num_mcts=20,
        depth_mcts=11,
        num_threads=4
        )
    next_state = np.array([
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 2, 2, 0, 1, 1, 3],
        [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3],
        [3, 3, 3, 0, 2, 2, 0, 1, 1, 0, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 1, 0, 0, 0, 0, 3, 3],
        [3, 0, 1, 1, 0, 2, 2, 0, 3, 3, 3],
        [3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
        [3, 0, 1, 0, 2, 2, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ],
        dtype=np.int16)
    
    magi_play.make_given_move(next_state)
    magi_play.make_ai_move()
    magi_play.stop_execution()
    
    # test with maximum depth
    magi_play = pyai_abalone.MagisterPlay(
        model=magi_zero,
        starting_position=pyai_abalone.starting_positions.BELGIAN_DAISY,
        prob_sum=0.95,
        num_mcts=10,
        depth_mcts=0,  # simulations will be played until the games finish
        num_threads=4
        )
    magi_play.make_ai_move()
    magi_play.stop_execution()

    