#მოგესალმებით მეგობრებო, მოცემულ შესრულებულ დავალებას ატვირთავთ e-learning-ის პლატფორმაზე.
#ფაილს დაარქვით მსგავსად: quiz 1 - elena bliadze (ჩემი სახელისა და გვარის ნაცვლად თქვენი) 
# პასუხი კოდები დაწერე დაკომენტარებული პირობების ქვემოდს! - > აუცილებელია

#გისურვებთ წარმატებას!



#1. დაწერე პროგრამა, რომელიც მომხმარებელს შეაყვანინებს, მის სახელს, გვარს, ასაკს ერთ ხაზზე
# # და გამოუტანს მისალმებას მაგ: გამარჯობა ელენა ბლიაძე!
name=str(input("sheiyvane seni saxeli : "))
surname=str(input("sheiyvane gvari : "))
age=int(input("input your agee : "))
print(f"hello {name} {surname} you are {age} years old")


# #2. შემოიტანე სამი ცვლადი:  x, y , khariskhi, gayofa, gayofisnasht, jami.
# # მოიფიქრე თუ საჭიროდ ჩათვლი შენთვის საურველი ცვლადი და მოახდინე შემდეგი ოპერაციებია:
# # 1 - აიყვანე იქსი იგრეკის ხარისხში, 2 - იგრეკი იქსის ხარისხში, 3- გაყავი პირველი მიღებული მნიშვნელობა მეორეზე და გაიგე მნიშვნელბა, ხოლო პირქით გაყოფისას გაიგე ნაშთები,
# # 4 -  დააჯამე ხარისხში აყვანილი რიცხვები და გამოიტანე მანიშნელებელი მესიჯი 5 - დააჯამე გაყოფისას მიღებული რიცხვები და გამოიტანე მანიშნელებელი მესიჯი
# # 6 -  მოიფიქრე შენთვის სასურველი მათემატიკური ოპერაცია და შეასრულე მიღებული შედეგებით.
x=int(input("sheiyvane 1 ricxvi : "))
y=int(input("sheiyvane meore ricxvi : "))
print(f"iksi igreksis xarisxsia {x**y}")
print(f"igrekis xarisxsia {x**y}")
print(f"{x**y/(y**x)} esaa jamebi ro gavkot")
print(f"xarisxebis jamia {x**y+x**y}")
print(f"gayopis jamia {x/y+y/x}")
print(f"{x+y} jamia es ")
# #3. დაწერეთ პროგრამა, რომელიც მომხმარებელს მისი სახელის და ასაკის შეტანას მოსთხოვს.
# # შემდეგ გაზრდის მომხარებლის ასაკს 1-ით და გამოიტანს მესიჯს „ მომხ.სახელი next birthday you will be ახალი ასაკი“ .
asaki=int(input("sheiyvane seni asaki : "))
print(f"next birthday you wil be {asaki+1}years old")
#4. დაწერეთ პროგრამა, რომელიც შეატანინებს მომხარებელს დღეების რაოდენობას,
# ხოლო შემდეგ პროგრამა გადააქცევს დღეების რაოდენობას, საათებში, წუთებში და წამებში, გამოიტანი მათი შედეგები.
day=int(input("sheiyvane dgeebis raodenoba : "))
print(f"sen mier agebuli dgeebi saatebsia: {day*24}. dgeebis raodeneba wutebsi :{day*24*60}. dgeebis raodenoba wamebsi {day*3600}")
#5. შესთავაზეთ მომხმარებელს, შეიყვანოს 2 რიცხვი. თუ პირველი მეტი იქნება მეორეზე, 
# გამოიტანეთ ჯერ მეორე რიცხვი, სხვა შემთხვევაში პირველი.
cvladi1=int(input("sheiyvane pirveli ricxvi : "))
cvladi2=int(input("sheiyvane meore ricxvi : "))
if cvladi1>cvladi2 :
    print(f"{cvladi1,cvladi2}anu pirveli ricxvi metia meoreze")
if cvladi2>cvladi1 :
    print(f"{cvladi2,cvladi1}anu meore ricxvi metia pirvelze")
# #6. შეაყვანინეთ მომხმარებელს 20 ზე ნაკლები რიცხვი. თუ რიცხვი აღმოჩნდება 20 ის ტოლი ან 20 ზე მეტი, 
# # გამოიყვანეთ მესიჯათ „Too high” სხვა შემშთხვევაში „Thank you”
k=int(input("seiyvane 20 ze naklebi ricxvi : "))
if k==20 or k>20 :
    print("number is too high")
if k<20 :
    print("thank you")
#7. დაწერე ბულიანის მაგალითი . მინიშნება: დაწერე მინიმუმ  2 შედარება.
f=int(input("sheiyvane nebismieri ricxvi : "))
l=int(input("sheiyvane kide erti ricxvi : "))
if f>l :
 print(f"{f>l} anu pirveli ricxvi meoreze metia")
if l>f :
 print(f"{l>f} anu meore ricvi metia pirvelze")
#8. დაწერე პროგრამა, რომელშიც გამოიყენებ პირობებს და შეამოწმებ რიცხვებს ნაშტებს და შესაბამისად გამოიტან მესიჯებს.
y=int(input("sheiyvane riccxvi : "))
t=int(input("sheiyvane meore ricxvi : "))
if y%t<2 :
 print(f"nashti tolia {nashti}")
else :
 print(f"nashti 2 ze naklebia")
#9. შესთავაზეთ მომხარებელს შეიყვანოს რიცხვი. თუ რიცხვი ნაკლებია 10 ზე გამოიყვანეთ მესიჯი „Too low” 
# თუ რიცხვი 10 დან 20 მდეა დაწერეთ „Correct” სხვა შემთხვევის დროს „Too high”.
m=int(input("sheiyvane ricxvi  : "))
if m<10 :
 print("number is too low")
if m==10 or m==11 or m==12 or m==13 or m==14 or m==15 or m==16 or m==17 or m==18 or m==19 or m==20 :
 print("correct")
if m>20 :
 print("too high") 
# 10. დაწერე იდენტურობის ოპერატორის(is, is not)
# და წევრობის ოპერატორის(in, not in) მეშვეობით შენთვის სასურველი პროგრამა.  
saxeli=str(input("input sheiyvane NIKA : "))
if saxeli=="NIka" :
 print("correct")
else : 
 print("ragac segesala")
