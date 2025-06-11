import os
from controller.main_controller import MainControl


def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    start = MainControl()
    start.run()


if __name__ == "__main__":

    main()
