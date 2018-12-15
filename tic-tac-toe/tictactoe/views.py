from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    if request.method == 'POST':
        newGame = ticTacToe()
        #if 'row' in request.POST:
        row = request.POST['row']
        column = request.POST['column']
        newGame.board[0][0] = request.POST['00']
        newGame.board[0][1] = request.POST['01']
        newGame.board[0][2] = request.POST['02']
        newGame.board[1][0] = request.POST['10']
        newGame.board[1][1] = request.POST['11']
        newGame.board[1][2] = request.POST['12']
        newGame.board[2][0] = request.POST['20']
        newGame.board[2][1] = request.POST['21']
        newGame.board[2][2] = request.POST['22']
        if row != -1:
            temp = newGame.makeMove([row,column], 0)

        bestMove = newGame.nextBestMove()
        if bestMove[0] != -1:
            temp = newGame.makeMove(bestMove, 1)
        content = {
            'temp':temp,
            'row': bestMove[0],
            'column': bestMove[1],
            '00' : newGame.board[0][0],
            '01': newGame.board[0][1],
            '02': newGame.board[0][2],
            '10': newGame.board[1][0],
            '11': newGame.board[1][1],
            '12': newGame.board[1][2],
            '20': newGame.board[2][0],
            '21': newGame.board[2][1],
            '22': newGame.board[2][2],
        }
        return HttpResponse(json.dumps(content),content_type="application/json")
    return render(request, 'tictactoe/index.html')


class ticTacToe:

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def miniMax(self,board,flag):
        temp = self.evaluate(board)
        if temp == 1:
            return 1
        elif temp == -1:
            return -1
        elif temp == 0:
            return 0
        else:
            if flag == 0:
                ret = 10
                for row in range(0, 3):
                    for column in range(0, 3):
                        if board[row][column] == ' ':
                            board[row][column] = 'O'
                            ret = min(ret, self.miniMax(board, 1))
                            board[row][column] = ' '
                return ret
            else:
                ret = -10
                for row in range(0, 3):
                    for column in range(0, 3):
                        if board[row][column] == ' ':
                            board[row][column] = 'x'
                            ret = max(ret, self.miniMax(board, 0))
                            board[row][column] = ' '
                return ret



    def evaluate(self,board):
        # check rows
        if (board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x') or \
                (board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x') or\
                (board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x'):
            return 1
        if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or \
                (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or \
                (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
            return -1

        # check columns
        if (board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x') or \
                (board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x') or \
                (board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x'):
            return 1
        if (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or \
                (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or \
                (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
            return -1

        # check diagonals
        if (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x') or \
                (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x'):
            return 1
        if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
                (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
            return -1

        # If board is full, return 0 else return -2
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == ' ':
                    return -2
        return 0



    def nextBestMove(self):
        ret = -10
        rowBest = -1
        columnBest = -1
        for row in range(0,3):
            for column in range(0,3):
                if self.board[row][column] == ' ':
                    self.board[row][column] = 'x'
                    temp = self.miniMax(self.board,0)
                    if temp > ret:
                        rowBest = row
                        columnBest = column
                        ret = temp
                    self.board[row][column] = ' '
        return [rowBest,columnBest]



    def printBoard(self):
        #ret = "<table>"
        #for row in range(0, 3):
        #    ret += "<tr>"
        #    for column in range(0, 3):
        #        ret += "<td>" + self.board[row][column] + "</td>"
        #    ret += "</tr>"
        #ret += "</table>"
        return self.board



    def makeMove(self,bestMove,flag):
        if flag==0:
            self.board[int(bestMove[0])][int(bestMove[1])] = 'O'
        else:
            self.board[int(bestMove[0])][int(bestMove[1])] = 'x'
        return self.evaluate(self.board)


