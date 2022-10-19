
from transposition_cipher import transposition
from rsa_cipher import RSA
from affine_cipher import affine_cipher

def __main__():
    cryptosystem=input('''
    *********************************************************************************************
    _________________________Welcome_____________________

    Choose the number that indicate the cryptosystem you want to encrypt your message with:
    1. Affine Cipher
    2. Transposition Cipher
    3. RSA Cipher
    4. Exit
    ''')

    while True:
        if cryptosystem=='1':
            print('*****You are currently using AFFINE CRYPTOSYSTEM*****')
            print('Enter the keys used to encrypt or decrypt a message using Affine Cipher')
            a = int(input('Enter the first key: '))
            b = int(input('Enter the second key: '))
            privateKey = affine_cipher(a,b)
            c = input(''' choose the number:
            1. If you want to encrypt
            2. If you want to decrypt
            ''')

            try:
                if c == '1':
                    d = input(' Enter the message you want to encrypt: ')
                    print(">>>Encrypted message : " + privateKey.encrypt(d))

                elif c == '2':
                    d = input(' Enter the message you want to decrypt: ')    
                    print(">>>Decrypted message : " + privateKey.decrypt(d))
            except:
                    print(" An Exception occured at affine cipher encryption/ decryption.")

        elif cryptosystem == '2':
            print('*****You are currently using TRANSPOSITION CRYPTOSYSTEM *****')
            print('Enter the keys used to encrypt or decrypt a message using Transposition Cipher')
            length = int(input('Enter the first key: '))
            arrange = int(input('Enter the second key: '))
            privateKey = transposition(length,arrange)
            c = input(''' Choose the number :
            1. If you want to encrypt
            2. If you want to decrypt
            ''')

            try:
                if c == '1':
                    d = input(' Enter the message you want to encrypt: ')
                    print(">>>Encrypted message : " + privateKey.encrypt(d))
                elif c == '2':
                    d = input(' Enter the message you want to decrypt: ')    
                    print(">>>Decrypted message : " + privateKey.decrypt(d))
            except:
                print(" An Exception occured.")

        elif cryptosystem=='3':
            print('*****You are currently using RSA CRYPTOSYSTEM*****')
            publicKey = RSA()
            p = int(input('Enter the first prime number: '))
            q = int(input('Enter the second prime n1umber: '))
            c=input(''' choose the number:
            1. If you want to encrypt
            2. If you want to decrypt
            ''')

            try:
                if c == '1':
                    d = input(' Enter the message you want to encrypt: ')
                    publicKey.generatekeys(p, q)
                    print(">>>Decrypted message : " + publicKey.encrypt(d))
                elif c == '2':
                    d = input(' Enter the message you want to decrypt ( separate by comma ): ') 
                    publicKey.generatekeys(p, q)   
                    print(">>>Decrypted message : " + publicKey.decrypt(d.split(',')))
            except:
                print(" An Exception occured at rsa encryption/ decryption.")

        elif cryptosystem == '4':
            print(" \n\n\t\t Thanks for using our program.")
            print(''' *********************************************************************************************            
            ''')
            break
        else:
            print(' Please enter valid input.')   
        cryptosystem = input('''choose the number that indicate the cryptosystem you want to encrypt your message with:
        1.Affine Cipher
        2.Transposition Cipher
        3.RSA Cipher
        4.if you are done with the program
        ''')

__main__()      
