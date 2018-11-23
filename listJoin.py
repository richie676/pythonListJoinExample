import itertools

users = ["user1", "user2", "user3", "user4", "user5", "user6"]
devices = ["EF5001", 'EF5002', "EF5003"]

zipUserDevice = list(zip(users, itertools.cycle(devices)))

print(zipUserDevice)