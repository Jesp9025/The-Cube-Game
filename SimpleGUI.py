#Simple GUI from our Cube Game
#Edit of 'demo2' from Kaj
import PySimpleGUI as sg
 
sg.change_look_and_feel('Reddit')
 
layout = [
    [sg.Text('The Cube Game', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Welcome to this mini-story text adventure game')],
    [sg.Text('Please enter your name')],
    [sg.InputText()],
    [sg.Text('Please select a difficulty')],
    [sg.Frame(layout=[
        [sg.Radio('Easy', "RADIO1", default=True),
         sg.Radio('Normal', "RADIO1"),
         sg.Radio('Hard', "RADIO1")]], title='Difficulty',
             title_color='black',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set difficulty')],
    [sg.Submit(button_text='Start', tooltip='Press to start the game'), sg.Cancel()]]

window = sg.Window('The Cube Game', layout,
    default_element_size=(40, 1), grab_anywhere=False)
 
event, values = window.read()
