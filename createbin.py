import io
#initialize string
strApiKey = "TOKEN"
#open file as a binary file
f = open('api_file.bin', 'wb')
#convert string to bytes
strBytes = strApiKey.encode()
#write byte string to binary file
f.write(strBytes)
f.close()