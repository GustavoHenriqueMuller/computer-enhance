import utils
import mov_disassembler

def get_disassembly(program):
    disassembly = ''
    disassembly += 'bits 16\n\n'

    byte_index = 0
    instruction_count = 1
    program_byte_amount = int(len(program) / 8)

    print()

    while byte_index < program_byte_amount:
        instruction = utils.get_next_instruction(program, byte_index)
        instruction_length = int(len(instruction) / 8)

        print('Instruction [{}]: {}'.format(instruction_count, instruction))

        if instruction.startswith(utils.INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_1']):
            disassembly += mov_disassembler.get_disassembly_mov_variation_1(instruction) + '\n'

        if instruction.startswith(utils.INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_2']):
            disassembly += mov_disassembler.get_disassembly_mov_variation_2(instruction) + '\n'

        if instruction.startswith(utils.INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_3']):
            disassembly += mov_disassembler.get_disassembly_mov_variation_3(instruction) + '\n'

        if instruction.startswith(utils.INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_4']):
            disassembly += mov_disassembler.get_disassembly_mov_variation_4(instruction) + '\n'

        if instruction.startswith(utils.INSTRUCTIONS_NAMES_OPCODES['MOV_VARIATION_5']):
            disassembly += mov_disassembler.get_disassembly_mov_variation_5(instruction) + '\n'

        byte_index += instruction_length
        instruction_count += 1

    return disassembly