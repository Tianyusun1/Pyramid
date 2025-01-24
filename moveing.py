def R_operation(state):
    # 中心块
    front_center_2 = state["front"]["centers"][1]
    right_center_3 = state["right"]["centers"][2]
    bottom_center_2 = state["bottom"]["centers"][1]

    state["right"]["centers"][2] = front_center_2
    state["bottom"]["centers"][1] = right_center_3
    state["front"]["centers"][1] = bottom_center_2

    # 棱块
    front_edge_1 = state["front"]["edges"][0]
    front_edge_2 = state["front"]["edges"][1]
    right_edge_2 = state["right"]["edges"][1]
    right_edge_3 = state["right"]["edges"][2]
    bottom_edge_1 = state["bottom"]["edges"][0]
    bottom_edge_2 = state["bottom"]["edges"][1]

    state["right"]["edges"][2] = front_edge_2
    state["right"]["edges"][1] = front_edge_1
    state["bottom"]["edges"][0] = right_edge_2
    state["bottom"]["edges"][1] = right_edge_3
    state["front"]["edges"][0] = bottom_edge_1
    state["front"]["edges"][1] = bottom_edge_2

    return state


def R_prime_operation(state):
    # 中心块
    front_center_2 = state["front"]["centers"][1]
    right_center_3 = state["right"]["centers"][2]
    bottom_center_2 = state["bottom"]["centers"][1]

    state["front"]["centers"][1] = right_center_3
    state["right"]["centers"][2] = bottom_center_2
    state["bottom"]["centers"][1] = front_center_2

    # 棱块
    front_edge_1 = state["front"]["edges"][0]
    front_edge_2 = state["front"]["edges"][1]
    right_edge_2 = state["right"]["edges"][1]
    right_edge_3 = state["right"]["edges"][2]
    bottom_edge_1 = state["bottom"]["edges"][0]
    bottom_edge_2 = state["bottom"]["edges"][1]

    state["front"]["edges"][0] = right_edge_2
    state["front"]["edges"][1] = right_edge_3
    state["right"]["edges"][1] = bottom_edge_1
    state["right"]["edges"][2] = bottom_edge_2
    state["bottom"]["edges"][0] = front_edge_1
    state["bottom"]["edges"][1] = front_edge_2

    return state

def U_operation(state):
    # 中心块
    front_center_1 = state["front"]["centers"][0]
    left_center_1 = state["left"]["centers"][0]
    right_center_1 = state["right"]["centers"][0]

    state["left"]["centers"][0] = front_center_1
    state["right"]["centers"][0] = left_center_1
    state["front"]["centers"][0] = right_center_1

    # 棱块
    front_edge_1 = state["front"]["edges"][0]
    front_edge_3 = state["front"]["edges"][2]
    left_edge_1 = state["left"]["edges"][0]
    left_edge_3 = state["left"]["edges"][2]
    right_edge_1 = state["right"]["edges"][0]
    right_edge_3 = state["right"]["edges"][2]

    state["left"]["edges"][0] = front_edge_1
    state["left"]["edges"][2] = front_edge_3
    state["right"]["edges"][0] = left_edge_1
    state["right"]["edges"][2] = left_edge_3
    state["front"]["edges"][0] = right_edge_1
    state["front"]["edges"][2] = right_edge_3

    return state

def U_prime_operation(state):
    # 中心块
    front_center_1 = state["front"]["centers"][0]
    left_center_1 = state["left"]["centers"][0]
    right_center_1 = state["right"]["centers"][0]

    state["front"]["centers"][0] = left_center_1
    state["left"]["centers"][0] = right_center_1
    state["right"]["centers"][0] = front_center_1

    # 棱块
    front_edge_1 = state["front"]["edges"][0]
    front_edge_3 = state["front"]["edges"][2]
    left_edge_1 = state["left"]["edges"][0]
    left_edge_3 = state["left"]["edges"][2]
    right_edge_1 = state["right"]["edges"][0]
    right_edge_3 = state["right"]["edges"][2]

    state["front"]["edges"][0] = left_edge_1
    state["front"]["edges"][2] = left_edge_3
    state["left"]["edges"][0] = right_edge_1
    state["left"]["edges"][2] = right_edge_3
    state["right"]["edges"][0] = front_edge_1
    state["right"]["edges"][2] = front_edge_3

    return state

