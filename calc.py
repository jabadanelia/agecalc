from datetime import datetime

byear = int(input("Enter your birthyear: "))
cyear = datetime.now().year


print(cyear - byear)
