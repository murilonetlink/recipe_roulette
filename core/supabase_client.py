from supabase import create_client, Client
from core.config import SUPABASE_URL, SUPABASE_KEY

def get_supabase() -> Client:
    # Retorna o client do supabase instanciado
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = get_supabase()