def L_operation(state):
    # 中心块
    front_center_3 = state["front"]["centers"][2]
    left_center_2 = state["left"]["centers"][1]
    bottom_center_1 = state["bottom"]["centers"][0]

    state["left"]["centers"][1] = bottom_center_1
    state["front"]["centers"][2] = left_center_2
    state["bottom"]["centers"][0] = front_center_3

    # 棱块
    front_edge_2 = state["front"]["edges"][1]
    front_edge_3 = state["front"]["edges"][2]
    left_edge_1 = state["left"]["edges"][0]
    left_edge_2 = state["left"]["edges"][1]
    bottom_edge_1 = state["bottom"]["edges"][0]
    bottom_edge_3 = state["bottom"]["edges"][2]

    state["left"]["edges"][0] = bottom_edge_3
    state["left"]["edges"][1] = bottom_edge_1
    state["front"]["edges"][1] = left_edge_1
    state["front"]["edges"][2] = left_edge_2
    state["bottom"]["edges"][0] = front_edge_3
    state["bottom"]["edges"][2] = front_edge_2

    return state

def L_prime_operation(state):
    # 中心块
    front_center_3 = state["front"]["centers"][2]
    left_center_2 = state["left"]["centers"][1]
    bottom_center_1 = state["bottom"]["centers"][0]

    state["front"]["centers"][2] = bottom_center_1
    state["left"]["centers"][1] = front_center_3
    state["bottom"]["centers"][0] = left_center_2

    # 棱块
    front_edge_2 = state["front"]["edges"][1]
    front_edge_3 = state["front"]["edges"][2]
    left_edge_1 = state["left"]["edges"][0]
    left_edge_2 = state["left"]["edges"][1]
    bottom_edge_1 = state["bottom"]["edges"][0]
    bottom_edge_3 = state["bottom"]["edges"][2]

    state["front"]["edges"][2] = bottom_edge_1
    state["front"]["edges"][1] = bottom_edge_3
    state["left"]["edges"][0] = front_edge_2
    state["left"]["edges"][1] = front_edge_3
    state["bottom"]["edges"][0] = left_edge_2
    state["bottom"]["edges"][2] = left_edge_1

    return state

def B_operation(state):
    # 中心块
    right_center_2 = state["right"]["centers"][1]
    left_center_3 = state["left"]["centers"][2]
    bottom_center_3 = state["bottom"]["centers"][2]

    state["left"]["centers"][2] = right_center_2
    state["right"]["centers"][1] = bottom_center_3
    state["bottom"]["centers"][2] = left_center_3

    # 棱块
    right_edge_1 = state["right"]["edges"][0]
    right_edge_2 = state["right"]["edges"][1]
    left_edge_2 = state["left"]["edges"][1]
    left_edge_3 = state["left"]["edges"][2]
    bottom_edge_2 = state["bottom"]["edges"][1]
    bottom_edge_3 = state["bottom"]["edges"][2]

    state["left"]["edges"][1] = right_edge_1
    state["left"]["edges"][2] = right_edge_2
    state["right"]["edges"][0] = bottom_edge_2
    state["right"]["edges"][1] = bottom_edge_3
    state["bottom"]["edges"][1] = left_edge_2
    state["bottom"]["edges"][2] = left_edge_3

    return state

def B_prime_operation(state):
    # 中心块
    right_center_2 = state["right"]["centers"][1]
    left_center_3 = state["left"]["centers"][2]
    bottom_center_3 = state["bottom"]["centers"][2]

    state["right"]["centers"][1] = left_center_3
    state["left"]["centers"][2] = bottom_center_3
    state["bottom"]["centers"][2] = right_center_2

    # 棱块
    right_edge_1 = state["right"]["edges"][0]
    right_edge_2 = state["right"]["edges"][1]
    left_edge_2 = state["left"]["edges"][1]
    left_edge_3 = state["left"]["edges"][2]
    bottom_edge_2 = state["bottom"]["edges"][1]
    bottom_edge_3 = state["bottom"]["edges"][2]

    state["right"]["edges"][0] = left_edge_2
    state["right"]["edges"][1] = left_edge_3
    state["left"]["edges"][1] = bottom_edge_2
    state["left"]["edges"][2] = bottom_edge_3
    state["bottom"]["edges"][1] = right_edge_1
    state["bottom"]["edges"][2] = right_edge_2

    return state