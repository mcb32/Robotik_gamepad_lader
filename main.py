# let random_number=0
# 
# random_number=randint(1, 6)   // generate Random Numer between 1 ..6
radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_NONE)
basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """,
    1000)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
# Vibration Motor on
pins.digital_write_pin(DigitalPin.P12, 1)
# Make Sound that Gamepad is ready
music.play_tone(220, music.beat(BeatFraction.SIXTEENTH))
# Viration Motor OFF
pins.digital_write_pin(DigitalPin.P12, 0)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P15) == 0:
        led.plot(3, 2)
        led.unplot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 4)
        radio.send_string("Open")
    elif pins.digital_read_pin(DigitalPin.P13) == 0:
        radio.send_string("Close")
        led.plot(3, 4)
        led.unplot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 2)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        radio.send_string("LEDL")
        led.plot(2, 3)
        led.unplot(4, 3)
        led.unplot(3, 2)
        led.unplot(3, 4)
    elif pins.digital_read_pin(DigitalPin.P14) == 0:
        radio.send_string("LEDR")
        led.plot(4, 3)
        led.unplot(2, 3)
        led.unplot(3, 2)
        led.unplot(3, 4)
    else:
        if pins.analog_read_pin(AnalogPin.P2) > 550 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
            radio.send_value("F", pins.analog_read_pin(AnalogPin.P2))
        elif pins.analog_read_pin(AnalogPin.P2) < 450 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
            radio.send_value("B", pins.analog_read_pin(AnalogPin.P2))
        elif pins.analog_read_pin(AnalogPin.P1) < 450 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
            radio.send_value("L", pins.analog_read_pin(AnalogPin.P1))
        elif pins.analog_read_pin(AnalogPin.P1) > 550 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
            radio.send_value("R", pins.analog_read_pin(AnalogPin.P1))
        else:
            radio.send_string("S")
basic.forever(on_forever)
