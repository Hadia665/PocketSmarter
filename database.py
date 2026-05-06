from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv('database.env')
SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY=os.getenv("SUPABASE_KEY")
print("URL:",SUPABASE_URL)
print("KEY:",SUPABASE_KEY)
supabase=create_client(SUPABASE_URL,SUPABASE_KEY)
print("Connected!")
