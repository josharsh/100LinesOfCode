sel = input("Shape of antenna should be (R)ectangle/(C)circle: ");
sel = sel.lower()
if (sel == "r") or (sel =="c"):
    pw = 1e+6
    pl = 1e+4
    PI = 3.14
    eef = delL = lef = length = radius = 0.00
    c = 3*10 ** 8
    fo = float(input("Enter the value of frequency to be tune (in Ghz): "))
    er = float(input("Enter the value of dielectric constant: "))
    h = float(input("Enter the value of height of dielectric (in mm): "))
    w = c/(2*fo*(((er+1)/2) * 0.5))
    eef = ((er+1)/2)+((er-1)/2)*((1+12 * (h/w))**(-0.5))
    delL = 0.412*h*(((eef+0.3)*((w/h)+0.264))/((eef-0.258)*((w/h)+0.8)))
    lef = c/(2*fo*(eef**0.5))
    length  = lef-(2*delL)
    w = w/pw
    length = length/pw
    pwidth = "{:.2f}".format(w)
    plength = "{:.2f}".format(length)

    if sel == "r":
            print ("Width: ", pwidth,"mm")
            print ("length:", plength,"mm")
            sel1 = input("Would you like to calculate efficiency (Y)es/(N)o: ");
            sel1 = sel1.lower()
   
            if sel1 == "y":
                gn= float(input("How much will be your input gain (in dBi): "))
                radius = (((w+h)*(length+h)) ** 0.5)/2
                efn = (((c/(fo*1e+9))/(PI*2*radius)) **2)*(10 ** (gn/10))*100
                pefn = "{:.5f}".format(efn)
                print ("Your antennas efficiency will be:", pefn, "%")
            elif sel1 == "n":
                print ("Ok, No problem")
            else:
                print ("You must choose right option to work on.")
   
    elif sel == "c":
            radius = (((w+h)*(length+h)) ** 0.5)/2
            pradius = "{:.2f}".format(radius)
            print ("radius :", pradius,"mm")
            sel1 = input("Would you like to calculate efficiency (Y)es/(N)o: ");
            sel1 = sel1.lower()
   
            if sel1 == "y":
                gn= float(input("How much will be your input gain (in dBi): "))
                efn = (((c/(fo*1e+9))/(PI*2*radius)) **2)*(10 ** (gn/10))*100
                pefn = "{:.5f}".format(efn)
                print ("Your antennas efficiency will be: ",pefn, "%")
            elif sel1 == "n":
                print ("Ok, No problem")
    
    
else:
   print ("You should select proper shape")