def print_move(fr, to):
    print(f'move from {fr} to {to}')

def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

fr = 'a'
to = 'b'
spare = 'c'

towers(5, fr, to, spare)
