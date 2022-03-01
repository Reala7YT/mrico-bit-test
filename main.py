def on_button_pressed_a():
    radio.send_string("test")
    basic.show_string("sent")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    led.plot(1, 1)
    led.plot(2, 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)