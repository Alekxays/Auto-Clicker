
import pyautogui
from pynput import keyboard, mouse
import time
import random

# États du programme
is_running = False
stop_program = False
config_mode = False  # Mode paramétrage activé/désactivé
coordinates = []  # Liste des coordonnées sauvegardées

# Paramètres de délai
min_delay = 0.8  # Délai minimum entre les clics (en secondes)
max_delay = 2.0  # Délai maximum entre les clics (en secondes)

def on_press(key):
    """Gère les touches pour contrôler le programme."""
    global is_running, stop_program, config_mode, coordinates, min_delay, max_delay

    try:
        if key.char == "s":  # 's' pour démarrer
            is_running = True
            config_mode = False  # Désactive le mode paramétrage en démarrant
            print("Programme démarré.")
        elif key.char == "p":  # 'p' pour mettre en pause
            is_running = False
            print("Programme en pause.")
        elif key.char == "q":  # 'q' pour quitter
            stop_program = True
            is_running = False
            config_mode = False
            print("Programme arrêté.")
            return False  # Arrête le listener
        elif key.char == "c":  # 'c' pour activer le mode paramétrage
            config_mode = not config_mode
            if config_mode:
                print("Mode paramétrage activé. Cliquez pour capturer des coordonnées.")
            else:
                print("Mode paramétrage désactivé.")
        elif key.char == "r":  # 'r' pour réinitialiser les coordonnées
            coordinates.clear()
            print("Coordonnées réinitialisées.")
        elif key.char == "m":  # 'm' pour configurer le délai minimum
            try:
                new_min = float(input("Entrez le délai minimum (en secondes): "))
                if 0.1 <= new_min <= max_delay:
                    min_delay = new_min
                    print(f"Délai minimum défini à {min_delay} secondes.")
                else:
                    print(f"Le délai doit être entre 0.1 et {max_delay} secondes.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        elif key.char == "x":  # 'x' pour configurer le délai maximum
            try:
                new_max = float(input("Entrez le délai maximum (en secondes): "))
                if new_max >= min_delay:
                    max_delay = new_max
                    print(f"Délai maximum défini à {max_delay} secondes.")
                else:
                    print(f"Le délai maximum doit être supérieur à {min_delay} secondes.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    except AttributeError:
        # Ignore les touches spéciales comme Shift ou Ctrl
        pass

def on_click(x, y, button, pressed):
    """Capture les clics en mode paramétrage."""
    global coordinates, config_mode

    if config_mode and pressed:
        coordinates.append((x, y))
        print(f"Coordonnées ajoutées : ({x}, {y})")

def auto_clicker(coords):
    """Effectue des clics sur les coordonnées spécifiées avec délai aléatoire."""
    global is_running, stop_program, min_delay, max_delay

    print("Commandes disponibles :")
    print("  's' : Démarrer")
    print("  'p' : Pause")
    print("  'c' : Mode paramétrage (cliquer pour capturer des coordonnées)")
    print("  'r' : Réinitialiser les coordonnées")
    print("  'm' : Configurer le délai minimum")
    print("  'x' : Configurer le délai maximum")
    print("  'q' : Quitter")
    print(f"Délai actuel : {min_delay}-{max_delay} secondes (aléatoire)")

    while not stop_program:
        if is_running:
            for x, y in coords:
                if stop_program:
                    break
                if not is_running:  # Si le programme est mis en pause
                    break
                pyautogui.click(x, y)
                # Génère un délai aléatoire entre min_delay et max_delay
                random_delay = random.uniform(min_delay, max_delay)
                time.sleep(random_delay)
        else:
            time.sleep(0.1)  # Attente avant de vérifier à nouveau

if __name__ == "__main__":
    # Démarre l'écoute des touches dans un thread séparé
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()

    # Démarre le clic automatique sur les coordonnées avec délai aléatoire
    auto_clicker(coordinates)

    # Attend la fin des listeners
    keyboard_listener.join()
    mouse_listener.join()
    print("Programme complètement arrêté.")
