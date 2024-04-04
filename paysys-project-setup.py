import pyautogui as pa
import time
import clipboard

class PaySysSetup:
    def __init__(self):
        pa.PAUSE = .2

    def play(self):
        self.open_program_by_search('docker')
        self.open_program_by_search('terminal')

    def open_program_by_search(self, program_name):
        pa.press('win')
        pa.write(program_name)
        pa.press('enter')

        time.sleep(.5)

    
setup = PaySysSetup()
setup.play()