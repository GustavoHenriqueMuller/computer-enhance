
def decode_contents(content_bytes):
    int_equivalent = int.from_bytes(content_bytes)
    string_equivalent = '{0:b}'.format(int_equivalent)

    return string_equivalent

def get_program(file_name):
    with open(file_name, 'rb') as input_file:
        program_bytes = input_file.read()
        program = decode_contents(program_bytes)

        print("Read file '{}' ({} bytes long). Disassembling..."
              .format(file_name, int(len(program) / 8)))

        return program

def write_to_file(file_name, contents):
    with open(file_name, 'w') as output_file:
        output_file.write(contents)