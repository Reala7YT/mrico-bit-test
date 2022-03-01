input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("test")
    basic.showString("sent")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    led.plot(1, 1)
    led.plot(2, 2)
})
radio.setGroup(1)
