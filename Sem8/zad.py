
# with open("file.txt","w") as f:
#     f.write("123")
#     f.write("abcg")
#     f.close()
# with open("file.txt","a") as f:
#     f.write("123")
#     f.write("abcg")
#     f.close()
# with open("file.txt","r+") as f:
#     print(f.read())
#     f.write("end")
#     f.seek(0)
#     print(f.read())

with open("file.txt","w+") as f:
    a=['1234\n','abcd\n','9876\n']
    f.writelines(a)
with open("file.txt","r") as f:
    a=f.readline()
    print(a)
    a=[i.strip() for i in a]
    print(a)