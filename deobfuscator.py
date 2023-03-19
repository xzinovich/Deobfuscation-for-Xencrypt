import re
import base64
import zlib

# read the input file
with open("input.ps1", "r") as f:
    data = f.read()

# regex pattern to match the encrypted data and encryption parameters
pattern = r'([`r`n])\$encrypted_data = `@"`r`n(?P<data>.+?)`r`n"@\$(?P<variables>(.|\n)+?)Invoke-Expression \$deobfuscated'

# loop through the code and extract the encrypted data and encryption parameters for each iteration
while True:
    match = re.search(pattern, data)
    if not match:
        break

    # extract the encrypted data and encryption parameters
    encrypted_data = match.group("data")
    variables = match.group("variables")

    # decode the base64 encrypted data
    encrypted_data = base64.b64decode(encrypted_data.encode())

    # extract the encryption key and parameters from the variables
    key = base64.b64decode(re.search(r"\$key = `"(.*?)`";", variables).group(1).encode())
    iv = re.search(r"\$iv = `\$(.*?)\[[0-9]+\.\.[0-9]+\];", variables).group(1).encode()
    cipher_mode = re.search(r"\$aesManaged.Mode = \[System\.Security\.Cryptography\.CipherMode\]::(ECB|CBC);", variables).group(1)
    padding_mode = re.search(r"\$aesManaged.Padding = \[System\.Security\.Cryptography\.PaddingMode\]::(PKCS7|ISO10126|ANSIX923|Zeros);", variables).group(1)

    # decrypt the data using the encryption key and parameters
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = aes.decrypt(encrypted_data)
    decrypted_data = zlib.decompress(decrypted_data)

    # replace the encrypted data with the decrypted data in the PowerShell code
    data = data[:match.start("data")] + decrypted_data.decode() + data[match.end("data"):]

# write the deobfuscated PowerShell code to the output file
with open("output.ps1", "w") as f:
    f.write(data)
