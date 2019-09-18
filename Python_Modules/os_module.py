import os

print(os.name) # output => "nt" for windows // "posix" for MacOs and GNU/linux

print(os.sep) #output => "\\" for Windows // "/" for MacOs and Linux 

liste=["bear","cat","dog"]
a=os.sep.join(liste)
print(a)  #=> output :   bear\cat\dog



print("Current Working Directory is " + os.getcwd())

#get file names from folder
file_list=os.listdir(r"C:\Users\Administrator\Desktop\deneme")
print(file_list)

os.chdir(r"C:\Users\Administrator\Desktop\deneme") #go to different directory
print(os.getcwd())

for i in os.listdir(os.getcwd()):
    print(i)
    if i.endswith(".txt"):
        print("====",i)  #if you want only .txt extension 

#os.mkdir("rgrg") #create a new file
#os.makedirs(r"C:\Users\Administrator\Desktop\deneme\go\go\next")  # => create nested files  
#os.startfile("deneme.txt") # only work Windows
#os.startfile("www.google.com.tr") #again only work Windows if you want different OS you can use webbrowser.
#os.rename("go","ileri")
file=os.stat("deneme")
print(file)
print(file.st_size/1024)
print(os.urandom(10)) #create random byte for cryptology,password,bitcoin

