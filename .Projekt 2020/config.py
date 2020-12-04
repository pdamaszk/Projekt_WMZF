# testowanie zawartosci okna
def test_interfecu():
    global test_id
    test_id = 1

# configuracja testowania framów interfacu
test_colours = {'title': (None, 'yellow'),
                'left_frame': (None, 'green'),
                'right_frame': (None, 'orange'),
                'canvas': (None, 'blue'),
                'botton': (None, 'blue'),
                'adds': (None, 'pink')}

test_id = 0
test = False
keypressed = False

window_ico = 'ico2_32_32.ico'
window_title = " Wahadło podwójne - v1.0 Beta"

main_font = "Times 12 "
sub_font = "Times 10 italic"
title_font = "Times 20 bold italic"

window_width_change = True
window_height_change = True

padx_label = 8
align_entry = 'right'

color_list = (None, 'white', 'red')
bg_canvas = color_list[1]
bg_button = color_list[0]
window_width = 600
window_height = 550
canvas_width = 300
canvas_height = 300

if test:
    test_interfecu()
