secret_code, meeting_point, time = input().split()
time = int(time)

class encode:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

case1 = encode(secret_code, meeting_point, time)
print("secret code :", case1.secret_code)
print("meeting point :", case1.meeting_point)
print("time :", case1.time)