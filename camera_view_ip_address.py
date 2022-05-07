import socket    
host_name = socket.gethostname()    
IPAddress = socket.gethostbyname(host_name)    
print("Your Computer Name is:" + host_name)    
# print("Your Computer IP Address is:" + IPAddress) 
myport = ":5000"
myIP = str(IPAddress)
camera_view_url = "http://"+myIP+myport
print("CAMERA_VIEW_URL:", camera_view_url)