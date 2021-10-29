def directions():
    path = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return path

def menu():
    print("Please select a direction:")
    path = directions()
    for index in range (len(path)):
        print(f"{index} {path[index]}")

def run():
    menu()
if __name__ == "__main__":
    run()

