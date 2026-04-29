import json

def converter_Txt(caminho_arquivo: str):
    # Iniciamos a lista vazia para evitar erros caso a leitura falhe
    lista_json = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            
            if not conteudo:
                return [] # Retorna lista vazia se o arquivo estiver em branco

            # Remove a última vírgula se ela existir
            if conteudo.endswith(','):
                conteudo = conteudo[:-1]
            
            # Converte para lista JSON
            json_formatado = f"[{conteudo}]"
            lista_json = json.loads(json_formatado)

    except json.JSONDecodeError as e:
        print(f"Erro crítico de sintaxe JSON no arquivo: {e}")
        return [] # Retorna vazio pois os dados estão corrompidos

    # Limpeza dos links (só acontece se a lista_json for preenchida)
    for item in lista_json:
        if "name" in item and "](" in item["name"]:
            item["name"] = item["name"].split('](')[1].replace(')', '')

    return lista_json