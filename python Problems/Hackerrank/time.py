string=input("Enter the time:\n");
hh=int(string[0:2])
mm=string[3:5]
ss=string[6:8]
d=string[8::]
# print(hh)
# print(mm)
# print(ss)
# print(d)
if(hh==12):
    if(d=="AM"):
        hh1=str(hh-12);
        fhh=hh1.zfill(2);
        print(fhh+":"+mm+":"+ss);
if(hh==12 and d=="PM"):
    hh1=str(hh);
    fhh=hh1.zfill(2);
    print(fhh+":"+mm+":"+ss);
if(hh!=12 and d=="AM"):
    hh1=str(hh);
    fhh=hh1.zfill(2)
    print(fhh+":"+mm+":"+ss);
if(hh!=12 and d=="PM"):
    hh1=str(hh+12);
    fhh=hh1.zfill(2)
    print(fhh+":"+mm+":"+ss);