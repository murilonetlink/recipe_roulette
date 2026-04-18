try:
    from core.env_vars import SUPABASE_URL, SUPABASE_KEY
except ImportError:
    SUPABASE_URL = "ERRO_SEM_URL"
    SUPABASE_KEY = "ERRO_SEM_KEY"
