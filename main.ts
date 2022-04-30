input.onButtonPressed(Button.A, function () {
    ping_lv += 500
    while (true) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(ping_lv)
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(ping_lv)
    }
})
input.onButtonPressed(Button.B, function () {
    ping_lv += -100
    ping_lv = Math.max(100, ping_lv)
    while (true) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(ping_lv)
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(ping_lv)
    }
})
let ping_lv = 0
ping_lv = 1000
basic.forever(function () {
	
})
