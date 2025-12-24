import json 
import os

data_directory = 'data'
users_file = os.path.join(data_directory, "users.json")

def chk_data_dir():
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        print('created data folder')

def load_users():
    chk_data_dir()
    if not os.path.exists(users_file):
        return {}
    with open(users_file,'r',encoding='utf-8') as file:
        try:
            users = json.load(file)
            return users
        except:
            print('user file damaged')
            return {}
        
def save_users(users):
    chk_data_dir()
    with open(users_file,'w',encoding='utf-8') as file:
        json.dump(users,file,indent=4)
    print(f'{len(users)} users successfully saved')
