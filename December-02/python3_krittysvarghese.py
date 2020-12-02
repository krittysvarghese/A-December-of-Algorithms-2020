n = input("Input: ")
letters = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
first = letters[int(n[0])-1]
second = letters[int(n[1])-1]
out=[]
for i in first:
    for j in second:
        out.append(i+j)
print("Output:",out)
