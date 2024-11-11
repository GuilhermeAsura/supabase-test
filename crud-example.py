#importando as bibliotecas necessárias:
from dotenv import load_dotenv
load_dotenv()

import os
from datetime import datetime, timedelta
from supabase import create_client

#definindo as variáveis de conexão e acesso:
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

#conexão com o DB:
supabase = create_client(url, key)

#chamando os dados selecionados na tabela "forces":
    #data = supabase.table("forces").select("id, Vy").eq("Vy","5").execute()
    #print(data)

#craeted_at = datetime.utcnow() - timedelta(hours=14)

#inserindo dados na tabela "forces" do Db:
    #data = supabase.table("forces").insert({"Vy":"45", "created_at":str(craeted_at)}).execute()

#atualizando dados:
    #data = supabase.table("forces").update({"Vy": "75"}).eq("id", 1).execute()
    #data = supabase.table("forces").update({"Vy": "35"}).eq("id", 2).execute()

#chamando os dados selecionados na tabela "forces":
    #data = supabase.table("forces").select("*").execute()
    #print(data)

#deletando dados da tabela:
data = supabase.table("forces").delete().eq("id", 3).execute()
data = supabase.table("forces").delete().eq("id", 4).execute()