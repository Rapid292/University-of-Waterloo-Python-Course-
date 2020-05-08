# Goodness of words
def goodNess(K):
   index = 0
   goodness_Value = []
   for i in K:
      good = 0
      for j in i:
         if j==' ':
            pass
         else:
            index = ord(j)-64
         good += letterGoodness[index-1]
      goodness_Value.append(good)
      max_prob = goodness_Value.index(max(goodness_Value))
   return K[max_prob]


#Goodness Values of alphabets
letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127,
 0.0223, 0.0202, 0.0609, 0.0697, 0.0015,
 0.0077, 0.0402, 0.0241, 0.0675, 0.0751,
 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276,
 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]


# Decryption
def Decrypt(S):
   list = []
   for x in range(0, 26):
      M = ''
      for i in S:
         if i==' ':
            l = ord(i)
         else:
            l = ord(i)+x
            if l>90:
               l = l-26
         M += chr(l)
      list.append(M)
   print(goodNess(list))
   
# Encryption
def Encrypt(S):
   M = ''
   for i in S:
      if i==' ':
         l = ord(i)
      else:
         l = ord(i)-1
         if l<65:
            l = l+26
      M += chr(l)
   print(M)      
Decrypt('UZHAGZU BGTSHZ GZH')