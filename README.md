# Deobfuscation-for-Xencrypt
The PowerShell code provided is a crypter (obfuscator and fudger) named "Xencrypt". It encrypts and packs the input PowerShell script in order to evade antivirus detection. The script also allows layering the encryption and packing recursively to further avoid detection.

### Reverse Engineering Report - Xencrypt PowerShell Crypter

**The script begins with defining the Create-Var function that generates random characters from the string "abcdefghijkmnopqrstuvwxyz" and creates a variable length for the generated file.

Next, the Invoke-Xencrypt function is defined, which takes the input script and output file as parameters. It also has an optional parameter for the number of times the script will be packed and encrypted recursively, with a default value of 2.

The function first reads the input file and then enters a loop that runs the number of times specified by the iterations parameter. Inside the loop, the encryption parameters (padding mode, cipher mode, key size, and compression type) are decided ahead of time.

The script then compresses the input code using the specified compression type and generates a key for encryption using the AesManaged object. It encrypts the compressed data using the created key and mode, and then writes the encrypted data to the output file.

The order of statements in the code is also randomized within each loop iteration to further increase the variation and make static analysis more difficult.

The encrypted data is then used as input for the next loop iteration, and the process is repeated. Finally, the encrypted and packed data is written to the output file.

To deobfuscate the Xencrypt PowerShell crypter code, a simple Python script can be created that reverses the encryption and packing process. The following steps can be taken:

Read the Xencrypt obfuscated PowerShell code from the input file.
Loop through the code and extract the encrypted data and encryption parameters used in each iteration.
Decrypt the extracted data using the encryption key and parameters for each iteration.
Replace the encrypted data with the decrypted data in the PowerShell code.
Write the deobfuscated PowerShell code to the output file.**
