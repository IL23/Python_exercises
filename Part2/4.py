# 4.     Izprintēt konsolē burtu ‘P’.

draw = ""

for row in range(1, 8):
    draw = ""
    for col in range(1, 5):
        if col == 1 or row == 1 or row == 4 or (col == 4 and (row == 2 or row == 3)):
            draw += "*"
        else:
            draw += " "
    print(draw)

