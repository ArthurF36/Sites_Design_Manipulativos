import os
from datetime import datetime

def salvar_resultados(df):
    pasta = r"/workspaces/Sites_Design_Manipulativos/Data/Resultados_Atuais"
    fonte = df['Fonte'].unique()[0]

    os.makedirs(pasta, exist_ok = True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = os.path.join(pasta, f"analise_sites_{fonte}_{timestamp}.xlsx")
    df.to_excel(caminho, index = False, engine = "openpyxl")
    
    print(f"\n📁 Resultados salvos em: {caminho}")