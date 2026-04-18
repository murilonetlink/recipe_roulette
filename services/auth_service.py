import hashlib
from core.supabase_client import supabase

def hash_password(password: str) -> str:
    # A usar a biblioteca nativa do Python. Zero problemas no telemóvel!
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

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
    # A verificação passa a ser uma comparação simples das hashes
    if hash_password(password) == user['password_hash']:
        return user
    return None
