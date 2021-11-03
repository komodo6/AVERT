import datetime
import pynput
from pynput import mouse 
from pynput.keyboard import Key
from pynput.mouse import Listener, Button, Controller
import pymongo
from operator import itemgetter
client = pymongo.MongoClient(host="54.215.46.201", port=27017)
db = client.AVERT
def make_script(start_range, end_range):
    mouseactions = []
    keystrokes = []
    actions = []

    range = {
        "timestamp":{
            "$gte" : start_range ,
            "$lt": end_range   
        }
    }

    ma  = db.MouseActions.find(range).sort('timestamp')
    not_dups = []
    for doc in ma:
        doc_time_stamp = doc['timestamp']
        if doc_time_stamp not in not_dups:
            mouseactions.append(doc)
            not_dups = not_dups + [doc_time_stamp]
    # print(mouseactions)

    k = db.Keystrokes.find(range).sort('timestamp')
    # k = db.Keystrokes.aggregate({}).sort('timestamp')
    # putting the documents in the keystorkes
    not_dups = []
    for doc in k:
        doc_time_stamp = doc['timestamp']
        if doc_time_stamp not in not_dups:
            keystrokes.append(doc)
            not_dups = not_dups + [doc_time_stamp]
    # keystrokes = sorted(keystrokes, key=itemgetter('timestamp'))
    # print(keystrokes)


    # Organizing the two database collection
    keystrokes_len = len(keystrokes) -1
    current_keystroke_index = 0

    mouseactions_len = len(mouseactions) - 1 
    current_mouseaction_index = 0

    while current_keystroke_index < keystrokes_len or current_mouseaction_index < mouseactions_len:
        # getting the elements from their respective collections for comparisons
        # print('in the loop')

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
            if artifact['artifact'] == None:
                smallest_artifact = smallest_artifact
                continue
            try:
                if artifact['artifact']['timestamp'] < smallest_artifact['artifact']['timestamp']:
                    smallest_artifact = artifact
            except TypeError:
                # print('smallest_artifact:', smallest_artifact )
                # print('artifact:', artifact)
                exit()

            

        # update the smallest artifact type index
        if smallest_artifact['type'] == 'mouseaction':
            current_mouseaction_index = current_mouseaction_index + 1

        if smallest_artifact['type'] == 'keystroke':
            current_keystroke_index = current_keystroke_index + 1

        # Put the smallest time stamp in the actiosn list {'type of artifact': {artifact it self}}
        actions.append(smallest_artifact)

    # for action in actions:
    #     print('type', action['type'])
    #     print('timesstamp',action['artifact']['timestamp'])


    # making the file
    outF = open("myOutFile.py", "w")

    # printing the imports
    outF.write('from pynput.mouse import Listener, Button, Controller\nfrom pynput.keyboard import Controller as K_Controller\nfrom pynput.keyboard import Key\nimport datetime\nimport time')
    outF.write('\n')
    # printing the contoller of the mouse action
    outF.write('mouse = Controller()\n')
    outF.write('keyboard = K_Controller()\n')

    # prev_time = float(actions[0]['artifact']['timestamp'].strftime("%S.%f"))
    prev_time = datetime.datetime.strptime(actions[0]['artifact']['timestamp'],"%Y-%m-%d %H:%M:%S.%f")
    prev_artifact = actions[0]['artifact'] # TODO: Delete
    for action in actions:
        # current_time = float(datetime.datetime.strptime(action['artifact']['timestamp'],"%Y-%m-%d %H:%M:%S.%f").strftime("%S.%f"))
        current_time = datetime.datetime.strptime(action['artifact']['timestamp'],"%Y-%m-%d %H:%M:%S.%f")
        current_artifact = action['artifact'] # TODO: Delete
        time_diff =  current_time - prev_time
        time_diff = time_diff.total_seconds()
        if time_diff < 0:
            print('in if time_diff <=0:')
            print()
            print(time_diff)
            print()
            print('prev_artifact: ', prev_artifact)
            print()
            print(prev_artifact['timestamp'])
            print()
            print('current_artifact: ', current_artifact)
            print()
            print(current_artifact['timestamp'])
            print()


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
                print(action['artifact'])
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
        prev_artifact = current_artifact


# make_script('2021-11-03 06:36:08.627853', '2021-11-03 06:36:21.087659')

