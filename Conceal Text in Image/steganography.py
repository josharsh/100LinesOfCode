from PIL import Image

# Convert encoding data into 8-bit form using ASCII value of characters
def genData(data):

        # list of binary codes of given data
        newdata = []

        #Getting 8 bits bianry representation of the letters present in the string.
        for i in data:
            newdata.append(format(ord(i), '08b'))
        return newdata


# Pixels are modified according to the 8-bit binary data and finally returned
def alterPixel(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    
    # The iter() function creates an object which can be iterated one element at a time.
    iterdata = iter(pix)
    
    
    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in iterdata.__next__()[:3] + iterdata.__next__()[:3] + iterdata.__next__()[:3]]

        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        '''
        Eighth pixel of every set tells whether to stop or read further.
        0 means keep reading; 1 means the message is over.
        i==lendata-1 means we read the last 8-bit binary value
        '''
        if (i == lendata - 1): 
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)

        '''
        yield is a keyword in Python that is used to return from a function 
        without destroying the states of its local variable 
        and when the function is called, the execution starts from the last yield statement.
        '''
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
        

#Encoding the data 
def encode_data(cloneimg, data):
    
    # w is the width of the image
    w = cloneimg.size[0]
    (x, y) = (0, 0)

    '''
    getdata() Returns the contents of this image as a sequence object containing pixel values. 
    The sequence object is flattened, so that values for line one follow directly after the values of line zero, 
    and so on.
    The default is to return all bands. 
    To return a single band, pass in the index value (e.g. 0 to get the “R” band from an “RGB” image).
    '''
    #print(alterPixel(cloneimg.getdata(), data))
    for pixel in alterPixel(cloneimg.getdata(), data):

        # Putting modified pixels in the new image
        cloneimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
            
    #print("Sucess!")


# Encode data into image
def encode(img,data,new_img_name):
    image = Image.open(img, 'r')
    
    if (len(data) == 0):
        raise ValueError('Empty data received from the user.')

    cloneimg = image.copy()
    encode_data(cloneimg, data)

    cloneimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    return True


#encode("pic.png","Hello", "testimg9.png")


# Decode the data in the image
def decode(img):
    image = Image.open(img, 'r')

    data = ''
    # The iter() function creates an object which can be iterated one element at a time.
    iterdata = iter(image.getdata())
    while True:
        pixels = [value for value in iterdata.__next__()[:3] + iterdata.__next__()[:3] + iterdata.__next__()[:3]]

        # string of binary data
        binarystr = ''
        #Each string of 8-bit binary data would represent a letter/character
        for i in pixels[:8]:
            if (i % 2 == 0):
                binarystr += '0'
            else:
                binarystr += '1'

        data += chr(int(binarystr, 2))
        if (pixels[-1] % 2 != 0):
            return data
            
#print(decode("testimg9.png"))