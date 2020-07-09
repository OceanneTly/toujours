for index in range(4):
    basic.show_string("Hello!")
    basic.pause(200)
    basic.show_number(10853)
    basic.pause(200)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.pause(200)
    basic.show_icon(IconNames.HAPPY)

def on_forever():
    pass
basic.forever(on_forever)
