import inputs
import threading
from time import sleep

class XboxController:
    MAX_JOY_VAL = 32767  # Maximum joystick value
    MAX_TRIG_VAL = 255   # Maximum trigger value

    def __init__(self):
        self.LeftJoystickX = 0
        self.LeftJoystickY = 0
        self.RightJoystickX = 0
        self.RightJoystickY = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

    def truncate(f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d + '0' * n)[:n]])

    def read(self):
        xl = self.LeftJoystickX
        yl = self.LeftJoystickY
        xr = self.RightJoystickX
        yr = self.RightJoystickY
        a = self.A
        b = self.B  # b=1, x=2
        x = self.X
        y = self.Y
        rb = self.RightBumper
        LeftTrigger = self.LeftTrigger
        RightTrigger = self.RightTrigger
       # truncate(f, n) value is f and places is n
        if 0.2 > RightTrigger > -0.2:
            RightTrigger = 0
        if 0.2 > LeftTrigger > -0.2:
            LeftTrigger = 0
        if 0.2 > xl > -0.2:
            xl = 0
        if 0.2 > xr > -0.2:
            xr = 0
        if 0.2 > yl > -0.2:
            yl = 0
        if 0.2 > yr > -0.2:
            yr = 0
        space = "    "
        return [xl, yl, space, xr, yr, space, a, b, x, y, LeftTrigger, RightTrigger]

    def _monitor_controller(self):
        while True:
            events = inputs.get_gamepad()  # Fetch gamepad events
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize joystick value
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize joystick value
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize joystick value
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize joystick value
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize trigger value
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize trigger value
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

    def start(self):
        self._monitor_thread = threading.Thread(target=self._monitor_controller)
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def stop(self):
        self._monitor_thread.join()

# Instantiate and start monitoring
xbox_controller = XboxController()
xbox_controller.start()

# Print controller state every 1 second
while True:
    #values pulled
    #formatted as
    #[xl, yl, space, xr, yr, space, a, b, x, y, rb]
    valuelist = xbox_controller.read()
    LeftX = valuelist[0]
    LeftY = valuelist[1]
    RightX = valuelist[3]
    RightY = valuelist[4]
    AButton = valuelist[6]
    BButton = valuelist[7]
    XButton = valuelist[8]
    yButton = valuelist[9]
    #print("left x: {LeftX:.2f} left y: {LeftY::.2f}\n")
    print("left x: {0} left y: {1}\n".format(LeftX, LeftY))

    #print(xbox_controller.read())
    sleep(1)
