import json
import re
import pandas as pd

def converter_Txt(caminho_arquivo: str) -> pd.DataFrame:
    # Iniciamos a lista vazia para evitar erros caso a leitura falhe
    lista_json = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            
            if not conteudo:
                print("Lista vazía")
                return [] # Retorna lista vazia se o arquivo estiver em branco

            # Remove vírgulas e espaços extras no final
            conteudo = conteudo.rstrip(', \n\t')

            # Converte para lista JSON
            json_formatado = f"[{conteudo}]"
            lista_json = json.loads(json_formatado)

    except json.JSONDecodeError as e:
        print(f"Erro crítico de sintaxe JSON no arquivo: {e}")
        return [] # Retorna vazio pois os dados estão corrompidos

    # Limpeza dos links
    for item in lista_json:
        if "name" in item:
            match = re.search(r'\]\((.*?)\)', item["name"])
            if match:
                item["name"] = match.group(1)

    df = pd.DataFrame(lista_json)

    return df