slowo=input("podaj slowo    ")
p1_list=["a", "e", "i","n", "o", "r","s","w","z"]
p2_list=["c","d","k","l","m","p","t","y"]
p3_list=["b","g","h","j","ł","u"]
p5_list=["ą","ę","f","ó","ś","ż"]
p6_list=["ć"]
p7_list=["ń"]
p9_list=["ź"]
p1=0
p2=0
p3=0
p5=0
p6=0
p7=0
p9=0
for i in p1_list:
    p1+=slowo.count(i)
for i in p2_list:
    p2+=slowo.count(i)
for i in p3_list:
    p3+=slowo.count(i)
for i in p5_list:
    p5+=slowo.count(i)
for i in p6_list:
    p6+=slowo.count(i)
for i in p7_list:
    p7+=slowo.count(i)    
for i in p9_list:
    p9+=slowo.count(i)    

point=p1+p2*2+p3*3+p5*5+p6*6+p7*7+p9*9
print(point)