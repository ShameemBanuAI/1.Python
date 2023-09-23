class multifunctions():
    def subfields():
        lists=('Neural networks','Vision','Robotics','Speech Recognition','Natural language processing')
        print ("Sub-fields in AI are : ")
        for subfields in lists:
            print(subfields)
            
    def eligible():
        gender=input("Enter your gender : ")
        age=int(input("Enter your age : "))
        if(gender=='male'):

            if(age>=21):
                print("Your are eligible for marriage")
                agevar='Your are eligible for marriage'
            else:
                print("Your are not eligible for marriage")
                agevar='Your are not eligible for marriage'
        else:
            if(age>=18):
                print("Your are eligible for marriage")
                agevar='Your are eligible for marriage'
            else:
                print("Your are not eligible for marriage")
                agevar='Your are not eligible for marriage'

                return agevar        
        
        
        
    def triangle():
        length=int(input("Length : "))
        height=int(input("Height : "))
        breath=int(input("Breath : "))
        area=(height*breath)/2
        print("Area Formula : (Height*breath)/2")
        print("Area of trianlge : ",area)
        perimeter=length*breath*height
        print("Perimeter formula :length*breath*height")
        print ("Perimeter of triangle : ",perimeter)
        return perimeter

    def percentage():
        tam=int(input("Enter tamil mark : "))
        eng=int(input("Enter english mark : "))
        mat=int(input("Enter maths mark : "))
        sci=int(input("Enter science mark : "))
        soc=int(input("Enter social mark : "))
        tot=tam+eng+mat+sci+soc
        per=tot/5
        print("Your total marks : ",tot)
        print("Your percentage : ",per)
        return per
    
    def oddeven():
        num=int(input("Enter the number :"))
        if((num%2)==0):
            print(num, " is even")
        else:
            print(num, "is odd")
        return num 
