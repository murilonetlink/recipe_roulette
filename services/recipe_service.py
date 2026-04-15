from core.supabase_client import supabase
import random

def get_random_recipe(category: str = None):
    query = supabase.table('recipes').select('*')
    if category and category != 'qualquer':
        query = query.eq('category', category)
    
    response = query.execute()
    recipes = response.data
    if not recipes:
        return None
    
    # Sorteio (Roleta)
    return random.choice(recipes)

def add_recipe(user_id: str, url: str, category: str):
    response = supabase.table('recipes').insert({
        'user_id': user_id,
        'url': url,
        'category': category
    }).execute()
    return response.data
