import Memory_handler
import keyboard
import pyautogui
import pygetwindow as gw
import time

def getWindowPosition():
    # Set the title of the "Path of Exile" window
    window_title = "Path of Exile"

    # Find the window by title
    poewindow = gw.getWindowsWithTitle(window_title)

    if poewindow:
        # Activate first the Path of Exile window
        poewindow[0].activate()

        #Setting up the coordinates
        poewindow = poewindow[0]  # Assuming there is only one window with the specified title
        window_x, window_y, window_width, window_height = poewindow.left, poewindow.top, poewindow.width, poewindow.height

        # Calculate the middle of the window
        middle_x = window_x + window_width // 2
        middle_y = window_y + window_height // 2
    else:
        middle_x, middle_y = None

    return middle_x, middle_y

# Get window position for logout
middle_x, middle_y = getWindowPosition()

while True:

    try:
        current_hp = Memory_handler.getCurrentHealth()
        maximum_hp = Memory_handler.getMaximumHealth()
        current_mana = Memory_handler.getCurrentMana()
        maximum_mana = Memory_handler.getMaximumMana()
        current_energyshield = Memory_handler.getCurrentEnergyShield()
        maximum_energyshield = Memory_handler.getMaximumEnergyShield()
    except:
        print("No memory value")
        break

    time.sleep(1)
    #print("HP:   ", current_hp, "/", maximum_hp)
    #print("MANA:   ",current_mana ,"/", maximum_mana)
    #print("ES:   ", current_energyshield ,"/", maximum_energyshield)


    # TAKE POTION
    if current_hp <= maximum_hp * 0.5 and current_hp > maximum_hp * 0.25:
        # assuming flask is at hotkey 1
        keyboard.press_and_release("1")
        print("potion taken at", current_hp)

    # If your character uses energy shields instead of health.
    #if current_energyshield <= maximum_energyshield * 0.5:
    #    # assuming flask is at hotkey 1, this can be any flask.
    #    keyboard.press_and_release("1")
    #    print("potion taken at", current_energyshield)

    # ADD more features depending on your build
    
    # LOGOUT
    #if current_hp <= maximum_hp * 0.35:
    #    keyboard.press_and_release("ESC")

        # Move the mouse to the middle of the POE window
    #    pyautogui.moveTo(middle_x, middle_y - 20)  # Can adjust the duration if needed
    #    pyautogui.leftClick()

    #    print("Saved ur ass at", current_hp, "!!!")

    # EXIT LOOP
    if keyboard.is_pressed("l"):
        print("Exiting...")
        break
