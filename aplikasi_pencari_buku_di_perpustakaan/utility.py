from colorama import Fore
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi bantuan
def garis():
    print(Fore.YELLOW + "-" * 50)

def header(text):
    garis()
    print(Fore.CYAN + f"{text.center(50)}")
    garis()
