import math
from inputs import get_gamepad
import threading
from time import sleep
#source for this code, used to learn threading and object names.
#https://stackoverflow.com/questions/46506850/how-can-i-get-input-from-an-xbox-one-controller-in-python
class Controller():
    def __init__(self):
        #initializing all of our first variables.
        #we need to read their intakes.
        #joysticks, LX, LY, RX, RY
        self.LeftJoystickY = 0
        self.LeftJoystickx = 0
        self.RightJoystickX = 0
        self.RightJoystickY = 0
        #bumpers,LR
        self.RightBumper = 0
        self.LeftBumper = 0
        #triggers, LR
        self.LeftTrigger = 0
        self.RightTrigger = 0
        #buttons, ABXY
        self.A = 0
        self.B = 0
        self.Y = 0
        self.X = 0
        #thumbs, Righthumb, LeftThumb
        self.LeftThumb = 0
        self.RightThumb = 0
        #dpad, up,down,left,right
        self.UpDPad = 0
        self.DownDPad = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        #back and start
        self.Start = 0
        self.Back = 0
        #implement threading here
        self.monitor_thread = threading.Thread(target = self._monitor_controller, args=())

    def controller_read(self):
        leftx = self.LeftJoystickx
        lefty = self.LeftJoystickY
        rightx = self.RightJoystickX
        righty = self.RightJoystickY
        #set them into two lists
        #take in left stick and return left_coord (x, y)
        #take in right stick and return right_coord (x, y)
        left_coord = (leftx, lefty)
        right_coord = (rightx, righty)
        joysticks = (leftx, lefty, rightx, righty)
        buttona = self.A
        buttonb = self.B
        buttonx = self.X
        buttony = self.Y
        #take buttons and return in list as (a, b, x, y)
        buttons = (buttona, buttonb, buttonx, buttony)
        right_bumper = self.RightBumper
        left_bumper = self.LeftBumper
        #we're returning the bumpers in a list as bumpers = (left, right)
        bumpers = (right_bumper, left_bumper)
        complete = (joysticks, buttons, bumpers)
        #complete is a list of lists, needs to be unpacked later.
        return complete
    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / Controller.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / Controller.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / Controller.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / Controller.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / Controller.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / Controller.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state  # previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state  # previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state

if __name__ == '__main__':
    readings = Controller()
    while True:
        print(readings.controller_read())
        sleep(1)


