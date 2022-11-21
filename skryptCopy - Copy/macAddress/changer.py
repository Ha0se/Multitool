
def output(output):
  print()
  print(output.lower())
  print(output.upper())
  print()
  

def changer():
  while True:
    
    menu = input("Jak chcesz by twoj Macaddress wygladal\n1: AA-AA-AA-AA-AA-AA\n2: AA:AA:AA:AA:AA:AA\n3: AAAA.AAAA.AAAA\n4: break\n: ")
    if menu == "4":
      break
      
    macaddr = input("Wpisz macaddress: ")
    temp = macaddr
    
    if temp[2] == "-" and len(macaddr) == 17:
      
      if menu == "1":
        temp2 = temp.replace("-","-")
        
        output(temp2)
        
      elif menu == "2":
        temp2 = temp.replace("-",":")
        
        output(temp2)
        
      elif menu == "3":
        temp2 = list(temp)
        temp3 = list(temp)

        temp2[0]=temp3[0]
        temp2[1]=temp3[1]
        temp2[2]=temp3[3]
        temp2[3]=temp3[4]
        temp2[4]=temp3[2]
        temp2[5]=temp3[6]
        temp2[6]=temp3[7]
        temp2[7]=temp3[9]
        temp2[8]=temp3[10]
        temp2[9]=temp3[5]
        temp2[10]=temp3[12]
        temp2[11]=temp3[13]
        temp2[12]=temp3[15]
        temp2[13]=temp3[16]

        temp2.pop(14)
        temp2.pop(14)
        temp2.pop(14)
        
        temp4 = ""

        for i in range(0,14) :
          temp4 = temp4 + temp2[i]
      
        temp4 = temp4.replace("-",".")
        
        output(temp4)
        
        
    elif temp[2] == ":" and len(macaddr) == 17:

      if menu == "1":
        temp2 = temp.replace(":","-")
        output(temp2)
        
      elif menu == "2":
        output(temp)
        
      elif menu == "3":
        temp2 = list(temp)
        temp3 = list(temp)

        temp2[0]=temp3[0]
        temp2[1]=temp3[1]
        temp2[2]=temp3[3]
        temp2[3]=temp3[4]
        temp2[4]=temp3[2]
        temp2[5]=temp3[6]
        temp2[6]=temp3[7]
        temp2[7]=temp3[9]
        temp2[8]=temp3[10]
        temp2[9]=temp3[5]
        temp2[10]=temp3[12]
        temp2[11]=temp3[13]
        temp2[12]=temp3[15]
        temp2[13]=temp3[16]

        temp2.pop(14)
        temp2.pop(14)
        temp2.pop(14)
        
        temp4 = ""

        for i in range(0,14) :
          temp4 = temp4 + temp2[i]
      
        temp4 = temp4.replace(":",".")

        output(temp4)

      
    elif temp[4] == "." and len(macaddr) == 14:
      
      if menu == "1":
        temp2 = list(temp)
        temp3 = list(temp)

        temp2.append("")
        temp2.append("")
        temp2.append("")

        temp2[0]=temp3[0]
        temp2[1]=temp3[1]
        temp2[2]="-"
        temp2[3]=temp3[2]
        temp2[4]=temp3[3]
        temp2[5]="-"
        temp2[6]=temp3[5]
        temp2[7]=temp3[6]
        temp2[8]="-"
        temp2[9]=temp3[7]
        temp2[10]=temp3[8]
        temp2[11]="-"
        temp2[12]=temp3[10]
        temp2[13]=temp3[11]
        temp2[14]="-"
        temp2[15]=temp3[12]
        temp2[16]=temp3[13]

        temp4 = ""
        for i in range(0,17) :
          temp4 = temp4 + temp2[i]

        output(temp4)
        
        
      elif menu == "2":
        temp2 = list(temp)
        temp3 = list(temp)

        temp2.append("")
        temp2.append("")
        temp2.append("")

        temp2[0]=temp3[0]
        temp2[1]=temp3[1]
        temp2[2]=":"
        temp2[3]=temp3[2]
        temp2[4]=temp3[3]
        temp2[5]=":"
        temp2[6]=temp3[5]
        temp2[7]=temp3[6]
        temp2[8]=":"
        temp2[9]=temp3[7]
        temp2[10]=temp3[8]
        temp2[11]=":"
        temp2[12]=temp3[10]
        temp2[13]=temp3[11]
        temp2[14]=":"
        temp2[15]=temp3[12]
        temp2[16]=temp3[13]

        temp4 = ""
        for i in range(0,17) :
          temp4 = temp4 + temp2[i]

        output(temp4)
        
      elif menu == "3":
        output(temp)
        
        
    else:
        print()
        print("zly macaddress")
        pass


