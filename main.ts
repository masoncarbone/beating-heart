basic.forever(function on_forever() {
    basic.showIcon(IconNames.TShirt)
    // shows a tshirt and then pauses
    basic.pause(700)
    // shows my name
    basic.showString("Mason Carbone")
    // pauses after my name
    basic.pause(300)
    // shows my football number so there is a quick pause
    basic.showNumber(42)
    basic.clearScreen()
})
