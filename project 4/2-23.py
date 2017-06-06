import tkinter

def hello_button_pressed()->None:
    print('hotdog')

def mouse_entered_button(event:tkinter.Event)->None:
    event.widget['text'] = 'I am'

def mouse_exited_button(event:tkinter.Event)->None:
    event.widget['text'] = 'anime'

def show_gui() -> None:
    root_window = tkinter.Tk()

    button = tkinter.Button(
        master = root_window, text = 'o sht wadup', font = ('Helvetica', 50),
        command = hello_button_pressed) #<- behavior
    button.pack()

    #event binding
    button.bind('<Enter>', mouse_entered_button)
    button.bind('<Leave>', mouse_exited_button)
    
    
    root_window.mainloop()

if __name__ == '__main__':
    show_gui()
