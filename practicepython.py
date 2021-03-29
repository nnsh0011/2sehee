name="leesehee"
email="deny71545@naver.com"
addr="seoul"

name2="leegeonhee"
email2="deny715455@naver.com"
addr2="Kyunggi"

def print_business_card(name,email,addr): #생성자
    print("-----------------")
    print("Name : ", name)
    print("E-mail : %s" % email)
    print("addr : %s " % addr)
    print("------------------")

print_business_card(name,email,addr) #생성자 호출
print_business_card(name2,email2,addr2) 

class BusinessCard:
    def __init__(self,name,email,addr):
        self.name=name
        self.addr=addr
        self.email=email

BusinessCard(name,email,addr) #클래스 생성 및 호출

class Parent:
    def can_sing(self):
        print("Sing a song")

parent=Parent()
parent.can_sing()