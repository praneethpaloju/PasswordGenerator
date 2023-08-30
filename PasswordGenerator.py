import random as r
import string as s

def generator(use_nums,use_special_chars,length):
    all_chars=s.ascii_letters
    if(use_nums=="y"):
        all_chars+=s.digits
    if(use_special_chars=="y"):
        all_chars+=s.punctuation
    password="".join(r.choice(all_chars) for _ in range(length))
    return password

def main():
    print("\n\t\tPASSWORD GENERATOR\t\t\n")
    length=int(input("Enter length of password (recommended length is 12):"))
    use_numbers=input("\nDo you want to use digits.?(y/n) ").lower()
    use_special_chars=input("\nDo you want to use special characters.?(y/n) ").lower()
    password=generator(use_numbers,use_special_chars,length)
    print("\nGenerated password:"+password)
if __name__=="__main__":
    main()