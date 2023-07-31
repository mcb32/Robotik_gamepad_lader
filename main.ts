// let random_number=0
// 
// random_number=randint(1, 6)   // generate Random Numer between 1 ..6
radio.setGroup(1)
pins.setPull(DigitalPin.P13, PinPullMode.PullNone)
pins.setPull(DigitalPin.P15, PinPullMode.PullNone)
pins.setPull(DigitalPin.P14, PinPullMode.PullNone)
pins.setPull(DigitalPin.P16, PinPullMode.PullNone)
basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    `,1000)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
// Vibration Motor on
pins.digitalWritePin(DigitalPin.P12, 1)
// Make Sound that Gamepad is ready
music.playTone(220, music.beat(BeatFraction.Sixteenth))
// Viration Motor OFF
pins.digitalWritePin(DigitalPin.P12, 0)

basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P15) == 0) {
        led.plot(3, 2)
        led.unplot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 4)
        radio.sendString("Open")
    } else if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        radio.sendString("Close")
        led.plot(3, 4)
        led.unplot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 2)
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        radio.sendString("LEDL")
        led.plot(2, 3)
        led.unplot(4, 3)
        led.unplot(3, 2)
        led.unplot(3, 4)
    } else if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        radio.sendString("LEDR")
        led.plot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 2)
        led.unplot(3, 4)
    } else {
        if (pins.analogReadPin(AnalogPin.P2) > 550 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
            radio.sendValue("F", pins.analogReadPin(AnalogPin.P2))
        } else if (pins.analogReadPin(AnalogPin.P2) < 450 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
            radio.sendValue("B", pins.analogReadPin(AnalogPin.P2))
        } else if (pins.analogReadPin(AnalogPin.P1) < 450 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
            radio.sendValue("L", pins.analogReadPin(AnalogPin.P1))
        } else if (pins.analogReadPin(AnalogPin.P1) > 550 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
            radio.sendValue("R", pins.analogReadPin(AnalogPin.P1))
        } else {
            radio.sendString("S")
        }
    }
})
