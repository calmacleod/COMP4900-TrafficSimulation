import PySimpleGUI as sg
import CONSTANTS

class Data_Entry:
    def __init__(self):
        return

    def get_book_variable_module_name(self,module_name):
        module = globals().get(module_name, None)
        book = {}
        if module:
            book = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
        return book

    def data_entry(self):
        layout = [
            [sg.Text('Main Menu:')],
            [sg.Text('Delta', size=(15,1)), sg.InputText(key='DELTA')],
            [sg.Text('Stopping Distance', size=(15,1)), sg.InputText(key='STOPPING_DISTANCE')],
            [sg.Text('Max Speed', size=(15,1)), sg.InputText(key='MAX_SPEED')],
            [sg.Text('Reaction Time', size=(15,1)), sg.InputText(key='REACTION_TIME')],
            [sg.Text('Accleration', size=(15,1)), sg.InputText(key='ACCELERATION')],
            [sg.Text('Bus Length', size=(15,1)), sg.InputText(key='BUS_LENGTH')],
            [sg.Text('Car Length', size=(15,1)), sg.InputText(key='CAR_LENGTH')],
            [sg.Text('Bus Capacity Range', size=(15,1)), sg.InputText(key='BUS_CAPACITY_RANGE')],
            [sg.Text('Car Capacity Range', size=(15,1)), sg.InputText(key='CAR_CAPACITY_RANGE')],
            [sg.Text('Red Light Time', size=(15,1)), sg.InputText(key='RED_TIME')],
            [sg.Text('Yellow Light Time', size=(15,1)), sg.InputText(key='YELLOW_TIME')],
            [sg.Text('Bus Priority Time', size=(15,1)), sg.InputText(key='BUS_PRIORITY')],
            [sg.Text('Probability of Bus Spawning', size=(15,1)), sg.InputText(key='BUS_PROB')],
            [sg.Submit()]
        ]

        window = sg.Window('Simulation Options', layout).finalize()

        for key,value in self.get_book_variable_module_name("CONSTANTS").items():
            if key in window.key_dict.keys():
                window[key].update(value)
        
        while True:
            event, values = window.read()
            if event == 'Submit':
                for key,value in values.items():
                    if key in ["BUS_CAPACITY_RANGE","CAR_CAPACITY_RANGE"]:
                        setattr(CONSTANTS,key,tuple([int(i) for i in value.strip("()").split(",")]) )
                    elif key in ["ACCELERATION","BRAKING","BUS_PROB"]:
                        setattr(CONSTANTS,key,float(value))
                    else:
                        setattr(CONSTANTS,key,int(value))
                print(self.get_book_variable_module_name("CONSTANTS"))
                    
                break

        window.close()
