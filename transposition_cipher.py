
class transposition:

    # The transposition class is initialized with 2 arguments, length = 
    def __init__(self, length, arrange):
        assert type(length) == int, "A noninteger argument given at initializing the class: Integer must be given."
        assert type(arrange) == int, "A noninteger argument given at initializing the class: Integer must be given."
        assert len(str(arrange)) == length , " Arrange should be of length % d" %length

        self.length = length
        self.arrange = arrange
        
    
    def encrypt(self, msg):
        splitted_msg = self.split(msg, self.length)      # the split function splits the message to substrings of length self.length
        encrypted_msg = ""

        for substring in splitted_msg:
            encrypted_substring = []

            # after the loop below encrypted_substring will be a list with self.length number of empty string elements 
            # ["", "" , "" , ... , "" ] => encrypted_substring
            for i in range(self.length):
                encrypted_substring.append("")    

            substring_index = 0
            # assigns characters in substring into encrypted_substring based on the arrangement specified by self.arrange
            for k in str(self.arrange):
                encrypted_substring[substring_index] = substring[int(k)-1]
                substring_index += 1
            
            #  concatenates all string elements in the encrypted_substring to the encrypted_msg string.
            for element in encrypted_substring:
                encrypted_msg += element

        return encrypted_msg


    def decrypt(self, msg):
        splitted_msg = self.split(msg, self.length)           # split the msg into elements of length <self.length> 
        decrypted_msg = ""

        for substring in splitted_msg:
            decrypted_substring = []

            # after the loop below decrypted_substring will be a list with self.length number of empty string elements 
            # ["", "" , "" , ... , "" ] => decrypted_substring
            for i in range(self.length):
                decrypted_substring.append("")

            substring_index = 0
            # assigns characters in substring into encrypted_substring based on the arrangement specified by self.arrange
            for k in str(self.arrange):
                decrypted_substring[int(k) -1] = substring[substring_index]
                substring_index += 1

            #  concatenates all string elements in the encrypted_substring to the encrypted_msg string.
            for char in decrypted_substring:
                decrypted_msg += char
            
        return decrypted_msg

    def split(self, msg, length):
        splitted_msg=[]

        #  adds an underscores to the end of the <msg> to divide it into parts of <length> length evenly, which make 
        #  the encryption amd decryption of the message easier
        while len(msg) % length != 0:
            msg += "_"
       
        i = 0
        j = i + length
        while i < len(msg):
            substring = msg[i:j]                        # splicing the message
            splitted_msg.append(substring)              # appending the created substring into the list  
            i = j
            j = i + length

        return splitted_msg

# ////////////////////////////////////////////////////////////////////////////////////

