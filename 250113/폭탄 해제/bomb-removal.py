unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class mission:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

mission1 = mission(unlock_code, wire_color, seconds)
print("code :", mission1.unlock_code)
print("color :", mission1.wire_color)
print("second :", mission1.seconds)