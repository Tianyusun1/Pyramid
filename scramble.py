def parse_scramble(scramble, pyraminx):
    """
    解析打乱公式，并对金字塔魔方实例执行相应的操作。

    :param scramble: 字符串形式的打乱公式
    :param pyraminx: 金字塔魔方实例
    """
    moves = scramble.split()
    for move in moves:
        if move == "R":
            pyraminx.R_operation()
        elif move == "R'":
            pyraminx.R_prime_operation()
        elif move == "U":
            pyraminx.U_operation()
        elif move == "U'":
            pyraminx.U_prime_operation()
        elif move == "L":
            pyraminx.L_operation()
        elif move == "L'":
            pyraminx.L_prime_operation()
        elif move == "B":
            pyraminx.B_operation()
        elif move == "B'":
            pyraminx.B_prime_operation()
        else:
            print(f"未知的操作: {move}")

