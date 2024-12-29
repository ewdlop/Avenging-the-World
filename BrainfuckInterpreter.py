class BrainfuckInterpreter:
    def __init__(self, code, input_data=""):
        self.code = code
        self.input_data = input_data
        self.memory = [0] * 30000
        self.pointer = 0
        self.code_pointer = 0
        self.input_pointer = 0
        self.output = []

    def run(self):
        while self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]

            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 0x110000  # Unicode range
            elif command == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 0x110000  # Unicode range
            elif command == '.':
                self.output.append(chr(self.memory[self.pointer]))
            elif command == ',':
                if self.input_pointer < len(self.input_data):
                    self.memory[self.pointer] = ord(self.input_data[self.input_pointer])
                    self.input_pointer += 1
                else:
                    self.memory[self.pointer] = 0  # If no input is available, set memory to 0
            elif command == '[':
                if self.memory[self.pointer] == 0:
                    open_brackets = 1
                    while open_brackets != 0:
                        self.code_pointer += 1
                        if self.code[self.code_pointer] == '[':
                            open_brackets += 1
                        elif self.code[self.code_pointer] == ']':
                            open_brackets -= 1
            elif command == ']':
                if self.memory[self.pointer] != 0:
                    close_brackets = 1
                    while close_brackets != 0:
                        self.code_pointer -= 1
                        if self.code[self.code_pointer] == '[':
                            close_brackets -= 1
                        elif self.code[self.code_pointer] == ']':
                            close_brackets += 1

            self.code_pointer += 1

        return ''.join(self.output)


# Example usage
code = "++++[>++++[>++++<-]<-]>>-----.>---.+++++++..+++."
interpreter = BrainfuckInterpreter(code)
output = interpreter.run()
print(output)
