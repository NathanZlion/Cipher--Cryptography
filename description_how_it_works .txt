<!-- Discrete Mathematics: Programing Assignment -->

    Topic : " Cryptography "

    We have used three classes to make implementations of three types of cryptographies, namely 'Affine Cipher', 'Transposition Cipher', and 'RSA Cipher".
Within each class we have added two methods encrypt and decrypt and some other methods we found useful.

A, Affine Cipher:

> How to run the program to encrypt and decrypt a message (string) using affine cipher :

    To run the program follow the following steps:

    1. Create an object of affine cipher class by passing the neccesary arguments to the constructor, these neccerary arguments are two integers <a> and <b> from the function 
    f(p)=(ap + b) mod 95, where gcd(a, 95) = 1. We can do this as follows :
        >>> privateKey = affine_cipher(1,5)
         where a=1 and  b=5

    2. To encrypt a message call the functon encrypt by passing the message as a string to function as an argument by using the object created in the first step.
       >>> privateKey.encrypt("hi friend")
        where <hi friend> is the message to be encrypted.

    3. To decrypt a message call the functon decrypt by passing the message as a string to function as an argument by using the object created in the first step.
        >>> privateKey.decrypt("hi friend")
         where <hi friend> is the message that has been encrypted before and that we want to decrypt now.

Note: All the above steps are included in the __main__() method, and the user can interact with the program by choosing the appropriate choices asked by the program. 

> Theorems and Concepts we used while implementing affine cipher:
    
    we have used the Euclidean Algorithm to calculate the greatest common divisor gcd(a,k) to check the validity of the encrypting number entered when initializing the class
     where k is the length of <key> list and <a> is the integer input entered.

    To encrypt a message first we find the index of each character which are in the message to be encrypted in the list we have designated it by <key> in the constructor of the 
    affine class and we find the functional value of this  indexes when they pass into the bijection function f(p)= (a(p)+b) mod k, this function became bijection when gcd(a,k) =1 ,
     where k is the length of 'key' list. after finding the functional value of each index that represent the position of the characters in the message to be encrypted 
    in the <key> list, we change the characters in the message to characters in the <key> list, which are in the positions of the functional value of indeces which represent the 
    position of the corresponding characters in the message to be encrypted in the "key" list.  

    To decrypt a message first we find the index of each character which are in the message to be decrypted in the list we have designated it by <key> in the constructor of the 
    affine class and we find the functional value of this  indexes when they pass into the bijection function f(p)= (s(p-b)) mod k, where s is an inverse of 'a' modulo k, where 
    k is length of <key>, and  a modulo 95 can have inverse if gcd(a,95) = 1. after finding the functional value of each index that represent the position of the characters in 
    the message to be decrypted  in the "key" list, we change the characters in the message to characters in the "key" list, which are in the positions of the functional value 
    of indexes which represent the position of the corresponding characters in the message to be decrypted in the "key" list. 

    In the class we have a method named < find_inv_mod(a, m) > that returns the inverse modulo of a (mod m). This is called in the < decrypt > method to solve the linear congruency 
    problem to get the original message character index in the  <key> from the index of the encrypted message character in the <key> list.


> The reason why the encryption and the decryption work in the program:

    First it checks if gcd(a, 95) = 1, if this isn't the case it gives an error message. This handles the exception well with out crushing or giving out error result (runtime error).

    For encryption, as stated in the concept part this program encrypts a message first by finding the position 'p' of a character in the message in the list <key>. And then 
    calculate functional value of 'p' by using the function f(p) = (a(p) + b) mod 95 ,and then substitute the character in the message by characters in list <key> in the position of f(p). 
    The program does this, first it create an empty string < encrypted_text >. Then it access every character in the message and correspondingly find position 'p' by using 
    function < key.index(character) > which apply on lists and then concatenate a character in 'key' at the position f(p). After it has finished iteration in the message it return
    the encrypted_text. 
    
    For decryption, as stated in the concept part this program decrypts a message first by finding the position 'p' of a character in the message in the list <key>. And then 
    calculate functional value of 'p' by using the function f(p)= (find_mod_inv(a, 95) * (p - b)) mod 95, and then substitute the characters in the message by characters in list <key> 
    in the position of f(p). 
    The program does this, first it create an empty string < decrypted_text >. Then it access every character in the message and correspondigly find position 'p' by using 
    function < key.index(character) > which apply on lists and then concatenate a character in < key > at the position f(p). After it has finished itration in the message it return 
    the decrypted_text.

B, Transposition cipher:

> How to run the program to encrypt and decrypt a message (string) using affine cipher:

    To run the program follow the following steps.

    1. Create an object of transposition cipher class by passing the neccesary arguments to the constructor, these neccerary arguments are two integers 'length' and 'arrange' , where 
        'length' represent the length of the substring, and 'arrange' represent the permutation functions.
        >>> private_key = transposition(4, 4321)
         where length = 4, arrange = 4321

    2. To encrypt a message call the functon encrypt by passing the message as a string to function as an argument by using the object created in the first step.
        >>>  privateKey.encrypt("hi friend")
         where < hi friend > is the string  message to be encrypted.

    3. To decrypt a message call the functon decrypt by passing the message as a string to function as an argument by using the object created in the first step.
        >>> privateKey.decrypt("hi friend")
         where < hi friend > is the string message to be encrypted.

       To decrypt a message that has been encrypted by using the encrypt function you can call the function decrypt using the encrypted message as an argument.
        >>> privateKey.decrypt(privateKey.encrypt("hi friend"))
         where <hi friend> is the string message that has been encrypted before.

