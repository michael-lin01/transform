from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
n                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,"r")
    lines = f.readlines()
    for line_num in range(0,len(lines)):
        line = lines[line_num].strip()
        if line == "line" or line == "scale" or line == "move" or line == "rotate":
            line_num += 1
            args = lines[line_num].strip().split(' ')
            if line == "line":
                args = list(map(int,args))
                add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            elif line == "scale":
                args = list(map(int,args))
                scale = make_scale(args[0], args[1], args[2])
                matrix_mult(scale, transform)
            elif line == "move":
                args = list(map(int,args))
                translate = make_translate(args[0], args[1], args[2])
                matrix_mult(translate, transform)
            elif line == "rotate":
                if args[0] == "x":
                    rotate = make_rotX(int(args[1]))
                if args[0] == "y":
                    rotate = make_rotY(int(args[1]))
                if args[0] == "z":
                    rotate = make_rotZ(int(args[1]))
                matrix_mult(rotate, transform)
        elif line == "ident":
            ident(transform)
        elif line == "apply":
            matrix_mult(transform, points)
        elif line == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif line == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, lines[line_num+1].strip())
    f.close()

