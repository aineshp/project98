file1  = input('Enter file name: ')
a=open("sampletext1.txt", 'r') 
data_a=a.read()     
file2 = input('Enter second file name: ')
b= open(file2,'r')
data_b=b.read()
def swapFileData(file1,file2,a,b):
    a=open(file1,'w')
    a.write(data_b) 
    b=open(file2,'w')
    b.write(data_a)

    
   