Note: All the above steps are included in the __main__() method, and the user can interact with the program by choosing the appropriate choices asked by the program. 

> Concepts we used while implementing transposition cipher:    

    To encrypt a message using transposition cipher, first the message is divided into substring with length of the substrings equal to the key, 'length', if the length 
    of the message is not the multiple and then it rearrange the characters in the substrings using the permutation functions, 'arrange'. Finally it concatenate the 
    rearranged substrings to one string, which is the encrypted message.

    To decrypt a message using transposition cipher, first the message is divided into substring with length of the substrings equal to the key, 'length', and then it 
    rearrange the characters in the substrings using the inverse of permutation functions, 'arrange'. 
    Finally it concatenate the rearranged substrings to one string, which is the decrypted message.


> The reason why the encryption and the decryption work in the program:

    For encryption, as stated in the concept part , in the encrypt function first the message is divide into substrings with length equal to the key 'length' by using the 
    'split(message, length)'. Then it rearranges the characters in each substings in the splitted message list base din the given <arrange> key, to create an encrypted message.

    For decryption, as stated in the concept part, in the decryption function first the message is divide into substrings with length equal to the key 'length' by using 
    the 'split(message, length)'. After this it does the reverse process of arranging the characters in each substings in the splitted message list, in the inverse order 
    from the given <arrange> key.

C, RSA cipher:

> How to run the program to encrypt and decrypt a message (string) using affine cipher:
    To run the program follow the following steps.

    1. Create an object of RSA class. This is done as shown below:
        >>> newrsa = RSA()

    2. Generate private and public key be using the generatekeys(p, q), where the arguments p and q must be two prime numbers. This i sdone as shown below:
        >>> newrsa.generatekeys(3, 37)
         3 and 37 are the prime numbers used here as an example, but can be any other prime number. It is preferred for the numbers to be as large as possible
         to avoid being cracked, but this means it takes larger time not only to generate the keys but also to encrypt and decrypt the message. And obviously
         our choice of these numbers must consider the resources we have( our pc's speed and processor and the like).

    3. To encrypt a message call the functon encrypt by passing the message as a string to function as an argument by using the object created in the first step.
        >>>  newrsa.encrypt(" Meet me at the Park ")
         where < Meet me at the Park > is the string  message to be encrypted. THis returns a list with number elements that is the encrypted message.

    4. To decrypt a message call the functon decrypt by passing the encrypted list of numbers to function as an argument by using the object created in the first step.
        >>> newrsa.decrypt([9, 36, 36, 51, 400, 71, 36, 400, 92, 51, 400, 51, 57, 36, 400, 39, 92, 46, 93])
         This list is an encrypted message using the corresponding public key.

Note: All the above steps are included in the __main__() method, and the user can interact with the program by choosing the appropriate choices asked by the program. 

    
> Concepts we used while implementing RSA cipher:

    => The generatekeys(p, q) method uses the arguments which are two prime numbers to generate the public and private keys of the respective class which can later be used by
    encrypt(msg) and decrypt(msg) methods respectively. This is done so by using a number of other functions implemented within this method.
        # isprime(num) : checks the primality of the entered numbers which are p and q, This ensures we get a correct public and private keys to encrypt and decrypt the
         message respectively.

        # find_mod_inv(a,m) : This method returns the modular inverse of < a mod m >

        # egcd(e,r):

        # eugcd(e,r):
    
    => The encrypt(msg) method uses the public key generated in the < generatekeys > method to encrypt characters in the message, using the RSA encryption formula : c = (m**e)%n
     where e is from the public key.
     This handles all types of characters like alphabets( uppercase or lowercase), symbols and space. 

    => The decrypt(msg) method has access to the private key generated by the < generatekeys > method. And it uses this to decrypt the <msg>. <msg> here is of type list and it is
     a list of integers. To decrypt these to the original message it uses the RSA decryption formula m = ((c) ** d) % n where d is from the private key. Then is concatenates the
     chr(m) to an empty string. It does this for every number in the inputted msg list. FInally returning the string, which id the decrypted message.


    >>> Addis Ababa Institute of Technology
    >>> Department of SiTE
    >>> SECTION: 1
    

>>>|        Name                |   ID number     |
>>>|    1. Dawit Zeleke         |     UGR/7912/13 |
>>>|    2. Kena Tekalign        |     UGR/6147/13 |
>>>|    3. Nathnael Dereje      |     UGR/8587/13 |
>>>|    4. Zekariyas Teshager   |     UGR/5480/13 |

submitted to : Estifanos Sisay
Submittion date: 8/10/22 G.c
