n = int(input())
resident = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    resident.append((n_i, s_i, r_i))

resident.sort(reverse = True, key = lambda x : x[0])


class Resident:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

person = Resident(resident[0][0], resident[0][1], resident[0][2])
print("name", person.name)
print("addr", person.street_address)
print("city", person.region)