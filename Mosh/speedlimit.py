def check_speed(speed):
    limit = 70
    points = 0
    if speed <= limit:
        print("Ok")
    else:
        for i in range(limit, speed, 5):
            points += 1
        if points > 12:
            print("License suspended")
        else:
            print("Points:", (points))


check_speed(120)
