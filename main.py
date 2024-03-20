import PySimpleGUI as sg
from convert import units, convert_units

output_value = 0 #output on 2nd input element

main_units = list(units.keys())
current_main_unit = main_units[0]
current_unit_values = list(units[current_main_unit])

#styles
sg.theme("DarkBlue")
sg.set_options(font=("Courier New", 15))

#create layout, giving each element a unique key
layout = [
    [sg.Text("CONVERTER APP", justification='center', expand_x=True)],
    [sg.Push(), sg.Spin(main_units, key="main-units",enable_events=True, size=(15,1)), sg.Push()], #main units element
                                    
    [sg.Input(0, key="input", enable_events=True),sg.Spin(current_unit_values, key="select-unit-1"),#3rd row(Divided in 2 to avoid overflow), first input and select unit element
    sg.Text("="),sg.Input(output_value, key="output", enable_events=True),sg.Spin(current_unit_values, key="select-unit-2")], #second input and select unit element

    [sg.Button("Convert", key="convert-button")] #button element, convert first unit to value of second element
]

window = sg.Window("Converter App", layout) #initialize window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'input' or event == 'convert-button': #output converts values based on input
        try:
            input_value = float(values['input'])
            output_value = convert_units(units[values['main-units']], values['input'], values['select-unit-1'], values['select-unit-2'])
            window['output'].update(output_value)

        #So app doesnt crash on value errors
        except ValueError:
            window['output'].update(0)
            print("Value Error")

    
    elif event == 'main-units':
        current_main_unit = values[event]
        current_unit_values = list(units[current_main_unit].keys())
        window['input'].update(0)
        window['output'].update(0)

        window['select-unit-1'].update(current_unit_values[0], values=current_unit_values)
        window['select-unit-2'].update(current_unit_values[0], values=current_unit_values)

window.close()