def get_sftp():
    print("sftp 작업을 실행합니다.")


def regist(name, sex, *args):
    print(f"name: {name}")
    print(f"sex: {sex}")
    print(f"additional arg: {args}")

def regist2(name, sex, *args, **kwargs):
    print(f"name: {name}")
    print(f"sex: {sex}")
    print(f"additional arg: {args}")
    print(f"keyword args: {kwargs}")
    
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    
    if email:
        print(email)
    if phone:
        print(phone)