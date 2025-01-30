class FSA:
    def __init__(self):
        self.state = 0  # Initial state

    def transition(self, char):
        if self.state == 0:
            self.state = 1 if char == 'a' else 0
        elif self.state == 1:
            self.state = 2 if char == 'b' else (1 if char == 'a' else 0)
        elif self.state == 2:
            self.state = 1 if char == 'a' else 0

    def is_accepted(self, string):
        self.state = 0  # Reset state for each string
        for char in string:
            self.transition(char)
        return self.state == 2  # Accept if final state is 2


# Test the FSA
fsa = FSA()
test_strings = ["cab", "aab", "bca", "abcab", "abab", "xyz"]

for s in test_strings:
    print(f"String '{s}' accepted? {fsa.is_accepted(s)}")
