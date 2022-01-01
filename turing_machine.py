# Variables
tape = [int(x) for x in list(input('Enter tape...\n'))]
# program_file = input('Enter program file...\n')
TM_program = {}

# Methods

def draw_horizontal_line():
    print('-'*(2*len(tape)+1))

def display_tape():
    draw_horizontal_line()
    print('|','|'.join(str(symbol) for symbol in tape),'|', sep='')
    draw_horizontal_line()

with open(input('Enter program file...\n')) as TM_program_file:
    for line in TM_program_file:
        if line.startswith('#'):
            current_state = line.split()[-1]
            continue
        elif line.isspace():
            continue
        state, symbol, new_state, new_symbol, direction = line.split()
        TM_program[state, int(symbol)] = new_state, int(new_symbol), direction

current_position = tape.index(1)
current_symbol = tape[current_position]

def display_current_configuration():
   display_tape()
   print('  ' * current_position, current_state)

display_current_configuration()
while (current_state, current_symbol) in TM_program:
    new_state, new_symbol, direction =\
                            TM_program[current_state, current_symbol]
    tape[current_position] = new_symbol
    current_state = new_state
    # Alternative notation for
    # current_position = current_position + 2 * (direction == 'R') - 1
    current_position += 2 * (direction == 'R') - 1
    current_symbol = tape[current_position]
    display_current_configuration()
display_current_configuration()