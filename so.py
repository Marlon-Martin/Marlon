from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

resp = supabase.table("nascar_stats").select("*").limit(5).execute()
print(resp.data)
