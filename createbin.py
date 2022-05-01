import io
#initialize string
strApiKey = "ODQxNzQ5Mzk3MzA2MjEyMzcy.YJrSNw._LN0UYK3CXXDo9guZsEp_uwIRPE"
#open file as a binary file
f = open('api_file.bin', 'wb')
#convert string to bytes
strBytes = strApiKey.encode()
#write byte string to binary file
f.write(strBytes)
f.close()