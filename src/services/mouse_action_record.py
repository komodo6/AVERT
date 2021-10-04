import time
from pynput import mouse
from src.models.MouseActions import MouseActions
# import logging
# import os

# cwd = os.getcwd()
# log_directory = os.path.join(cwd,"Key_logs")
#
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)
#
# i = 0
# while os.path.exists("mouse_log%s.txt" %i):
#     i += 1
#
# #log_dir = ""
# #logging.basicConfig(filename = (log_dir + "key_log%s.txt" % i), level=logging.INFO, format='%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')
#
# formatter = logging.Formatter('%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')
# def setup_logger(name, log_file, level=logging.INFO):
#     """Function setup as many loggers as you want"""
#
#     handler = logging.FileHandler(log_file)
#     handler.setFormatter(formatter)
#
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.addHandler(handler)
#
#     return logger
#
# mouse_logger = setup_logger('mouse_logger', 'mouse_log%s.txt' %i)
# # Collect events until released
# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener_m:
#     listener_m.join()

# class MouseActionRecord:
#     def test_functionality(self):
#         self.listener.start()
#         with mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener_m:
#             listener_m.join()
#
#     '''
#     When using the non - blocking version below, the current thread will
#     continue executing.This might be necessary when integrating
#     with other GUI frameworks that incorporate a main-loop, but
#     when run from a script, this will cause the program to terminate immediately.
#     '''
#
#     def initiate(self):
#         print("made init")
#         self.running = False
#         self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
#
#     def start(self):
#         self.running = True
#         self.listener.start()
#
#     def stop(self):
#         print('stop')
#         self.running = "False"
#         self.listener.stop()
#
#     def makeClass(self):
#         pass
#
#     def on_move(self,x, y):
#         print("on_move")
#         print(x , ',', y)
#         if not self.running:
#             return False
#         # return False
#
#
#     def on_click(self,x, y, button, pressed):
#         print("on_click")
#         print(x, ',' ,y)
#         print('pressed: ',pressed)
#         print('button: ', button)
#         if not self.running:
#             return False
#         # return False
#
#     def on_scroll(self,x, y, dx, dy):
#
#         print('on_scroll')
#         print(x , ',', y)
#         print('dy', dy)
#         if not self.running:
#             return False
#         # return False
#
#
#     def make_mouse_action(self):
#         # IP
#         # MAC
#         # Time Stamp
#         pass



class MouseActionRecord:
    def test_functionality(self):
        self.listener.start()
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener_m:
            listener_m.join()

    '''
    When using the non - blocking version below, the current thread will
    continue executing.This might be necessary when integrating
    with other GUI frameworks that incorporate a main-loop, but 
    when run from a script, this will cause the program to terminate immediately.
    '''

    def initiate(self):
        print("made init")
        self.running = False
        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    def start(self):
        self.running = True
        self.listener.start()

    def stop(self):
        print('stop')
        self.running = "False"
        self.listener.stop()

    def makeClass(self):
        pass

    def on_move(self,x, y):
        print("on_move")
        print(x , ',', y)
        if not self.running:
            return False
        # return False


    def on_click(self,x, y, button, pressed):
        print("on_click")
        print(x, ',' ,y)
        print('pressed: ',pressed)
        print('button: ', button)
        # if not self.running:
        #     return False
        return False

    def on_scroll(self,x, y, dx, dy):

        print('on_scroll')
        print(x , ',', y)
        print('dy', dy)
        # if not self.running:
        #     return False
        # return False


    def make_mouse_action(self):
        # IP
        # MAC
        # Time Stamp
        pass


# mouse_action_recorder = MouseActionRecord()
# mouse_action_recorder.initiate()
# mouse_action_recorder.start()
# time.sleep(4)
# mouse_action_recorder.stop()
#
#
# time.sleep(4)
# print("Starting 2")
#
# mouse_action_recorder = MouseActionRecord()
# mouse_action_recorder.initiate()
# mouse_action_recorder.start()
# time.sleep(4)
# mouse_action_recorder.stop()

mouse_action_recorder = None

while True:
    print('Beginning----------------------------------------------------------------------------------------\n\n\n\n\n\n\n\n\n')
    time.sleep(4)
    mouse_action_recorder = MouseActionRecord()
    mouse_action_recorder.initiate()
    mouse_action_recorder.start()

    print("Before the sleep")
    time.sleep(4)
    print("after the sleep")

    mouse_action_recorder.stop()




# mouse_action_recorder = None
# user_input = ""
#
# while True:
#     user_input = input("Enter x to stop y to start z to exit")
#
#     if user_input == 'x':
#         mouse_action_recorder.stop()
#         user_input = ""
#
#     if user_input == 'y':
#         mouse_action_recorder = MouseActionRecord()
#         mouse_action_recorder.initiate()
#         mouse_action_recorder.start()
#         user_input = ""
#
#     if user_input == 'z':
#         exit()
