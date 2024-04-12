import file_utils
import disassembler

INPUT_FILE_NAME = 'listing_40'
INPUT_FILE_DIRECTORY = '../Homework 2/'
OUTPUT_FILE_NAME = INPUT_FILE_DIRECTORY + 'decompiled_' + INPUT_FILE_NAME + '.asm'

def main():
    print()

    program = file_utils.get_program(INPUT_FILE_DIRECTORY + INPUT_FILE_NAME)
    disassembly = disassembler.get_disassembly(program)
    file_utils.write_to_file(OUTPUT_FILE_NAME, disassembly)

    print("\nWrote disassembly to file '{}'.".format(OUTPUT_FILE_NAME))

if __name__ == '__main__':
    main()