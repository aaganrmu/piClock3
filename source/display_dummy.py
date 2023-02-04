from display import display

class display_dummy(display):
    def get_text(self):
        items = [
                 'fake stats:',
                 '10   potrzebie',
                 ' 1.1 bloit/shake',
                 ' 9   jiffy'
                 ]
        return(items)
