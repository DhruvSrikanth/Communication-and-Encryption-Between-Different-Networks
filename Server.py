from Crypto import Crypto
import socket

crypto = Crypto()
def get_message_details(data = ''):
  if data == '':
    decrypted_data = ''
    print("Message Not Decoded Properly!")
  else:
    choice = data.split("_")[0]
    data_portion = data.split("_")[1].split()
    decrypted_data = ''
    if choice == 'c1':
      key = data.split("_")[-1]
      for word in data_portion:
        decrypted_data += crypto.caesar_cipher(word,26-int(key)) + ' '
    elif choice == 'c2':
      try:
        key = data.split("_")[-1]
        _,key_inverse = crypto.calc_mod_array(crypto.cnst)
        dekey = key_inverse[int(key)]
        for word in data_portion:
          decrypted_data += crypto.decimation_cipher(word,dekey) + ' '
      except:
        decrypted_data = "INVALID KEY USED BY CLIENT"
    elif choice == 'c3':
      try:
        a = data.split("_")[-2]
        b = data.split("_")[-1]
        for word in data_portion:
          decrypted_data += crypto.linear_cipher(word,int(a),int(b),'Decryption') + ' '
      except:
        decrypted_data = "INVALID KEY USED BY CLIENT"
    elif choice == 'c4':
      for word in data_portion:
        decrypted_data += crypto.morse_code(word,'Decryption') + ' '
    elif choice == 'c5':
      keyword = data.split("_")[-1]
      for word in data_portion:
        decrypted_data += crypto.keyword_cipher(keyword,word,Option = 'Decryption') + ' '
    else:
      decrypted_data = ''
      print("Message Not Decoded Properly!")

  decrypted_data = decrypted_data.rstrip()
  return decrypted_data


def Main():

  host = '::1' #Server ip
  port = 4000

  s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
  s.bind((host, port))

  print("Server Started")
  while True:
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("Message from: " + str(addr))
    print("From connected user: " + data)
    decrypted_data = get_message_details(data)
    if decrypted_data != '':
      print("Sending: " + decrypted_data)
      s.sendto(decrypted_data.encode('utf-8'), addr)
    else:
      pass
  s.close()

if __name__=='__main__':
  Main()
