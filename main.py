def fonction(num: number):
    return num * 5 + 3

def on_button_pressed_a():
    global x
    x = x - 1
    basic.show_number(x)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global x
    basic.show_number(fonction(x))
    x = 0
    basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global x
    x = x + 1
    basic.show_number(x)
input.on_button_pressed(Button.B, on_button_pressed_b)

x = 0
x = 0
basic.show_number(x)