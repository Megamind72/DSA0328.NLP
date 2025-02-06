class PluralizerFSM:
    def __init__(self):
        self.irregular_nouns = {
            "man": "men", "woman": "women", "child": "children",
            "tooth": "teeth", "foot": "feet", "mouse": "mice"
        }

    def get_plural(self, noun):
        """Finite-State Machine for pluralizing English nouns"""
        if noun in self.irregular_nouns:
            return self.irregular_nouns[noun]
        
        if noun.endswith(("s", "x", "z", "ch", "sh")):
            return noun + "es"
        
        if noun.endswith("y") and noun[-2] not in "aeiou":
            return noun[:-1] + "ies"

        return noun + "s"

fsm = PluralizerFSM()
test_nouns = ["cat", "dog", "box", "church", "baby", "boy", "man", "child", "foot", "tooth", "mouse"]

print("Singular → Plural")
for noun in test_nouns:
    print(f"{noun} → {fsm.get_plural(noun)}")
