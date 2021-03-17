import argparse
from ecdsa import SigningKey, VerifyingKey, NIST256p
from pathlib import Path
import hashlib

parser = argparse.ArgumentParser(
    description="Generate key pairs and e-signature for binary file and appends signature as well")
parser.add_argument("-gen_key", type=str,
                    help=" Generating public.bin and private.bin files")
parser.add_argument("-Dir", type=str,
                    help=" Provide Output path to store files")
parser.add_argument("-Hash_gen", type=str,
                    help=" Generating Hash value for binary image")
parser.add_argument("-i", type=str,
                    help=" Provide Input Binary Image path")
parser.add_argument("-Private_key", type=str,
                    help=" Provide Private Key path(Private_key.bin)")
parser.add_argument("-verify", type=str,
                    help=" Verifies input signature file against the input public-key file and input binary-image.")
parser.add_argument("-Public_key", type=str,
                    help=" Provide Public Key path(Public_key.bin)")
parser.add_argument("-signature", type=str,
                    help=" Input signature file for signature verification")
parser.add_argument("-append", type=str,
                    help=" Append signature to input binary image")
parser.add_argument("-gen_sign", type=str,
                    help=" Generate signature file")

args = parser.parse_args()
hash_value = list()

# Generating Public and Private Key
if args.gen_key == "Keypair":
    Prk = SigningKey.generate(curve=NIST256p)  # Generating Private key
    Prk_string = Prk.to_string()  # Store key in form of bytes
    Puk = Prk.verifying_key  # Generating public key
    Puk_string = Puk.to_string()  # Store key in form of bytes
    vk2 = VerifyingKey.from_string(Puk_string, curve=NIST256p)
    # PrkString = Prk_string.hex()  # store key in form of str
    # PukString = vk2.to_string().hex()  # store key in form of str
    if Path(args.Dir).is_dir():
        print()
    else:
        Path(args.Dir).mkdir(parents=True, exist_ok=False)
    file = open(args.Dir + "\\Private_key.bin", "wb")  # creating private.bin file
    file.write(Prk_string)
    file.close()

    file1 = open(args.Dir + "\\Public_key.bin", "wb")  # creating public.bin file
    file1.write(Puk_string)
    file1.close()
    print('''INFO:root:*** Generating key-pair. *** 
    INFO:root:--- Key-pair successfully generated. ---''')
elif args.gen_key != None:
    print('''ERROR:root:Wrong command.
                     Usage: python file_name.py -gen_key Keypair  -Dir <Output Directory>''')

# Generating Hash Value for Binary image
if args.Hash_gen == "hash" or args.gen_sign == "sign":
    try:
        f2 = open(args.i, "rb")
        data = f2.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(data).hexdigest()
        if args.gen_sign != "sign":
            print("INFO:root:", readable_hash)  # Generating Hash value for binary image
        hash_value.append(readable_hash)
        f2.close()
    except FileNotFoundError:
        print('''ERROR:root:Cannot locate input image file.
           Please try again with the correct image file.''')
elif args.Hash_gen != None:
    print('''ERROR:root:Wrong command.
                     Usage: python file_name.py -Hash_gen hash -i <Binary Image Path>''')

# Generating Signature
if args.gen_sign == "sign":
    try:
        e_sign = bytes(hash_value[0], "utf-8")  # converting hex to bytes
        f5 = open(args.Private_key, "rb")
        f6 = f5.read()
        Prk1 = SigningKey.from_string(f6, curve=NIST256p)  # Reading Private Key from Private_key.bin file
        signature = Prk1.sign(e_sign)  # takes input as bytes
        # print(type(signature))
        if Path(args.Dir).is_dir():
            print()
        else:
            Path(args.Dir).mkdir(parents=True, exist_ok=False)
        f2 = open(args.Dir + "\\Signature.bin", "wb")  # Generating Signature.bin file
        f2.write(signature)
        f2.close()
        print('''INFO:root:--- Generating Signature ---
    INFO:root:--- signature.bin file successfully created --- ''')
    except FileNotFoundError:
        print('''ERROR:root:Cannot locate input image file.
           Please try again with the correct path for Private_key.bin file.''')
elif args.gen_sign != None:
    print('''ERROR:root:Wrong command.
                     Usage: python file_name.py -gen_sign sign -i <Binary Image Path> -Private_key <Private_key.bin Path> 
                     -Dir <Output Directory>''')

# Verification
if args.verify == "Verify":
    try:
        f7 = open(args.Public_key, "rb")
        f8 = f7.read()
        Puk1 = VerifyingKey.from_string(f8, curve=NIST256p)  # Reading Public Key from Public_key.bin file
        signature = open(args.signature, "rb")
        f9 = signature.read()
        hash_value = list()
        hash = open(args.i, "rb")
        data = hash.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(data).hexdigest()
        # print(type(readable_hash))
        hash_value.append(readable_hash)
        readable_hash = bytes(hash_value[0], "utf-8")
        Verify = Puk1.verify(f9, readable_hash)  # Verifying with Public key and Hash Value
        if Verify == True:
            print("INFO:root:Verified OK!")
    except FileNotFoundError:
        print('''ERROR:root:Cannot locate input image file.
           Please try again with the correct path for Public_key.bin file.''')

# Generating Signed Document
if args.append == "append":
    f3 = open(args.i, 'ab')
    f4 = open(args.signature, 'rb')
    f5 = f4.read()
    f3.write(f5)  # Appending the signature with Binary file
    f3.close()
    print('''INFO:root:---Over-writing input image file---
            INFO:root:---Signature append complete---''')

'''

C:\\Users\\99002561\\PycharmProjects\\My_Practice
# -gen_key Keypair -Dir .\
# -Hash_gen hash -i slick.bin
# -gen_sign sign -i slick.bin -Private_key Private_key.bin -Dir .\
# -verify Verify -i slick.bin -signature Signature.bin -Public_key Public_key.bin
# -append append -i slick.bin -signature Signature.bin

1) e_sign.exe -genkey keypair -dir .\
2) e_sign.exe -hash_gen hash -i wf_ota_44932.bin
3) e_sign.exe -gen_sign sign -i wf_ota_44932.bin -private_key private.bin -dir .\
4) e_sign.exe -verify verify -i wf_ota_44932.bin -signature signature.bin -public_key public.bin
5)e_sign.exe -append append -i wf_ota_44932.bin -signature signature.bin

'''
