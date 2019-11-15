#Simple GUI from our Cube Game 
import PySimpleGUI as sg
 
sg.change_look_and_feel('GreenTan')
 
layout = [
    [sg.Text('The Cube Game', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, background_color='#C93515')],
    [sg.Text('Welcome to the Cube Game.\nPlease select a difficulty',
            background_color='#C93515')],
    [sg.Frame(layout=[
        [sg.Radio('Easy', "RADIO1", default=True, background_color='#808080'),
         sg.Radio('Normal', "RADIO1", background_color='#808080'),
         sg.Radio('Hard', "RADIO1", background_color='#808080')]], title='Difficulty',
             title_color='black',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set difficulty',
             background_color='#C93515')],
    [sg.Submit(button_text='Start', tooltip='Press to start the game'), sg.Cancel()]]
 
window = sg.Window('The Cube Game', layout,
    default_element_size=(40, 1), grab_anywhere=False, background_color='#C93515')
 
event, values = window.read()