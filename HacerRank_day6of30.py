'''
Given a string, S , of length N that is indexed from 0 to N-1 , 
print its even-indexed and odd-indexed characters as space-separated strings on a single line 
'''
 
# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    T = int(input())
    S = ''
    even_string =''
    odd_string = ''

    for item in range(T):
        S = input()

        for index in range(len(S)):
            if index % 2==0:
                even_string += S[index]
            else:
               odd_string += S[index]
        
        print("%s %s" % (even_string, odd_string))
        even_string = ''
        odd_string = ''
    
  
        
