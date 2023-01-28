class enigma:
    def __init__(self,rotors,reflector):
        # default values
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.table = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
                        'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,
                        'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
                        'V':21,'W':22,'X':23,'Y':24,'Z':25}
        self.rotors_set = {'I':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                    'II':"AJDKSIRUXBLHWTMCQGZNPYFVOE",
                    'III':"BDFHJLCPRTXVZNYEIWGAKMUSQO"}
        self.reflector_set = {'A':"EJMZALYXVBWFCRQUONTSPIKHGD",'B':"YRUHQSLDPXNGOKMIEBFZCWVJAT",'C':"FVPJIAOYEDRZXWGCTKUQSBNMHL"}
        
        # accept input
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = []

        # check if input valid
        self.machine_valid()

        # create circuit
        self.circuit = self.circuit()

    def circuit(self):
        # initial settings
        circuit = [self.alpha_to_num(list(self.letters))]
        
        # plugboard

        # rotors
        for rotor in self.rotors:
            lst = self.alpha_to_num(list(self.rotors_set[rotor]))
            circuit.append(lst)
        # reflector
        
        circuit.append(self.alpha_to_num(list(self.reflector_set[self.reflector])))
        
        return circuit

    def alpha_to_num(self,lst):
        new_lst = []
        for _ in lst:
            new_lst.append(self.table[_])
        return new_lst

    def num_to_alpha(self,num):
        return list(self.table.keys())[list(self.table.values()).index(num)]

    def machine_valid(self):
        assert len(self.rotors) == 3, "3 rotors required"
        for _ in self.rotors:
            assert self.rotors_set[_], "not valid rotor inserted"
        assert self.reflector_set[self.reflector], "not valid reflector selected"
    
    def message_valid(self,msg):
        for _ in msg:
            assert _.upper() in self.letters , "only alphabets allowed"

    def rotate(self):
        # do something
        c = self.circuit
        
        # if notch

        # rotote the first rotor
        lst = [_ - 1 if _>0 else 25 for _ in c[1]]
        c[1] = lst[1:] + [lst[0]]
        #self.circuit[2]

    def encode(self,letter):
        # rotate once
        self.rotate()
        c = self.circuit
        # get the index
        idx = self.table[letter.upper()]
        # run through the circuit
        
        _0 = c[0][idx] # when pressed
        #print(letter, self.num_to_alpha(_0))
        _1 = c[1][_0] # 1st rotor
        #print(self.num_to_alpha(_1))
        _2 = c[2][_1]
        #print(self.num_to_alpha(_2))
        _3 = c[3][_2]
        #print(self.num_to_alpha(_3))
        _4 = c[4][_3]
        _3 = c[3].index(_4)
        _2 = c[2].index(_3)
        _1 = c[1].index(_2)
        _0 = c[0].index(_1)

        return self.num_to_alpha(_0)
    def run(self,msg):
        # validate msg
        self.message_valid(msg)
        encoded = ''
        # assume no notch first, and the first wheel will step when key pressed
        for _ in msg:
            encoded += self.encode(_)

        print(msg,"is encoded into",encoded)
        # load the 

if __name__ == '__main__':
    engine = enigma(['III','II','I'],'A')
    #engine.rotate()
    #print(engine.circuit)
    
    engine.run('NFOWMLQ') # ans: l
