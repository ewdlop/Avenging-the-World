# Avenging-the-World

Hey Russkies, you should save your country first.

You may call me 支那.

In Матушка Россия, bears eat you. (not proper Russian of course. People put Russian in English to understand Russian)

Ukrainians are stronger and more powerful than you American Russkies.(指桑罵槐)

# B#(BSharp) - BrainFuck Interpreter written Python

Brainfuck is a minimalistic programming language that typically works with 8-bit values, which means it doesn't natively support Unicode. However, you can modify the interpreter to handle Unicode characters by using a larger data type for the memory cells and handling input/output appropriately. Below is an example of a Brainfuck interpreter in Python that supports Unicode:

```python
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
```

### Explanation:
1. **Initialization**:
   - The `BrainfuckInterpreter` class is initialized with the Brainfuck code and optional input data.
   - The memory is initialized to a list of 30,000 zeros, which is typical for Brainfuck.
   - Pointers for the code (`code_pointer`), memory (`pointer`), and input (`input_pointer`) are also initialized.

2. **Running the Code**:
   - The `run` method processes each command in the Brainfuck code.
   - Commands like `>`, `<`, `+`, `-`, `.` and `,` are handled as per Brainfuck specifications.
   - The `+` and `-` commands are modified to handle the full Unicode range (`0x110000`).
   - The `[` and `]` commands handle loops, jumping to the matching bracket if the current memory cell is zero or non-zero, respectively.

3. **Input and Output**:
   - The `,` command reads from the input data if available and sets the memory cell to the Unicode code point of the character.
   - The `.` command outputs the character corresponding to the current memory cell's value.

This interpreter allows you to run Brainfuck programs that can handle Unicode input and output, expanding the language's capabilities to a wider range of characters.
