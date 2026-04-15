import bcrypt
from core.supabase_client import supabase

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def register_user(username: str, password: str):
    hashed = hash_password(password)
    response = supabase.table('users').insert({
        'username': username,
        'password_hash': hashed
    }).execute()
    return response.data

def login(username: str, password: str):
    response = supabase.table('users').select('*').eq('username', username).execute()
    users = response.data
    if len(users) == 0:
        return None
    user = users[0]
    password_hash = user['password_hash']
    if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
        return user
    return None
