# class telephone:
#     calling= True 
#     def make_calls(self):
#         return "it can make calls "
# class smartmobiles(telephone):
#     internet=True
#     def net_connect(self):
#         return "it can access internet"
# landline=telephone()
# print(landline.calling)
# print(landline.make_calls())
# s25=smartmobiles()
# print(s25.calling)
# print(s25.make_calls())


# class SBI:
#     bank_name="SBI"
#     acc_options= ["cur","sav","joint"]
#     def check_bal(self):
#         return "come after lunch"
#     def application(self):
#         return "go to next counter"
    
# class SBI_kphb(SBI):
#     check_deposit = True
# acc1=SBI()   #this is parent class 
# print(acc1.acc_options)
# print(acc1.check_deposit)   


# acc2=SBI_kphb()
# print(acc2.application())
# print(acc2.check_deposit)  


#-> types of inheritence 

#single ,mulitiple, multilevel,hiereacheil,hybrid 

#single 

# class mechanical:
#     pass
# class quartz(mechanical):
#     pass


# multiple 
# class father:
#     gives_money = True
# class mother:
#     gives_food = True

# class child(father,mother):
#     pass
# c1=child()
# print(c1.gives_food)
  

# class father:
#     gives_money=True
# class mother:
#     gives_food=True
# class child(father,mother):
#     def __init__(self,name):
#         self.name=name 
# child1=child("sagar")
# print(child1.gives_food)
# print(child1.gives_money)


#multilevel 

# class grandfather:
#     prop1="2acres"
# class father(grandfather):
#     prop="3acres"
# class son(father):
#     pass
# s=son()
# print(s.prop1)
# print(s.prop)
        



# class animal:
#     def sound1(self):
#         return "animal makes sound"
# class dog(animal):
#     def sound2(self):
#         return "barks"
# class pamerian(dog):
#     def sound3(self):
#         return "no sound"
    
# p=pamerian()
# print(p.sound1())
# print(p.sound2())
# print(p.sound3())

        
#hierarchey   -> one parent multiple childs 

# class sbi:
#     name ="main"
# class sbi_kphb(sbi):
#     name="branch"
# class sbi_jntu(sbi):
#     name="branch1"
# bank1=sbi()
# print(bank1.name)


#hybrid 
# class computer:
#     pass
# class desktop(computer):
#     pass 
# class laptop(computer):
#     pass
# class tab(laptop):
    

# practicing 

# class animal:
#     alive=True
#     def eat(self):
#         print("animal is eating :")
# class dog(animal):
#     pass
# d1=dog()
# print(d1.alive)
# d1.eat()

# class vehicle:
#     def start(self):
#         print("vehicle is started ")
# class bike(vehicle):
#     pass
# b1=bike()
# print(b1.start())


# it is easy but some what use logics or brain 

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name)
#         print(self.age)
# class student(person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age)
#         self.course=course
#     def student_details(self):
#         self.display()        print("course",self.course)
# s1 = student("Pavan", 21, "AI")
# s1.student_details()

# class bank:
#     bank_name="sbi"
#     def check_bal(self):
#         return "checking balance "
# class savingsaccount(bank):
#     def deposit(self):
#         return "deposited"
# d1=savingsaccount()
# print(d1.check_bal())
# print(d1.deposit)

# class employee:
#     def __init__(self,id,name,):
#         self.id=id
#         self.name=name
#     def show_employee(self):
#         print("id is ", self.id)
#         print("name is ",self.name)
# class developer(employee):
#     def __init__(self, id, name,pgmlang):
#         super().__init__(id, name)
#         self.pgmlang=pgmlang
#     def write_code(self):
#         print("coding language  is",self.pgmlang)

# d1=developer(1,"pavan","python")
# d1.show_employee()
# d1.write_code()

# now its time for (multiple inheritence )

# class father:
#     car="bmw"
# class mother:
#     house="villa"
# class child(father,mother):
#     pass
# c1=child()
# print(c1.car)
# print(c1.house)

# class camera:
#     def take_photo(self):
#         return "clicked a nice shot "
# class musicplayer:
#     def play_music(self):
#         return "started ntr songs "
# class smartphone(camera,musicplayer):
#     def internet(self):
#         return "mobile data is on mode "
# d1=smartphone()
# print(d1.take_photo())
# print(d1.play_music())
# print(d1.internet())

class father:
    bike="royal enifield "
    def ride(self):
        return "father is riding" 
class mother:
    jewellery="gold"
    def cook(self):
        return "mother is cooking"
class child(father,mother):
    pass
f1=child()
print(f1.bike)
print(f1.jewellery)
print(f1.ride())
print(f1.cook())

#multi level 

# class livingthig:
#     def breathe(self):
#         return "all living things can breathe"
# class animal(livingthig):
#     def eat(self):
#         return "animal is eating "
# class dog(animal):
#     def bark(self):
#         return "dog is barking "
# d1=dog()
# print(d1.breathe())
# print(d1.eat())
# print(d1.bark())

