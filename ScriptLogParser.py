import re
#initial pattern to be matched while reading the file line to extract the required line only
pattern=re.compile(r'^INFO.* \s\@.*\s\@\s.*[=].*[took]\s[t].*')
#opening the file from disk
inp=open('C:\Windows\_var_log_tomcat7_catalina.OUT-1382601662','r')
file=inp.read()
lines=file.split('\n')
ls1=[];ls=[];mytemp=[];mytemp1=[]
for line in lines:
    if re.match(pattern,line):
         #if line found from above condition will be further break down on basis of @  sign and will be stored in 'ls' list
        ls=line.split('@')
       #ls1 list store only index value 3 which contain URL and time has taken by specific URL
        ls1.append(ls[2])
#to show the content of ls1 list you can uncomment and next time it executed it will show the list ls1 all items
#print(ls1)

#Now we will extract only URLs and Time and we are splitting on the basis of '
for i in ls1:
    temp=i.split("'")
    #mytemp contain all the URL visited
    mytemp.append(temp[1])
    #mytemp1 contain time took by each URL visited and time contain milli second 'ms' string as well
    mytemp1.append(temp[-2])
#print(mytemp)  #contain all the url visited

count=0;tmp=[]
#Cleaning mytemp1 to remove milli second 'ms' from time and will be store in tmp
for i in mytemp1:
   i=re.findall(r'([0-9.]+)',i)
   tmp.append(''.join(i))
   count+=1
#print(tmp)  #tmp contain time in integer

#Now it's time to count the Unique URL and Number each URL visited
tmp4=[];tmp7=[];tmp6=[]
tmp4=list(set(mytemp)) #tmp4 contain list of list of unique url
tmp4=sorted(tmp4,reverse=True)
visitcount=[];unqurl=[]
for i in tmp4:
    unqurl.append(i)
    visitcount.append(mytemp.count(i))
print('Total Unique URL founds are ' +str(unqurl))
print('Total Invocations of Unique URL are ' +str(visitcount))
#count=0;sum=0;mult=1;result=0
tmp8=[]

def repetition(val):
    totalcount=0;  result=0;previousvalue=0
    #This for loop will check for UUID in the URL if found it 
    # will replace it with * otherwise it will show the original value passed as argument to the function
    for x in range(len(mytemp)):
        if(mytemp[x]==val):
            pattern=re.compile(r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}')
            if(len(val)>0):
             tmpstr=str(val)
             reg=pattern.sub(' * ',tmpstr)
            tmp7.append(x)
    totalcount=len(tmp7)
    #this loop find the average time by adding the value divided by number of occurrance
    for i in range(len(tmp7)):
        tmp6.append(tmp[tmp7[i]])
        tmp8.append(mytemp[i])
        previousvalue=int(tmp6[i])  #*int(tmp5[i])
        result+=previousvalue
    print("average time took " +str(round(result/totalcount))+'ms' +' and number of invocations are ' +str(totalcount) +' for URL ' +str(reg))

val=int(input(print('Enter index for URL to display e.g.; 0 for first URL to be displayed and 1 for second and so on\n ')))
#for i in range(len(tmp4)):
repetition(tmp4[val])




