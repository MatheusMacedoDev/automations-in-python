import pyautogui as pa
import time
import clipboard

class PaySysSetup:
    def __init__(self):
        self.project_path = '/mnt/d/Files/Projects/paysys-backend/'

        pa.PAUSE = .2

    def play(self):

        self.open_program_by_search('docker')
        self.open_program_by_search('terminal')

        self.open_neovim_project(self.project_path)

        self.startTmux()

    def startTmux(self):
        self.open_new_terminal_window()

        self.execute_in_terminal(f'cd {self.project_path}')

        self.create_tmux_session('Backend')
        self.close_tmux_session()
        self.create_tmux_session('Commands')

    def open_program_by_search(self, program_name):
        pa.press('win')
        pa.write(program_name)
        pa.press('enter')

        time.sleep(.5)

    def execute_in_terminal(self, command):
        clipboard.copy(command)
        pa.hotkey('ctrl', 'v')
        pa.press('enter')

        time.sleep(.5)

    def open_neovim_project(self, project_path):
        self.execute_in_terminal(f'cd {project_path}')
        self.execute_in_terminal('nvim ./')

        pa.press('enter')
        pa.press('enter')

    def open_new_terminal_window(self):
        pa.hotkey('ctrl', 'shift', '5')
        time.sleep(.5)

    def create_tmux_session(self, session_name):
        pa.write(f'tmux new -s {session_name}')
        pa.press('enter')

        time.sleep(.5)

    def close_tmux_session(self):
        pa.hotkey('ctrl', 'b')
        time.sleep(.5)
        pa.press('d')


    
setup = PaySysSetup()
setup.play()