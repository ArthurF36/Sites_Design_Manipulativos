import json
import re
import pandas as pd

def converter_Txt(caminho_arquivo: str) -> pd.DataFrame:
    lista_json = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            
            if not conteudo:
                print("Lista vazia")
                return pd.DataFrame()  # melhor retornar DataFrame vazio

            conteudo = conteudo.rstrip(', \n\t')
            json_formatado = f"[{conteudo}]"
            lista_json = json.loads(json_formatado)

    except json.JSONDecodeError as e:
        print(f"Erro crítico de sintaxe JSON no arquivo: {e}")
        return pd.DataFrame()

    # Limpeza dos links
    for item in lista_json:
        if "name" in item:
            match = re.search(r'\]\((.*?)\)', str(item["name"]))
            
            if match:
                url = match.group(1)
            else:
                url = item["name"]
            
            # Ajusta protocolo
            item["name"] = ajustar_url(url)

    df = pd.DataFrame(lista_json)
    return df

def ajustar_url(url):
    url = str(url).strip()
    
    if url.startswith("https://"):
        return url
    elif url.startswith("http://"):
        return url.replace("http://", "https://", 1)
    else:
        return "https://" + url