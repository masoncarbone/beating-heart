def on_forever():
    basic.show_icon(IconNames.PITCHFORK)
    #shows a tshirt and then pauses
    basic.pause(700)
    #shows my name
    basic.show_string("Mason Carbone")
    #pauses after my name
    basic.pause(300)
    #shows my football number so there is a quick pause
    basic.show_number(42)
    basic.pause(1000)
    #has another pause so that the person wathcing does not look at the same thing quickly again
    basic.clear_screen(300)
basic.forever(on_forever)
