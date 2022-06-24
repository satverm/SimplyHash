# SimplyHash
A simple python program to hash any text.
## Requirements: You need the python to run the program. 
## How to use: The program generates the sha256( Secure hash algorithm)hash of any input given by the user.
   
 The sha256 is a 256 bit length binary code but we are using the 64 bit hexadecimal output of the same.
 The beauty of the sha256 hashing is that there is no way of finding the output if you don't know the input.
 
 Some people store a list of inputs and its hash pairs to find the input or they have to try all combinations of input and generate the hashes for each of them to find a match ( also called bruteforce attack).
## The simple trick: The sha256 generates a totally new hash digits even if a minor change is done to the input, It means the hashes of 'password' and 'password1' will be totally different. To make it impossible for someone to find the input even by bruteforce is to note down only the first few 4 to 5 characters of the 64 bit code, this way there is no way to find the input as there would be infinite inputs having the same starting 4 to 5 hash code which you have noted.
   
Note: If you wish to store the password and retrieve it later in a secure way, you can use the python program from the Password-Manager repository.
