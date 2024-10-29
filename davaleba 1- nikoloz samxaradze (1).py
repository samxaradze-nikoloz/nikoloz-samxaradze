# 1.	დაწერეთ კოდი, რომელიც გამოიტანს შემდეგ კითხვას „ What do you call a bear with no teeth?“  
# და პასუხად გამოუტანს „ A gummy bear!” ეცადე, რომ განალაგო ისინი ერთ ხაზზე.
x=str(input(" ask What do you call a bear with no teeth? to get answer :"))
if x==("What do you call a bear with no teeth?") :
  print("gummy bear")
else :
    print("ragac segesala tavidan cade")
# 2.	დაწერე პროგრამა, რომელიც მომხარებელს შეაყვანინებს ორ რიცხვს და შემდეგ შედეგად დაბეჭდავს („Total is :”, შედეგი)
a=int(input("cawere ricxvi sesakrebad : "))
b=int(input("cawere meore ricxvi sesakrebad : "))
print(f"total is : {a+b}")
# 3.	დაწერე პროგრამა, რომელიც მომხმარებელს შეაყვანინებს 3 რიცხვს.
# შეაჯამებთ პირველი 2 რიცხვი და შემდგომ გაამრავლეთ მესამეზე. დაბეჭდეთ შედეგი და პრინტში მიუთითეთ თქვენთვის სასურველი ტექსტი.
n=int(input("seiyvane ricxvi : "))
z=int(input("seiyvane meore ricxvi : "))
y=int(input("seiyvane mesame ricxvi : "))
print(f"jamis namravli tolia {(n+z)*y}")
# 4.	დაწერეთ პროგრამა, რომელიც მომხმარებელს კითხავს რამდენი პიცის ნაჭერი ქონდა და რამდენი შეჭამა. 
# გამოითვალეთ რამდენი ნაჭერი დარჩა და შედეგი თქვენთვის სასურველი ფორმით გამოიტანეთ.
mtelipica=int(input("ramdeni naweri ak picas : "))
naweri=int(input("ramdeni picis naweri sewame : "))
print(f"sen dagrca {mtelipica - naweri} picis naweri ")
# 5.  1 კილოგრამში 2204 ფუნტია. შესთავაზეთ მომხმარებელს შეიყვანოს მისი წონა კილოგრამებში, ცოლო თქვენმა პროგრამამ გადაიყვანოს ის ფუტებში.
wona=int(input("seiyvane seni wona kilogramebsi : "))
print(f"seni wona pundebsia : {wona*2.204}")
# 6. დაწერე მოცემული ბლოკისთვის პროგრამა if, else, elif ის გამოყენებით: ( სურათი განთავსებულია ცალკე)
num1=int(input("input number : "))
if num1<10 :
    print("this number is less then 10")
if num1>10 :
    print("this number is over 10")
if num1==10 :
    print("this number is eaqual to 10")
# 7. შესთავაზეთ მომხმარებელს შეიყვანოს რიცხვები 10 დან 20 ის ჩათვლით. 
# თუ რიცხვი მომხმარებლის მიერ შეყვანილი იქნება, მოცემული დიაპაზონიდან, პროგრამამ დაპრინტოს „Thank you” 
# საწინააღმდეგო შემთხვევაში დაპრინტოს „Incorrect answer”.
number=int(input("seiyvane ricxvi 10 idan 20 amde : "))
if number==10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 :
 print("thank you")
else : 
    print("incorrect answer")

# 8. შეაყვანინეთ მომხმარებელს მისი სახელი, გვარი და ასაკი. თუ ასაკი 18 წელია ან/ და მეტი მაშინ დაბეჭდეთ „(name) cavn vote “,
# თუ 17 ის ტოლია  „ (name, surname) can learn to drive” , 
# თუ 16 მაშინ „ (name) can go Trick-or Treating”.
name=str(input("input your name : "))
surname=str(input("input your surname : "))
age=int(input("input your age : "))
if age>=18 :
    print(f"{name} you can vote")  
else :
    print(f"{name} you cant vote ")
if age==17 :
  print(f"{name},{surname} you can learn to drive")
if age==16 :
  print(f"{name} you can go trick or treating")
# 9. შეაყვანინეთ მომხმარებელს ინფორმაცია ტემპერატურაზე ფარენგეიტებში და მოცემული ფორმულის მეშვეობით C=(F-32)*5/9 გადაიყვანე ცელსიუსში. არ დაგავიწყდეს განსაზღვრო სწორი შესაყვანი რიცხვის ტიპი.
# შემდეგ გამოიყენე and, or , not , ასევე ორზე მეტი პირობის ქონის შესაძლებლობა და დაუბეჭდე რა შემთხვევაში შეიძლება რომ ქონდეს ქოლგა, ა რა შემთხვევაში უნდა ჩაიცვას თბილად ან თხლად. 
# გამოიყენე შენი კრეატიულობა.
temperatura1=int(input("seiyvane temperatura farengeitshi : "))
temperatura2=((temperatura1-32)*5/9)
weather=str(input("how is the weather ex : fine rainy or snowy : "))
print(f"temperatura celsiushi={temperatura2}")
if temperatura2<=15 :
  print("chaicvi tbilad")
else :
  print("chaicvi rogorc ginda")
if weather=="fine" :
 print ("chaicvi rogorc ginda tu tbila")
if weather=="rainy" :
  print("aige colga")
if weather=="snowy" :
  print("tbilad chaicvi da gaerte!")


# 10. შემოაყვაანინე მომხმარებელს რიცხვები და შეამოწმე არიან კენტი თუ ლუწი, და 7 ზე გაყოფის შემთხვევაში რომელს აქვს ნაშთი, 2, 3, 4, 5 . მიფიქრე და დაუბეჭდე შენთვის სასურველი მესიჯები.
ricxvi1=int(input("seiyvane  ricxvi : "))
ricxvi2=int(input("seiyvane  meore ricxvi : "))
if ricxvi1%2==0 :
  print("luwia es ricxvi")
else :
  print("kentia es ricxvi")
if ricxvi1%ricxvi2==2 or 3 or 4 or 5 :
  print(f"nashti aris {ricxvi1%ricxvi2} es jdeba pirobasi sagol anu nashti 1-dan 5 amde")
  