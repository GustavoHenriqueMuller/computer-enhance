
REGISTERS_W0 = {
    '000': 'al',
    '001': 'cl',
    '010': 'dl',
    '011': 'bl',
    '100': 'ah',
    '101': 'ch',
    '110': 'dh',
    '111': 'bh',
}

REGISTERS_W1 = {
    '000': 'ax',
    '001': 'cx',
    '010': 'dx',
    '011': 'bx',
    '100': 'sp',
    '101': 'bp',
    '110': 'si',
    '111': 'di',
}

INSTRUCTIONS_NAMES_OPCODES = {
    'MOV_VARIATION_1': '100010',
    'MOV_VARIATION_2': '1100011',
    'MOV_VARIATION_3': '1011',
    'MOV_VARIATION_4': '1010000',
    'MOV_VARIATION_5': '1010001',
}

REGISTER_MEMORY_BASE_EQUATIONS = {
    '000': 'bx + si',
    '001': 'bx + di',
    '010': 'bp + si',
    '011': 'bp + di',
    '100': 'si',
    '101': 'di',
    '110': 'bp',
    '111': 'bx'
}

def get_length_by_mod_and_rm_fields(mod, rm):
    if mod == '00':
        if rm == '110':
            return 4
        else:
            return 2
    elif mod == '01':
        return 3
    elif mod == '10':
        return 4
    elif mod == '11':
        return 2

def get_register_name(register_index, w_bit):
    if w_bit == '0':
        return REGISTERS_W0[register_index]
    elif w_bit == '1':
        return REGISTERS_W1[register_index]

def get_next_instruction_length(program_slice):
    if program_slice.startswith(INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_1']):
        mod = program_slice[8:10]
        rm = program_slice[13:16]

        return get_length_by_mod_and_rm_fields(mod, rm)

    elif program_slice.startswith(INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_2']):
        mod = program_slice[8:10]
        rm = program_slice[13:16]
        w_bit = program_slice[7]

        length_without_data_field = get_length_by_mod_and_rm_fields(mod, rm)

        if w_bit == '1':
            return length_without_data_field + 2
        elif w_bit == '0':
            return length_without_data_field + 1

    elif program_slice.startswith(INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_3']):
        w_bit = program_slice[4]

        if w_bit == '1':
            return 3
        elif w_bit == '0':
            return 2

    elif program_slice.startswith(INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_4']):
        return 3

    elif program_slice.startswith(INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_5']):
        return 3

def get_next_instruction(program, byte_index):
    program_slice = program[(byte_index * 8):]

    for instruction_name in INSTRUCTIONS_NAMES_OPCODES:
        opcode = INSTRUCTIONS_NAMES_OPCODES[instruction_name]

        if program_slice.startswith(opcode):
            instruction_length = get_next_instruction_length(program_slice)
            instruction = program_slice[0:instruction_length * 8]

            return instruction