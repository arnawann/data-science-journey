with open("dreams.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line:
            print("Goal:", line)
