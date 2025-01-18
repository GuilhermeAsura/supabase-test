#importando as bibliotecas necessárias:
from dotenv import load_dotenv
load_dotenv()

import os
from datetime import datetime, timedelta
from supabase import create_client
from gotrue.exceptions import APIError
#definindo as variáveis de conexão e acesso:
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

#conexão com o DB:
supabase = create_client(url, key)

my_email: str = "you_email"
my_password: str = "your_pswd"
#user = supabase.auth.sign_up({ "email": my_email, "password": my_password })
session = None
try: 
    session = user = supabase.auth.sign_in_with_password({ "email": my_email, "password": my_password })
except APIError:
    print("Falha no Login!")
print(session)

supabase.auth.sign_out()
