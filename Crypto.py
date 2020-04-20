class Crypto:
  """
  This is a class which contains all the cryptography algorithms studied in Sem-5.
  """
  def __init__(self):
    self.cnst = 26

  def calc_mod_array(self,mod_no):
    """
    This function calculates the modulo multiplication array.\n
    It then returns the array and also a dictionary with the inverse elements.
    """
    self.mod_list = []
    self.key_inv_dict = dict() 
    for i in range(1,mod_no):
      mod_val = []
      for j in range(1,mod_no):
        num = (i*j) % mod_no
        if (num==1):
          self.key_inv_dict.update({i:j})
        mod_val.append(num)
      self.mod_list.append(mod_val)
    return self.mod_list,self.key_inv_dict

  def caesar_cipher(self,text,n):
    """
    This function performs Caesar cipher.\n
    Input is the plain-text to be encrypted and a key used for encryption.\n
    Returns the encrypted text.
    """
    try:
      self.res = ''
      for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
          self.res += chr((ord(char) + n - 65) % 26 + 65)
        elif (char.islower()):
          self.res += chr((ord(char) + n - 97) % 26 + 97)
        elif char.isalpha():
          self.res += chr(ord(char) + n)
        else:
          self.res += char
    except:
      exit("Invalid Input")
    return self.res
  
  def decimation_cipher(self,text,key):
    """
    This function performs Decimation cipher.\n
    Input is the plain-text to be encrypted and a key used for encryption.\n
    Returns the encrypted text.
    """
    crypto = Crypto()
    text = text.lower()
    self.res = ''
    try:
      _,key_inverse = crypto.calc_mod_array(self.cnst)
      if key not in key_inverse.keys():
        print("Invalid Key")
      else:
        for i in range(len(text)):
          char = text[i]
          if char.isalpha():
            self.res += chr(((key*(ord(char)-97))%26)+97)
          else:
             self.res += char
    except:
        exit("Invalid Input")
    return self.res
  
  def linear_cipher(self,text,a,b,Option='Encryption'):
    """
    This function performs Linear cipher.\n
    Input is the plain-text to be encrypted and a key used for encryption.\n
    Returns the cipher/plain text.
    """
    crypto = Crypto()
    text = text.lower()
    self.res = ''
    if Option == 'Encryption':
      res1 = crypto.decimation_cipher(text,a)
      self.res = crypto.caesar_cipher(res1,b)
            
    elif Option == 'Decryption':
      _,key_inverse = crypto.calc_mod_array(crypto.cnst)
      res1 = crypto.caesar_cipher(text,26-b)
      dekey = key_inverse[a]
      res2 = crypto.decimation_cipher(res1,dekey)
      self.res = res2

    else:
      from sys import exit
      exit('Invalid Option Chosen')
  
    return self.res

  def morse_code(self,text,option='Encryption'):
    """
    This function performs Morse encoding/decoding.\n
    Input is the plain-text to be encrypted and a key used for encryption.\n
    Returns the cipher/plain text.
    """
    from sys import exit
    self.res = ''
    morse_dict = {'1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----', \
                    'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..', \
                    'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'-.-','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-', \
                    'y':'-.--','z':'--..'}
    res_en = ''
    res_de = ''
    temp = ''
    try:
      if option == 'Encryption':
        for element in text:
          if element.isalpha():
            temp += element.lower()
          elif element.isnumeric():
            temp += element
          else:
            print("Invalid Input i.e input cannot contain any kind punctuation")
        
        for element in temp:
          res_en += morse_dict[element] + ' '
        self.res = res_en
          
      elif option == 'Decryption':
        text = text.split()
        for element in text:
          for alpha,mcode in morse_dict.items():
            if mcode == element:
                res_de += alpha
        self.res = res_de
      else:
        exit('Invalid Option Chosen')
    except:
      exit("Invalid Input i.e refer morse dictionary for valid inputs @https://en.wikipedia.org/wiki/Morse_code")  
    return self.res

  def keyword_cipher(self,keyword,text,index='a',Option='Encryption'):
    """
    This function performs 2 types of keyword ciphers. Regular and Giovanni's.\n
    It performs encryption and decrption depending on the option input.\n
    Input is the keyword, plain-text for regular keyword cipher and also index for Giovanni's cipher.\n
    Returns the cipher/plain text.
    """
    from sys import exit
    
    crypto = Crypto()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    keyword = keyword.lower()
    res = ''
    for ele in keyword:
      if ele not in res:
        res += ele
      else:
          pass
    
    for ele in alpha:
      if ele not in res:
        res += ele
      else:
          pass
    try:
      if index != 'a':
        res = crypto.rotate(res,alpha.index(index))
      else:
        pass

      alpha_map_dict = dict()
      count = 0
      for let in alpha:
        alpha_map_dict.update({let:res[count]})
        count += 1

      if Option == 'Encryption':  
        encrypted = ''
        for ele in text:
          if ele == ' ':
            encrypted += ele
          else:
            encrypted += alpha_map_dict[ele]
        self.final = encrypted

      elif Option == 'Decryption':
        decrypted = ''
        for ele in text:
          if ele == ' ':
            decrypted += ele
          else:
            for alpha,kcode in alpha_map_dict.items():
              if kcode == ele:
                decrypted += alpha
        self.final = decrypted
      else:
        exit('Invalid Option Chosen')
    except:
      exit("Invalid Input i.e Only letters can be provided as input")
    return self.final
