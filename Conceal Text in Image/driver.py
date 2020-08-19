import caesar
import argparse 
import steganography

def main():

    print("\n\n********************* ENCODE & DECODE CIPHERED TEXT IN IMAGE *********************")

    # Initialize parser 
    parser = argparse.ArgumentParser() 

    # Adding optional argument 
    parser.add_argument("-k", "--key", help = "insert your shift key for cipher",type=int) 
    parser.add_argument("-m", "--message", help = "insert your message here")
    parser.add_argument("-e", "--encode", help = "name of the image file where we want to hide the message")
    parser.add_argument("-n", "--newimg", help = "name of the new image file where data will be hidden")
    parser.add_argument("-d", "--decode", help = "name of the image file which has the hidden message")
    parser.add_argument("-s", "--syntax", help = "Type 'python filename.py -s YES' or 'python filename.py --syntax YES'")

    
    # Read arguments from command line   

    args = parser.parse_args() 
    syntaxhelp = False
    if args.syntax:
        print("[*] To encode use the following syntax:")
        print("python filename.py -e [image name with extension] -n [new image name with extension] -k [shift key, an integer value] -m [Your string to be encoded within inverted commas]\n")
        print("[*] To decode use the following syntax:")
        print("python filename.py -d [image name with extension where the data is hidden] -k [shift key, an integer value]\n")
        syntaxhelp = True

        
    if syntaxhelp==False:
        if args.encode is None and args.decode is None:
            print("\n\n[-] No arguments were provided.")
            print("[*] Type 'python filename.py -h' or 'python filename.py --help' for help.\n\n")

        if args.encode: 
            print("[*] Encoding data in the image initiated.\n[*] Image name: % s\n" % args.encode)
            if args.key is None or args.message is None or args.newimg is None:
                print("Process terminated due to lack of arguments!")
            else:
                msg = caesar.encrypt(args.message,args.key)
                print("[+] Data ciphered successfully --------- [50%  Completed]")

                feedback = steganography.encode(args.encode,msg,args.newimg)
                if feedback==True:
                    print("[+] Encoding successful ---------------- [100% Completed]\n")
                    print("[+] The new image is saved as: % s\n" % args.newimg)

                
        if args.decode: 
            print("[*] Decoding data from the image initiated")
            print("[*] Image name: % s\n" % args.decode)
            if args.key:
                ciphermsg = steganography.decode(args.decode)
                print("[+] Decoding successful ----------------- [50%  Completed]")
                msg = caesar.decrypt(ciphermsg, args.key)
                print("[+] Data deciphered successful ---------- [100% Completed]\n")
                print("[+] The data decoded and deciphered from the image is: ",msg)
                print("[+] Task Completed")
    

if __name__ == "__main__":
    main() 
