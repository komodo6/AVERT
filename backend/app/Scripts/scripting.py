# TODO: delete all the below
import pynput
from pynput import mouse 
from pynput.keyboard import Key
from pynput.mouse import Listener, Button, Controller
import datetime
import time
import enum
global keystrokes
global mouseactions
global actions
global left_stop

left_stop = 0

actions = []
mouseactions = []
keystrokes = []

def on_move(x, y):
    global mouseactions
    print('Pointer moved to {0}'.format(
        (x, y)))
    utc = datetime.datetime.utcnow()
    mouseactions = mouseactions + [{'type':'on_move', 'coords':[x,y],'timestamp':utc},]
    

def on_click(x, y, button, pressed):
    global mouseactions
    global left_stop
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    print(left_stop)
    

    but = ''
    if button == Button.right:
        but = 'right'
    if button == Button.left:
        but = 'left'
    
    mouseactions = mouseactions + [{'type':'on_click','coords':[x,y],'button':but, 'pressed': pressed, 'timestamp':datetime.datetime.utcnow()}]

    if button == Button.right :
        left_stop = left_stop + 1
    if left_stop == 4:
        return False

def on_scroll(x, y, dx, dy):
    global mouseactions
    print('Scrolled {0}'.format(
        (x, y)))
    mouseactions = mouseactions + [{'type':'on_scroll', 'coords':[x,y], 'scroll':dy, 'timestamp':datetime.datetime.utcnow()}]

def on_release(key):
    global keystrokes
    print(isinstance(key, enum.Enum)  )
    keystrokes = keystrokes + [{ 'key':key, 'timestamp':datetime.datetime.utcnow()}]
    if key == Key.esc:
        return False

with pynput.keyboard.Listener(on_release=on_release) as k_listener, pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()


# print(mouseactions)
# print()
# print(keystrokes)

# Organizing the two database collection
keystrokes_len = len(keystrokes) -1
current_keystroke_index = 0

mouseactions_len = len(mouseactions) - 1 
current_mouseaction_index = 0

while current_keystroke_index < keystrokes_len or current_mouseaction_index < mouseactions_len:
    # getting the elements from their respective collections for comparisons
    print('in the loop')

    comparison_list = []

    if current_mouseaction_index <= mouseactions_len:
        comparison_list.append({'type':'mouseaction', 'artifact' : mouseactions[current_mouseaction_index]})
    else: 
        comparison_list.append({'type':'mouseaction', 'artifact' : None})
            

    if current_keystroke_index <= keystrokes_len:
        comparison_list.append({'type':'keystroke', 'artifact' : keystrokes[current_keystroke_index]})
    else:
        comparison_list.append({'type':'keystroke', 'artifact' : None})

    # Do the comparisons
    smallest_artifact = comparison_list[0]
    for artifact in comparison_list:
        if smallest_artifact['artifact'] == None:
            smallest_artifact = artifact
            continue

        if artifact['artifact']['timestamp'] < smallest_artifact['artifact']['timestamp']:
            smallest_artifact = artifact
    

    # update the smallest artifact type index
    if smallest_artifact['type'] == 'mouseaction':
        current_mouseaction_index = current_mouseaction_index + 1

    if smallest_artifact['type'] == 'keystroke':
        current_keystroke_index = current_keystroke_index + 1

    # Put the smallest time stamp in the actiosn list {'type of artifact': {artifact it self}}
    actions.append(smallest_artifact)

# making the file
outF = open("myOutFile.py", "w")

# printing the imports
outF.write('from pynput.mouse import Listener, Button, Controller\nfrom pynput.keyboard import Controller as K_Controller\nfrom pynput.keyboard import Key\nimport datetime\nimport time')
outF.write('\n')
# printing the contoller of the mouse action
outF.write('mouse = Controller()\n')
outF.write('keyboard = K_Controller()\n')

prev_time = float(actions[0]['artifact']['timestamp'].strftime("%S.%f"))

for action in actions:
    current_time = float(action['artifact']['timestamp'].strftime("%S.%f"))
    time_diff =  current_time - prev_time
    if action['type'] == 'mouseaction':
        if action['artifact']['type'] == 'on_move':
            x = action['artifact']['coords'][0]
            # print(x)
            y = action['artifact']['coords'][1]
            time_write = 'time.sleep(' + str(time_diff) + ')\n'
            outF.write(time_write)
            postion_write = 'mouse.position = (' + str(x) +','+ str(y) + ')\n'
            outF.write(postion_write)
            # mouse.position = (x,y)

        # if action['type'] == 'on_scroll':
            
        if action['artifact']['type'] == 'on_click':
            if action['artifact']['button'] == 'left':
                button = 'Button.left'
            
            if action['artifact']['button'] == 'right':
                button = 'Button.right'

            time_write = 'time.sleep(' + str(time_diff) + ')\n'
            outF.write(time_write)

            if action['artifact']['pressed'] == True:
                # mouse.press(button)
                press_write = 'mouse.press(' + button + ')\n'
                outF.write(press_write)
            
            if action['artifact']['pressed'] == False:
                # mouse.release(button)
                release_write = 'mouse.release(' + button + ')\n'
                outF.write(release_write)

    if action['type'] == 'keystroke':
        time_write = 'time.sleep(' + str(time_diff) + ')\n'
        outF.write(time_write)

        # # write_key = 
        # type_write = 'keyboard.press(\'{}\')\n'.format(action['artifact']['key'])
        outF.write('keyboard.press({})\n'.format(action['artifact']['key']))
        # type_write = 'keyboard.press(\'{}\')\n'.format(action['artifact']['key'])
        outF.write('keyboard.release({})\n'.format(action['artifact']['key']))
   
    prev_time = current_time




