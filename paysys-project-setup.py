import pyautogui as pa
import time
import clipboard

class PaySysSetup:
    def __init__(self):
        pa.PAUSE = .2

    def play(self):
        self.open_program_by_search('docker')
        self.open_program_by_search('terminal')

        self.open_neovim_project('/mnt/d/Files/Projects/paysys-backend/')
        self.open_new_terminal_window()

    def open_program_by_search(self, program_name):
        pa.press('win')
        pa.write(program_name)
        pa.press('enter')

        time.sleep(.5)

    def write_in_terminal(self, command):
        clipboard.copy(command)
        pa.hotkey('ctrl', 'v')
        pa.press('enter')

        time.sleep(.5)

    def open_neovim_project(self, project_path):
        self.write_in_terminal(f'cd {project_path}')
        self.write_in_terminal('nvim ./')

        pa.press('enter')
        pa.press('enter')

    def open_new_terminal_window(self):
        pa.hotkey('ctrl', 'shift', '5')
        time.sleep(.5)

    def create_tmux_session(self, session_name):
        pa.write(f'tmux new -s {session_name}')
        pa.press('enter')

        time.sleep(.5)


    
setup = PaySysSetup()
setup.play()