STAR, SPACE, CRLF = '*', ' ', '\n'

START, REPEAT, END = STAR, SPACE + STAR, ''

WIDTH = 60

def line(line_num: int) -> str:
    return start_line(line_num) + repeat_middle(line_num) + end_line(line_num)

def start_line(line_num: int)-> str:
    return START

def repeat_middle(line_num: int)-> str:
    return line_num * REPEAT

def end_line(line_num: int)-> str:
    return END

def pyramid_b1(size: int) -> [str]:
    pyramid = []
    for line_num in range(size):
        pyramid.append(line(line_num))
    return pyramid

def format_pyramid(ps: [str]) -> str:
    pyramid = []
    pyramid2 = []
    for p in ps:
        pyramid.append(p.center(WIDTH))
    for p in ps[::-1]:
        pyramid.append(p.center(WIDTH))
    pyramid3 = pyramid + pyramid2
    return CRLF.join(pyramid3)

print(format_pyramid(pyramid_b1(7)))