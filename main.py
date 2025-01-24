import scramble
import pyramid as py
import V
import Layer

# 创建一个Pyraminx实例并测试其功能
if __name__ == "__main__":
    py = py.Pyraminx()
    scramble_input = input("请输入一条打乱公式：")
    scramble.parse_scramble(scramble_input, py)
    print(py.state)
    V.bfs_solve(py.state)
    Layer.bfs_solve(py.state)


