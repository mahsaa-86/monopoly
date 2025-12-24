import hashlib
import re
from .user import User
from .database import load_users, save_users


def passwd_hashing(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def username_availibility(user_name: str) -> bool:
    users = load_users()
    return user_name in users

def chk_passwd(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"\d", password):     
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\"\\|,.<>\/?]", password):
        return False  
    return True

def signup() -> User | None:
    print("\n signup ")
    while True:
        username = input('enter username: ').strip()
        if not username:
            print('username cant be empty')
            continue
        elif username_availibility(username):
            print('username already exists please choose another!')
            continue
        break
    while True:
        password = input('enter password: ').strip()
        if not password:
            print('password cant be empty!')
            continue
        if not chk_passwd(password=password):
            print("\nPassword is too weak. It must:")
            print("  • Be at least 8 characters long")
            print("  • Contain at least one lowercase letter (a-z)")
            print("  • Contain at least one uppercase letter (A-Z)")
            print("  • Contain at least one number (0-9)")
            print("  • Contain at least one special character (e.g. @, #, $, %, etc.)\n")
            continue

        reenter_passwd = input('enter password again')
        if password != reenter_passwd:
            print('passwords are not equal!')
            continue
        break
    hash_passwd = passwd_hashing(password)
    new_user = User(username=username,password_hash = hash_passwd)
    users = load_users()
    users[username] = {
        'password_hash':hash_passwd,
    }
    save_users(users)
    print('account created successfully! ')
    