
import pyautogui
from pynput import keyboard, mouse
import time

# États du programme
is_running = False
stop_program = False
config_mode = False  # Mode paramétrage activé/désactivé
coordinates = []  # Liste des coordonnées sauvegardées

def on_press(key):
    """Gère les touches pour contrôler le programme."""
    global is_running, stop_program, config_mode, coordinates

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
    except AttributeError:
        # Ignore les touches spéciales comme Shift ou Ctrl
        pass

def on_click(x, y, button, pressed):
    """Capture les clics en mode paramétrage."""
    global coordinates, config_mode

    if config_mode and pressed:
        coordinates.append((x, y))
        print(f"Coordonnées ajoutées : ({x}, {y})")

def auto_clicker(coords, interval=1.5):
    """Effectue des clics sur les coordonnées spécifiées."""
    global is_running, stop_program

    print("Appuyez sur 's' pour démarrer, 'p' pour mettre en pause, 'c' pour activer le mode paramétrage, 'r' pour réinitialiser, et 'q' pour quitter.")

    while not stop_program:
        if is_running:
            for x, y in coords:
                if stop_program:
                    break
                if not is_running:  # Si le programme est mis en pause
                    break
                pyautogui.click(x, y)
                time.sleep(interval)  # Pause entre chaque clic
        else:
            time.sleep(0.1)  # Attente avant de vérifier à nouveau

if __name__ == "__main__":
    # Démarre l'écoute des touches dans un thread séparé
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()

    # Démarre le clic automatique sur les coordonnées
    auto_clicker(coordinates)

    # Attend la fin des listeners
    keyboard_listener.join()
    mouse_listener.join()
    print("Programme complètement arrêté.")
