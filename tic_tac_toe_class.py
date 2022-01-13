#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:57:24 2021

@author: paul
"""


import numpy as np 
from random import randrange


class tic_tac_toe(object):

    def __init__(self):
        self.board = np.zeros((3,3), dtype=int) + 2
        return

    def get_board_state(self):
        
        # Case 1
        board_state = "Game on!"
        board = self.board
        # Case 2
        for i in range(3):
            if (board[:,i] == np.array([1,1,1], dtype=int)).all() or (board[i,:] == np.array([1,1,1], dtype=int)).all():
                board_state = "X wins!"
        if (np.array([board[0,0],board[1,1],board[2,2]]) == np.array([1,1,1], dtype=int)).all():
            board_state = "X wins!"
        if (np.array([board[2,0],board[1,1],board[0,2]]) == np.array([1,1,1], dtype=int)).all():
            board_state = "X wins!"
           
        # Case 3
        for i in range(3):
            if (board[:,i] == np.array([0,0,0], dtype=int)).all() or (board[i,:] == np.array([0,0,0], dtype=int)).all():
                board_state = "O wins!"
        if (np.array([board[0,0],board[1,1],board[2,2]]) == np.array([0,0,0], dtype=int)).all():
            board_state = "O wins!"
        if (np.array([board[2,0],board[1,1],board[0,2]]) == np.array([0,0,0], dtype=int)).all():
            board_state = "O wins!"
    
        # Case 4
        if (board_state == "Game on!") and (2 not in board):
            board_state = "Draw"
        
        return board_state
    
    def get_availiable_moves(self):
        board = self.board
        l = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    l.append((i,j))
        return l
    
    def erace_board(self):
        self.board = np.zeros((3,3), dtype=int) + 2
        return 
    
    def mark_board(self, char, coord):
        """ Mark board"""
        if self.board[coord[0]][coord[1]] == 2:
            self.board[coord[0]][coord[1]] = char 
        else:
            print("Illegal Move")
        return
    

def get_topleft_coord(ttt):
    l = ttt.get_availiable_moves()
    row = int(l[0][0])
    col = int(l[0][1])
    coord = (row, col)
    return coord

def get_random_coord(ttt):
    l = ttt.get_availiable_moves()
    r = randrange(len(l))
    row = int(l[r][0])
    col = int(l[r][1])
    coord = (row, col)
    return coord
    
def get_human_coord(ttt):
    waiting = True       
    while waiting:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if ((row in [0,1,2]) and (col in [0,1,2])) and ttt.board[row][col] == 2:
            coord = (row, col)
            waiting = False
        else:
            print("Not a valid move")     
    return coord

def get_randwin_coord(ttt):
    l = ttt.get_availiable_moves()
    win = False
    for i in range(len(l)):
        current_state = ttt
        current_state.mark_board(0, l[i])
        ns = current_state.get_board_state()
        if ns!="Game on!":
            coord = l[i]
            win = True
    
    if win==False:
        r = randrange(len(l))
        row = int(l[r][0])
        col = int(l[r][1])
        coord = (row, col)
    return coord

    
ttt = tic_tac_toe()
if __name__ == '__main__':
    board_state = ttt.get_board_state()
    print()
    print(ttt.board)
    while board_state == "Game on!":
        ttt.mark_board(1, get_human_coord(ttt))
        print(ttt.board)
        board_state = ttt.get_board_state()
        print()
        if board_state == "Game on!":
            ttt.mark_board(0, get_random_coord(ttt))
            print(ttt.board)
            board_state = ttt.get_board_state()
            print()
    print(ttt.get_board_state())




    
    