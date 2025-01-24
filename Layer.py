"""
V是什么？

首先，V应该保证一个面三个中心为一个颜色，同时有两个棱块也为这个颜色；
比如黄色V就应该是3个黄色中心+2个黄色棱块，但是如果是3个黄色中心+3个黄色棱块这也是V但是是V的特殊情况
"""
import moveing
from collections import deque
import copy

def apply_move(state, move):
    # 此处为简化展示，仅实现部分操作，请根据实际情况补充完整
    new_state = copy.deepcopy(state)
    if move == "R":
        new_state = moveing.R_operation(new_state)
    elif move == "R'":
        new_state = moveing.R_prime_operation(new_state)
    if move == "l":
        new_state = moveing.L_operation(new_state)
    elif move == "L'":
        new_state = moveing.L_prime_operation(new_state)
    if move == "B":
        new_state = moveing.B_operation(new_state)
    elif move == "B'":
        new_state = moveing.B_prime_operation(new_state)
    if move == "U":
        new_state = moveing.U_operation(new_state)
    elif move == "U'":
        new_state = moveing.U_prime_operation(new_state)

    return new_state


def check_Layer(state, face, color):
    centers = state[face]['centers']
    edges = state[face]['edges']
    if state["bottom"]["centers"][1] != "yellow" or state["bottom"]["centers"][2] != "yellow" or state["bottom"]["centers"][0] != "yellow":
        return False
    count1 = sum(1 for e in edges if e == color)
    if count1 == 3:
        if state[face]["edges"][0] == color and state[face]["edges"][1] == color and state[face]["edges"][2] == color:
            if state["front"]["edges"][1] == "green" and state["right"]["edges"][1] == "blue" :
                return True
            else:
                return False
    else:
        return False



def bfs_solve(initial_state, target_face='bottom', target_color='yellow'):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(str(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if check_Layer(current_state, target_face, target_color):
            print("解决方案步骤:", path)
            print(current_state)
            return path

        moves = ["R", "R'","L", "L'", "U", "U'", "B", "B'"]
        for move in moves:
            new_state = apply_move(current_state, move)
            state_str = str(new_state)
            if state_str not in visited:
                visited.add(state_str)
                queue.append((new_state, path + [move]))
    print("无法找到解决方案")
    return []