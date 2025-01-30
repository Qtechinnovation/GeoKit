import os


def main():
    while True:
        command = input("Enter a command: ")
        if command.lower() == "sides":
            os.system("python sides.py")
        elif command.lower() == "angles":
            os.system("python angles.py")
        elif command.lower() == "measures":
            os.system("python measures.py")
        elif command.lower() == "exit":
            break
        else:
            print("Unknown command. Valid commands: sides (finds the number of sides from the measure of a single interior angle of a regular polygon), angles (finds the measure of a single interior angle from the number of sides of a regular polygon), measures (finds the sum of the measures of the interior angles of a polygon)")


if __name__ == "__main__":
    main()
