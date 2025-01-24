class Pyraminx:
    def __init__(self):
        # 初始化金字塔魔方的状态
        self.state = {
            "front": {
                "centers": ["green", "green", "green"],  # 前面3个中心块
                "edges": ["green", "green", "green"]  # 前面3个棱块
            },
            "bottom": {
                "centers": ["yellow", "yellow", "yellow"],  # 底面3个中心块
                "edges": ["yellow", "yellow", "yellow"]  # 底面3个棱块
            },
            "left": {
                "centers": ["red", "red", "red"],  # 左面3个中心块
                "edges": ["red", "red", "red"]  # 左面3个棱块
            },
            "right": {
                "centers": ["blue", "blue", "blue"],  # 右面3个中心块
                "edges": ["blue", "blue", "blue"]  # 右面3个棱块
            }
        }

    def print_state(self):
        # 输出当前状态
        for face, face_info in self.state.items():
            print(f"{face.capitalize()} 面: 中心块 = {face_info['centers']}, 棱块 = {face_info['edges']}")

    def R_operation(self):
        # 中心块
        front_center_2 = self.state["front"]["centers"][1]
        right_center_3 = self.state["right"]["centers"][2]
        bottom_center_2 = self.state["bottom"]["centers"][1]

        self.state["right"]["centers"][2] = front_center_2
        self.state["bottom"]["centers"][1] = right_center_3
        self.state["front"]["centers"][1] = bottom_center_2

        # 棱块
        front_edge_1 = self.state["front"]["edges"][0]
        front_edge_2 = self.state["front"]["edges"][1]
        right_edge_2 = self.state["right"]["edges"][1]
        right_edge_3 = self.state["right"]["edges"][2]
        bottom_edge_1 = self.state["bottom"]["edges"][0]
        bottom_edge_2 = self.state["bottom"]["edges"][1]

        self.state["right"]["edges"][2] = front_edge_2
        self.state["right"]["edges"][1] = front_edge_1
        self.state["bottom"]["edges"][0] = right_edge_2
        self.state["bottom"]["edges"][1] = right_edge_3
        self.state["front"]["edges"][0] = bottom_edge_1
        self.state["front"]["edges"][1] = bottom_edge_2

    def R_prime_operation(self):
        # 中心块
        front_center_2 = self.state["front"]["centers"][1]
        right_center_3 = self.state["right"]["centers"][2]
        bottom_center_2 = self.state["bottom"]["centers"][1]

        self.state["front"]["centers"][1] = right_center_3
        self.state["right"]["centers"][2] = bottom_center_2
        self.state["bottom"]["centers"][1] = front_center_2

        # 棱块
        front_edge_1 = self.state["front"]["edges"][0]
        front_edge_2 = self.state["front"]["edges"][1]
        right_edge_2 = self.state["right"]["edges"][1]
        right_edge_3 = self.state["right"]["edges"][2]
        bottom_edge_1 = self.state["bottom"]["edges"][0]
        bottom_edge_2 = self.state["bottom"]["edges"][1]

        self.state["front"]["edges"][0] = right_edge_2
        self.state["front"]["edges"][1] = right_edge_3
        self.state["right"]["edges"][1] = bottom_edge_1
        self.state["right"]["edges"][2] = bottom_edge_2
        self.state["bottom"]["edges"][0] = front_edge_1
        self.state["bottom"]["edges"][1] = front_edge_2

    def U_operation(self):
        # 中心块
        front_center_1 = self.state["front"]["centers"][0]
        left_center_1 = self.state["left"]["centers"][0]
        right_center_1 = self.state["right"]["centers"][0]

        self.state["left"]["centers"][0] = front_center_1
        self.state["right"]["centers"][0] = left_center_1
        self.state["front"]["centers"][0] = right_center_1

        # 棱块
        front_edge_1 = self.state["front"]["edges"][0]
        front_edge_3 = self.state["front"]["edges"][2]
        left_edge_1 = self.state["left"]["edges"][0]
        left_edge_3 = self.state["left"]["edges"][2]
        right_edge_1 = self.state["right"]["edges"][0]
        right_edge_3 = self.state["right"]["edges"][2]

        self.state["left"]["edges"][0] = front_edge_1
        self.state["left"]["edges"][2] = front_edge_3
        self.state["right"]["edges"][0] = left_edge_1
        self.state["right"]["edges"][2] = left_edge_3
        self.state["front"]["edges"][0] = right_edge_1
        self.state["front"]["edges"][2] = right_edge_3

    def U_prime_operation(self):
        # 中心块
        front_center_1 = self.state["front"]["centers"][0]
        left_center_1 = self.state["left"]["centers"][0]
        right_center_1 = self.state["right"]["centers"][0]

        self.state["front"]["centers"][0] = left_center_1
        self.state["left"]["centers"][0] = right_center_1
        self.state["right"]["centers"][0] = front_center_1

        # 棱块
        front_edge_1 = self.state["front"]["edges"][0]
        front_edge_3 = self.state["front"]["edges"][2]
        left_edge_1 = self.state["left"]["edges"][0]
        left_edge_3 = self.state["left"]["edges"][2]
        right_edge_1 = self.state["right"]["edges"][0]
        right_edge_3 = self.state["right"]["edges"][2]

        self.state["front"]["edges"][0] = left_edge_1
        self.state["front"]["edges"][2] = left_edge_3
        self.state["left"]["edges"][0] = right_edge_1
        self.state["left"]["edges"][2] = right_edge_3
        self.state["right"]["edges"][0] = front_edge_1
        self.state["right"]["edges"][2] = front_edge_3

    def L_operation(self):
        # 中心块
        front_center_3 = self.state["front"]["centers"][2]
        left_center_2 = self.state["left"]["centers"][1]
        bottom_center_1 = self.state["bottom"]["centers"][0]

        self.state["left"]["centers"][1] = bottom_center_1
        self.state["front"]["centers"][2] = left_center_2
        self.state["bottom"]["centers"][0] = front_center_3

        # 棱块
        front_edge_2 = self.state["front"]["edges"][1]
        front_edge_3 = self.state["front"]["edges"][2]
        left_edge_1 = self.state["left"]["edges"][0]
        left_edge_2 = self.state["left"]["edges"][1]
        bottom_edge_1 = self.state["bottom"]["edges"][0]
        bottom_edge_3 = self.state["bottom"]["edges"][2]

        self.state["left"]["edges"][0] = bottom_edge_3
        self.state["left"]["edges"][1] = bottom_edge_1
        self.state["front"]["edges"][1] = left_edge_1
        self.state["front"]["edges"][2] = left_edge_2
        self.state["bottom"]["edges"][0] = front_edge_3
        self.state["bottom"]["edges"][2] = front_edge_2

    def L_prime_operation(self):
        # 中心块
        front_center_3 = self.state["front"]["centers"][2]
        left_center_2 = self.state["left"]["centers"][1]
        bottom_center_1 = self.state["bottom"]["centers"][0]

        self.state["front"]["centers"][2] = bottom_center_1
        self.state["left"]["centers"][1] = front_center_3
        self.state["bottom"]["centers"][0] = left_center_2

        # 棱块
        front_edge_2 = self.state["front"]["edges"][1]
        front_edge_3 = self.state["front"]["edges"][2]
        left_edge_1 = self.state["left"]["edges"][0]
        left_edge_2 = self.state["left"]["edges"][1]
        bottom_edge_1 = self.state["bottom"]["edges"][0]
        bottom_edge_3 = self.state["bottom"]["edges"][2]

        self.state["front"]["edges"][2] = bottom_edge_1
        self.state["front"]["edges"][1] = bottom_edge_3
        self.state["left"]["edges"][0] = front_edge_2
        self.state["left"]["edges"][1] = front_edge_3
        self.state["bottom"]["edges"][0] = left_edge_2
        self.state["bottom"]["edges"][2] = left_edge_1

    def B_operation(self):
        # 中心块
        right_center_2 = self.state["right"]["centers"][1]
        left_center_3 = self.state["left"]["centers"][2]
        bottom_center_3 = self.state["bottom"]["centers"][2]

        self.state["left"]["centers"][2] = right_center_2
        self.state["right"]["centers"][1] = bottom_center_3
        self.state["bottom"]["centers"][2] = left_center_3

        # 棱块
        right_edge_1 = self.state["right"]["edges"][0]
        right_edge_2 = self.state["right"]["edges"][1]
        left_edge_2 = self.state["left"]["edges"][1]
        left_edge_3 = self.state["left"]["edges"][2]
        bottom_edge_2 = self.state["bottom"]["edges"][1]
        bottom_edge_3 = self.state["bottom"]["edges"][2]

        self.state["left"]["edges"][1] = right_edge_1
        self.state["left"]["edges"][2] = right_edge_2
        self.state["right"]["edges"][0] = bottom_edge_2
        self.state["right"]["edges"][1] = bottom_edge_3
        self.state["bottom"]["edges"][1] = left_edge_2
        self.state["bottom"]["edges"][2] = left_edge_3

    def B_prime_operation(self):
        # 中心块
        right_center_2 = self.state["right"]["centers"][1]
        left_center_3 = self.state["left"]["centers"][2]
        bottom_center_3 = self.state["bottom"]["centers"][2]

        self.state["right"]["centers"][1] = left_center_3
        self.state["left"]["centers"][2] = bottom_center_3
        self.state["bottom"]["centers"][2] = right_center_2

        # 棱块
        right_edge_1 = self.state["right"]["edges"][0]
        right_edge_2 = self.state["right"]["edges"][1]
        left_edge_2 = self.state["left"]["edges"][1]
        left_edge_3 = self.state["left"]["edges"][2]
        bottom_edge_2 = self.state["bottom"]["edges"][1]
        bottom_edge_3 = self.state["bottom"]["edges"][2]

        self.state["right"]["edges"][0] = left_edge_2
        self.state["right"]["edges"][1] = left_edge_3
        self.state["left"]["edges"][1] = bottom_edge_2
        self.state["left"]["edges"][2] = bottom_edge_3
        self.state["bottom"]["edges"][1] = right_edge_1
        self.state["bottom"]["edges"][2] = right_edge_2
