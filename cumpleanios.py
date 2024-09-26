import time
import os

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_decorations():
    print(" " + "*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 17 + "🎉🎂 FELIZ CUMPLEAÑOS 🎂🎉" + " " * 4 + "*")
    print("*" + " " * 48 + "*")
    print(" " + "*" * 50)

def hearts_decorator():
    print("\n".join([
        "      *****       *****       *****",
        "   *********** *********** ***********",
        "  *******************************",
        "   *****************************",
        "    ***************************",
        "      ***********************",
        "        *******************",
        "          ***************",
        "            ***********",
        "              *******",
        "                ***",
        "                 *"
    ]))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    hearts_decorator()
    time.sleep(1)
    print_with_delay("\n\nTe deseo un día lleno de alegría y amor. 💕\n", 0.1)
    time.sleep(1)
    draw_decorations()
    print_with_delay("\n¡Que todos tus sueños se hagan realidad!\n", 0.1)
    draw_decorations()
    time.sleep(1)
    hearts_decorator()

if __name__ == "__main__":
    main()
