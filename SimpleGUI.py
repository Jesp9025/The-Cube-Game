#Simple GUI from our Cube Game
#Edit of 'demo2' from Kaj
import PySimpleGUI as sg
 
def hello():
    print("Hello")

sg.change_look_and_feel('Reddit')
 
layout = [
    [sg.Text('The Cube Game', size=(
        20, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Welcome to this mini-story text adventure game')],
    [sg.Text('Please enter your name')],
    [sg.InputText(key="_NAME_")],
    [sg.Text('Please select a difficulty')],
    [sg.Frame(layout=[
        [sg.Radio('Easy', "RADIO1", default=True, key="_EASY_"),
         sg.Radio('Normal', "RADIO1", key="_NORMAL_"),
         sg.Radio('Hard', "RADIO1", key="_HARD_")]],
            title='Difficulty',
            title_color='black',
            relief=sg.RELIEF_SUNKEN,)],
    [sg.Button(button_text="Start"), sg.Button(button_text="Quit")]]
    

window = sg.Window('The Cube Game', layout,
    default_element_size=(40, 1), grab_anywhere=False)


event, values = window.read()
if event == "Start":
    hello()
elif event == "Quit":
    print("Im out")
username = values["_NAME_"]
print(username)
if values["_EASY_"]:
    print("EASY SELECTED")
elif values["_NORMAL_"]:
    print("NORMAL SELECTED")
elif values["_HARD_"]:
    print("HARD SELECTED")
