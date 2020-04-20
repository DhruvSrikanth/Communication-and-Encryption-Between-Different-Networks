import socket
from Crypto import Crypto
from sys import exit

crypto = Crypto()
print("Socket programming with Encryption and decryption")

def get_input_message(*choice):

  global message
  global key
  message = ''
  
  print("The following cryptography functions are available to choose from. Please select a choice")
  print("1. Caesar Cipher \n \
        2. Decimation Cipher \n \
        3. Linear Cipher \n \
        4. Morse Code \n \
        5. Keyword Cipher \n \
        6. Exit")
  try:
    choice = int(input("Enter your choice (num): "))
    if choice in (1,2,3,4,5,6):
      if choice == 6:
        quit()
      else:
        pass
    else:
      print("Invalid Choice")
      get_input_message()
  except:
    print("Invalid Choice")
    get_input_message()

  data = input("Enter the message to be sent: ").split()
  # return choice
  cipher_text = ""
  if choice == 1:
    try:
      key = int(input("Enter key value: "))
      for word in data:
        cipher_text += crypto.caesar_cipher(word,key) + " "
      message = "c1" + "_" + cipher_text + "_" + str(key)
    except:
      print("Key Value Must Be An Integer")
      get_input_message()
  elif choice == 2:
    try:
      key = int(input("Enter key value: "))
      for word in data:
        cipher_text += crypto.decimation_cipher(word,key) + " "
      message = "c2" + "_" + cipher_text + "_" + str(key)
    except:
      print("Key Value Must Be An Integer")
      get_input_message()
  elif choice == 3:
    try:
      a = int(input("Enter \"a\" value: "))
      b = int(input("Enter \"b\" value: "))
      for word in data:
        cipher_text += crypto.linear_cipher(word,a,b) + " "
      message = "c3" + "_" + cipher_text + "_" + str(a) + "_" + str(b)
    except:
      print("\"a\" And \"b\" Must Be Integers")
      get_input_message()
  elif choice == 4:
    try:
      for word in data:
        cipher_text += crypto.morse_code(word) + " "
      message = "c4" + "_" + cipher_text
    except:
      get_input_message()
  elif choice == 5:
    try:
      keyword = input("Enter the keyword: ")
      for word in data:
        cipher_text += crypto.keyword_cipher(keyword,word) + " "
      message = "c5" + "_" + cipher_text + "_" + keyword
    except:
      get_input_message()

def Main():

  host='::1' #client ip
  port = 4005

  server = ('::1', 4000)

  s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
  s.bind((host,port))
  
  while True:
    try:
      get_input_message()
      print(message)
    except SystemExit:
      s.close()
      print("Terminating")
      return
    s.sendto(message.encode('utf-8'), server)
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("Received from server: " + data)

if __name__=='__main__':
  Main()
