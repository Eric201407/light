def on_button_pressed_a():
    global ping_lv
    ping_lv += 10000
    while True:
        pins.digital_write_pin(DigitalPin.P0, 0)
        control.wait_micros(ping_lv)
        pins.digital_write_pin(DigitalPin.P0, 1)
        control.wait_micros(ping_lv)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global ping_lv
    ping_lv += -10000
    ping_lv = max(10000, ping_lv)
    while True:
        pins.digital_write_pin(DigitalPin.P0, 0)
        control.wait_micros(ping_lv)
        pins.digital_write_pin(DigitalPin.P0, 1)
        control.wait_micros(ping_lv)
input.on_button_pressed(Button.B, on_button_pressed_b)

ping_lv = 0
ping_lv = 500000

def on_forever():
    pass
basic.forever(on_forever)
