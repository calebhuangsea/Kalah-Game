"""
This file implement the decision of AI playing Kalah game,
this program will take in an argument with current game state
and use minimax algorithm with alpha and beta pruning to
return an approximate decision
"""
import time
import random
import io
import math


class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"


class ai:
    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin

    def __init__(self):
        pass

    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately
    def move(self, a, b, a_fin, b_fin, t):
        # To test the execution time, use time and file modules
        # In your experiments, you can try different depth, for example:
        f = open('time.txt', 'a')  # append to time.txt so that you can see running time for all moves.
        # Make sure to clean the file before each of your experiment
        depth = 6  # depth to look into
        # copy a state to pass in the minimax algorithm
        state = self.state(a, b, a_fin, b_fin)
        f.write('depth = ' + str(depth) + '\n')
        t_start = time.time()
        action = self.minimax(state, depth=depth)
        f.write(str(time.time() - t_start) + '\n')
        f.close()
        # r = []
        # for i in range(6):
        #     if a[i] != 0:
        #         r.append(i)
        # return r[random.randint(0, len(r)-1)]
        return action
        # But remember in your final version you should choose only one depth according to your CPU speed (TA's is
        # 3.4GHz) and remove timing code.hh

    # takes in a current state and the depth to look into, and return an action calculated by minimax algorithm
    # state(state class): the game information
    # depth(int): how many levels do we want to look into
    # return(int): next action for AI
    def minimax(self, state, depth):
        # example: doing nothing but wait 0.1*depth sec
        # time.sleep(0.1*depth)
        (action, _) = self.maxVal(state, -math.inf, math.inf, depth)
        return action

    # the level for our turn
    # return(action, v-value)
    def maxVal(self, state, alpha, beta, depth):
        if depth == 0 or not any(state.a) or not any(state.b):  # terminate not because score over
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, self.heuristic(state)
        if state.a_fin > 36:  # terminate if a wins
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, math.inf
        if state.b_fin > 36:  # terminate if b wins
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, -math.inf
        val = -math.inf
        action = -1
        for (action_, landing, state_) in self.successors(state, True):
            if landing:  # if it is AI's turn again, not decrease depth
                (_, val_) = self.maxVal(state_, alpha, beta, depth)
                if val_ > val:
                    val = val_
                    action = action_
            else:  # if it is opponent's turn, decrease depth
                (_, val_) = self.minVal(state_, alpha, beta, depth - 1)
                if val_ > val:
                    val = val_
                    action = action_
            if val >= beta:  # cutoff, pruning
                return action, val
            alpha = max(alpha, val)
        return action, val

    # the level for opponent's turn
    # return(action, v-value)
    def minVal(self, state, alpha, beta, depth):
        if depth == 0 or not any(state.a) or not any(state.b):  # terminate not because score over
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, self.heuristic(state)
        if state.a_fin > 36:  # terminate if a wins
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, math.inf
        if state.b_fin > 36:  # terminate if b wins
            for i in range(6):  # assign a random step if the ai is not making decision
                if state.a[i] != 0:
                    return i, self.heuristic(state)
            return -1, -math.inf
        val = math.inf
        # iterate through each successor
        action = -1
        for (action_, landing, state_) in self.successors(state, False):
            if landing:  # if it is opponent's turn again
                (_, val_) = self.minVal(state_, alpha, beta, depth)
                if val_ < val:
                    val = val_
                    action = action_
            else:  # if it is AI's turn
                (_, val_) = self.maxVal(state_, alpha, beta, depth - 1)
                if val_ < val:
                    val = val_
                    action = action_
            if val <= alpha:  # cutoff, pruning
                return action, val
            beta = min(beta, val)
        return action, val

    # takes in a current game state and return a heuristic value
    # state(state class): current state that we want to evaluate
    # return(int): heuristic value
    def heuristic(self, state):
        if state.a_fin>36 or (sum(state.b)==0 and sum(state.a)+state.a_fin>36): # ai wins
            return 1000000 # Returns a large number
        if state.b_fin>36 or (sum(state.a)==0 and sum(state.b)+state.b_fin>36): # opponent wins
            return -1000000 # Return a small number
        num = 5 # If the ith hole has 6-i stones (mod13), pick this hole gives the player an extra turn, give this a score
        score = 0 # Count the score
        for i in range(6):
            if state.a[i]%13==6-i: # The ith hole has 6-i stones, pick this hole gives ai and extra turn, add num*i to the score
                score+=num
            if state.b[i]%13==6-i: # Same thing for the opponent
                score-=num
        weight = 7 # The weight of the stones in the kalah
        stone_num=1 # The weight of the number of stones in holes
        return score+(state.a_fin-state.b_fin)*weight+(sum(state.a)-sum(state.b))*stone_num


    # find all valid successors for AI or opponent
    # state(state class): current state that we want to evaluate
    # return(list[(index, landing, state)]), list of index, whether landing in kalah and state
    def successors(self, state, turn):
        result = []
        if turn:  # it is our turn
            for i in range(len(state.a)):
                if state.a[i] != 0:  # if it is a valid move
                    temp, land = self.movement(state, i)
                    result.append((i, land, temp))
        else:  # it is opponent's turn
            for i in range(len(state.a)):
                #  we need to reverse the list order because of the layout and player turn
                if state.b[::-1][i] != 0:  # if it is a valid move
                    temp = self.state(state.b[::-1], state.a[::-1], state.b_fin, state.a_fin)
                    temp, land = self.movement(temp, i)
                    oppo = self.state(temp.b[::-1], temp.a[::-1], temp.b_fin, temp.a_fin)
                    result.append((i, land, oppo))
        return result

    # according to the state and index, update and return a new state
    # state(state class): current state that we want to evaluate
    # return(state, landing): new state and whether it is landing in kalah
    def movement(self, state, index):
        temp = self.state(state.a[:], state.b[:], state.a_fin, state.b_fin)
        steps = temp.a[index]
        temp.a[index] = 0
        index += 1
        mod = -1
        for i in range(steps):  # iterate through every steps
            mod = index % 13
            if mod == 6:  # if it is landing on our kalah
                temp.a_fin += 1
            elif mod < 6:  # if it is landing on our board
                temp.a[mod] += 1
            else:  # if it is landing in our opponent's board
                temp.b[12 - mod] += 1
            index += 1
        if not any(temp.a):  # if our side is empty, we let opponent collect all points
            for i in range(6):
                temp.b_fin += temp.b[i]
                temp.b_fin = 0
                return temp, False
        if mod == 6:  # if we land on our kalah finally
            return temp, True
        if steps == 13 or mod < 6 and steps < 13 and state.a[mod] == 0:  # if we land on an empty spot, we take points
            score = state.a[mod] + state.b[mod]
            temp.a_fin += score
            temp.a[mod] = 0
            temp.b[mod] = 0
        return temp, False
