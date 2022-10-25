

class RSA:

    #Check if Input's are Prime
   
    def generatekeys(self, p, q):

        # Checks the primality of the number entered

        def isprime ( num):
            if(num == 2): return True
            elif((num < 2) or ((num % 2) == 0)): return False
            elif(num > 2):
                for i in range(2 , num):
                    if not(num % i): return False
            return True

        # Euclidean algorithm to find the gcs of two numbers
        def egcd(e,r):
            while(r!=0):
                e,r = r, e%r
            return e
        
        def eugcd(e,r):
            for i in range(1,r):
                while(e!=0):
                    a,b = r//e, r%e
                    r=e
                    e=b

        # this code tries to find the inverse modulo
        def find_mod_inv(a,m):

            for inv in range(1,m):
                if((a % m) * (inv % m) % m == 1 ):
                    return inv

            raise Exception('An Exception occured while trying to decrypt. Error description :\
                The modular inverse does not exist.')

        check_p = isprime(p)
        check_q = isprime(q)

        assert check_p ,"generatekeys function must be given prime numbers. Non prime found."
        assert check_q ,"generatekeys function must be given prime numbers. Non prime found."
        
        # n is the rsa modulus n
        n = p * q
        
        # This r is called Eulers Toitent
        r = (p-1) * (q-1)
       
        # FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.
        for i in range(1,1000):
            if (egcd(i ,r ) == 1):
                publickey = i

        #CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.
        eugcd(publickey, r)


        privatekey = find_mod_inv(publickey, r)

        public = (publickey, n)
        private = (privatekey, n)

        self.private = private
        self.public = public


    # encryption_function that takes the public key to encrypt the message and the message to be encrypted

    def encrypt(self, msg):
        publickey, n = self.public
        enc_msg=""
        m=0

        #  iterate through each character in the <msg> string to encrypt their ordinance, append this number to the 
        # <enc_msg> and return the encrypted nessage

        for i in msg:
            if(i.isupper() or i.islower()):
                m = ord(i)-65
                c = (m ** publickey) % n           # The encryption formula for rsa cipher using the publickey
                enc_msg.append(c)

            
            elif (i.isspace()):
                space = 400
                enc_msg.append(space)

            else:               
                m = ord(i)-97
                c = (m ** publickey) % n
                enc_msg.append(c)

        return enc_msg


    # decryption function that takes the private key with which we decrypt the ciphered message and the message to be decrypted
    def decrypt(self, msg):
        privatekey ,n= self.private
        dec_msg=""
        m=0


        # iterating through each integer in the <msg> to decrypt each one
        # and concatenate the character formed to the <dec_msg> then return the 
        # decrypted string message
        for i in msg:
            if (i == 400): dec_msg += ' '
            else:
                m = (int(i) ** privatekey) % n            # the decryption formula using the private key
                m += 65
                character = chr(m)
                dec_msg += character

        return dec_msg
