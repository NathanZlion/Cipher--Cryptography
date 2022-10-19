# ////////////////////////////////////////////////////////////////////////////////////



class affine_cipher:
    def __init__(self, a, b):
        self.key  = self.list_generator()

        if type(a) == int and type(b) == int:
            pass
        else:
            raise Exception('An Exception occured while trying to decrypt. description :The modular inverse does not exist.')


        # a and the length of the self.key should be coprimes for an affine cipher to 
        #  work properly as intended

        assert self.gcd(a, 95) == 1, "Invalid input,  %d is not coprime with 95 !" %a

        self.a = a
        self.b = b

    #  generates the key which has all available alphabets, symbols and numbers, 
    #  The generated list is of length 95 

    def list_generator(self):
        list = []
        firstSymbol= ord(" ")
        lastSymbol = ord("~")
        for symbol in range(firstSymbol,lastSymbol + 1):
            value=chr(symbol)
            list.append(value)
        return list


    def encrypt(self, msg):
        encrypted_text = ""

        for char in msg:
            if char in self.key:
                position = self.key.index(char)
                encrypted_text += self.key[(self.a * position + self.b) % 95]
            else:
                encrypted_text += char

        return encrypted_text

    # The inputs for this decryption is the same as the ones used to encrypt it

    def decrypt(self, msg):
        decrypted_text = ""

        for char in msg:
            if char in self.key:
                position = self.key.index(char)

                #  below is a formula that uses the inverse modulo to solve for the original message index
                #  from the index of the current message index
                decrypted_char_index = (self.find_mod_inv(self.a, 95) * (position - self.b)) % 95
                decrypted_text += self.key[decrypted_char_index]

            else:
                decrypted_text += char

        return decrypted_text

    # This function returns the inverse modulus of a(mod m) if no inverse is available it handles the exception by raising an exception

    def find_mod_inv(self, a,m):
        for i in range(1,m):
            if((a%m)*(i%m) % m==1):
                return i

        raise Exception('An Exception occured while trying to decrypt. description :The modular inverse does not exist.')

    #  finds the greatest common divisor of two numbers by implementing the euclidean algorithm to find gcd of the numbers efficiently (faster)
    #  euclidean algorithm   >> gcd(a, b) = gcd (b, a mod b)
    def gcd(self, num1, num2):
        if num1 >= num2:
            while num2 !=0:
                remainder = num1 % num2
                num1 = num2
                num2 = remainder
            
            return num1
        else:
            while num1 != 0:
                remainder = num2 % num1
                num2 = num1
                num1 = remainder
            
        return num2       

# ////////////////////////////////////////////////////////////////////////////////////
