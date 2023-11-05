function fonction(num: number): number {
    return num * 5 + 3
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    x = x - 1
    basic.showNumber(x)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    basic.showNumber(fonction(x))
    x = 0
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    x = x + 1
    basic.showNumber(x)
})
let x = 0
x = 0
basic.showNumber(x)
