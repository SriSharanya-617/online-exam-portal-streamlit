from supabase import create_client

SUPABASE_URL = "https://ovecsavqqrqfoczvnrun.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92ZWNzYXZxcXJxZm9jenZucnVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkzMjI2ODEsImV4cCI6MjA3NDg5ODY4MX0.HAcGaxW7v__yxwkWhEHCubxNFAf8r0nRY4pudvWc4vo"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
