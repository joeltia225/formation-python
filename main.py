import os
import time

import functions
import FreeSimpleGUI as sg

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Entrer une information", key="todo")
add_button = sg.Button("Ajouter")
list_box = sg.Listbox(values=functions.get_todos(), key='todos' ,
                      enable_events=True, size=(45, 10))

edit_button = sg.Button("Modifier")
complete_buton = sg.Button("Supprimer")
exit_button = sg.Button("Sortir")

layout = []
layout =  [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_buton],
          [exit_button]]

window = sg.Window('My To-Do App',
                    enable_close_attempted_event=True,
                    layout= layout,
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    match event:
        case "Ajouter":
                new_todo = values['todo'].strip()
                if new_todo == "":
                    sg.popup("champ vide !")
                else:
                    todos = functions.get_todos()
                    new_todo = values['todo'] + "\n"
                    todos.append(new_todo)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update("")

        case "Modifier":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first")

        case "Supprimer":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please, select an item first")

        case "Sortir":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            continue

window.close()