# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
my_dict = dict()
result = []

for i in range(N):
    #arr = list(map(str, input().rstrip().split()))
    key, value = input().split()
    my_dict[key]=value
    

for j in range(N):
        value = input()
        if value in my_dict:
            print("%s=%s" % (str(value), my_dict[value]))
        else:
            print("Not found")
       
