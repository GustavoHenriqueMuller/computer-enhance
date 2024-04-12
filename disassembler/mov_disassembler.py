import utils

def get_disassembly_mov_variation_1(instruction):
    first_byte = instruction[0:8]
    second_byte = instruction[8:16]

    d_bit = first_byte[6]
    w_bit = first_byte[7]
    mod = second_byte[0:2]
    reg = second_byte[2:5]
    rm = second_byte[5:8]

    if mod == '00':
        register_name = utils.get_register_name(reg, w_bit)
        memory_expression = None

        if rm == '110':
            displacement = instruction[24:32] + instruction[16:24]
            memory_expression = str(int(displacement, 2))
        else:
            memory_expression = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]

        if d_bit == '1':
            return 'mov {}, [{}]'.format(register_name, memory_expression)
        elif d_bit == '0':
            return 'mov [{}], {}'.format(memory_expression, register_name)

    if mod == '01':
        register_name = utils.get_register_name(reg, w_bit)
        displacement = instruction[16:24]
        memory_expression = None

        memory_access_equation = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]
        memory_expression = memory_access_equation + ' + ' + str(int(displacement, 2))

        if d_bit == '1':
            return 'mov {}, [{}]'.format(register_name, memory_expression)
        elif d_bit == '0':
            return 'mov [{}], {}'.format(memory_expression, register_name)

    if mod == '10':
        register_name = utils.get_register_name(reg, w_bit)
        displacement = instruction[24:32] + instruction[16:24]
        memory_expression = None

        memory_access_equation = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]
        memory_expression = memory_access_equation + ' + ' + str(int(displacement, 2))

        if d_bit == '1':
            return 'mov {}, [{}]'.format(register_name, memory_expression)
        elif d_bit == '0':
            return 'mov [{}], {}'.format(memory_expression, register_name)

    elif mod == '11':
        first_register_name = utils.get_register_name(reg, w_bit)
        second_register_name = utils.get_register_name(rm, w_bit)

        if d_bit == '1':
            return 'mov {}, {}'.format(first_register_name, second_register_name)
        elif d_bit == '0':
            return 'mov {}, {}'.format(second_register_name, first_register_name)

def get_disassembly_mov_variation_2(instruction):
    w_bit = instruction[7]
    mod = instruction[8:10]
    rm = instruction[13:16]

    immediate = None

    if w_bit == '1':
        immediate_low = instruction[-16:-8]
        immediate_high = instruction[-8:]

        immediate = str(int(immediate_high + immediate_low, 2))
    elif w_bit == '0':
        immediate = str(int(instruction[-8:], 2))

    if mod == '00':
        memory_expression = None

        if rm == '110':
            displacement = instruction[24:32] + instruction[16:24]
            memory_expression = str(int(displacement, 2))
        else:
            memory_expression = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]

        if w_bit == '1':
            return 'mov [{}], word {}'.format(memory_expression, immediate)
        elif w_bit == '0':
            return 'mov [{}], byte {}'.format(memory_expression, immediate)

    elif mod == '01':
        displacement = instruction[16:24]

        memory_access_equation = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]
        memory_expression = memory_access_equation + ' + ' + str(int(displacement, 2))

        if w_bit == '1':
            return 'mov [{}], word {}'.format(memory_expression, immediate)
        elif w_bit == '0':
            return 'mov [{}], byte {}'.format(memory_expression, immediate)

    elif mod == '10':
        displacement = instruction[24:32] + instruction[16:24]

        memory_access_equation = utils.REGISTER_MEMORY_BASE_EQUATIONS[rm]
        memory_expression = memory_access_equation + ' + ' + str(int(displacement, 2))

        if w_bit == '1':
            return 'mov [{}], word {}'.format(memory_expression, immediate)
        elif w_bit == '0':
            return 'mov [{}], byte {}'.format(memory_expression, immediate)

    elif mod == '11':
        raise Exception('Não sei o que significa mod 11 na instrução de immediate to memory...')

def get_disassembly_mov_variation_3(instruction):
    w_bit = instruction[4]
    reg = instruction[5:8]

    register_name = utils.get_register_name(reg, w_bit)
    immediate = None

    if w_bit == '1':
        immediate = instruction[16:24] + instruction[8:16]
    elif w_bit == '0':
        immediate = instruction[8:16]

    return 'mov {}, {}'.format(register_name, str(int(immediate, 2)))

def get_disassembly_mov_variation_4(instruction):
    w_bit = instruction[7]
    address = instruction[16:24] + instruction[8:16]
    accumulator_register_name = utils.get_register_name('000', w_bit)

    return 'mov {}, [{}]'.format(accumulator_register_name, str(int(address, 2)))

def get_disassembly_mov_variation_5(instruction):
    w_bit = instruction[7]
    address = instruction[16:24] + instruction[8:16]
    accumulator_register_name = utils.get_register_name('000', w_bit)

    return 'mov [{}], {}'.format(str(int(address, 2)), accumulator_register_name)