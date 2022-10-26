t=int(input("test case= "))
li=[];
k=0;

while t>0:
    t=t-1;
    k=k+1;
    print("case =",k);
    a=int(input("how many student "))
    b=int(input("pices "))
    mul=a*b;
    p=int(mul/4);
    add=mul%4;
    if add>0:
        p=p+1;
    li.append(p);
    print(p);
    print("___________________________________________________");
print("cakes+");
for x in li:
    print(x)
g=input("THANK you !");

