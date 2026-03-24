import os
import requests
import json
import pandas as pd
import time

# ============================================
# CONFIGURAÇÃO DA API GEMINI
# ============================================
key = "GOOGLE_API_KEY"
api_key = os.getenv(key)

if not api_key:
    print(f"ERRO: {key} não encontrada!")
    exit(1)

# Usando o modelo estável mais recente
modelo = "gemini-1.5-flash" 
endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"

def obter_html(url):
    try:
        # User-agent para evitar bloqueios simples de bots
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
        return resposta.text
    except Exception as e:
        print(f"   x Erro ao acessar {url}: {e}")
        return None

def analisar_site(url):
    html = obter_html(url)
    
    resultado_padrao = {
        "url": url,
        "manipulative_design": False,
        "patterns_detected": [],
        "security_risks": [],
        "confidence_level": "baixa"
    }

    if not html:
        resultado_padrao["security_risks"] = ["Site inacessível."]
        return resultado_padrao

    # Reduzi o corte do HTML para evitar estouro de tokens se houver muitas URLs
    prompt = f"""
Analise o HTML e responda APENAS com um JSON válido seguindo este padrão:
{{
    "url": "{url}",
    "manipulative_design": boolean,
    "patterns_detected": [{{ "name": "string", "description": "string" }}],
    "security_risks": ["string"],
    "confidence_level": "alta/média/baixa"
}}
HTML: {html[:10000]} 
"""

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(endpoint, json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            texto_json = data["candidates"][0]["content"]["parts"][0]["text"].strip()
            
            # Limpeza de Markdown
            if "```" in texto_json:
                texto_json = texto_json.split("```")[1].replace("json", "").strip()
            
            return json.loads(texto_json)
        else:
            resultado_padrao["security_risks"] = [f"Erro API: {response.status_code}"]
            return resultado_padrao
    except Exception as e:
        resultado_padrao["security_risks"] = [f"Erro no processamento: {str(e)}"]
        return resultado_padrao

# ============================================
# PROCESSAMENTO DO ARQUIVO TXT
# ============================================
if __name__ == "__main__":
    caminho_txt = "urls.txt"  # Certifique-se que este arquivo existe
    lista_resultados = []

    if not os.path.exists(caminho_txt):
        print(f"Arquivo {caminho_txt} não encontrado! Crie o arquivo com uma URL por linha.")
        exit(1)

    with open(caminho_txt, "r") as f:
        # Lê linhas, remove espaços e ignora linhas vazias
        urls = [linha.strip() for linha in f.readlines() if linha.strip()]

    print(f"--- Iniciando análise de {len(urls)} sites ---")

    for i, url in enumerate(urls, 1):
        if not url.startswith("http"):
            print(f"[{i}/{len(urls)}] Pulando URL inválida: {url}")
            continue

        print(f"[{i}/{len(urls)}] Analisando: {url}...")
        dados_analise = analisar_site(url)
        lista_resultados.append(dados_analise)
        
        # Pausa leve para não estourar o limite de requisições por minuto (RPM) da API gratuita
        time.sleep(2) 

    # Salva os resultados
    if lista_resultados:
        df_final = pd.DataFrame(lista_resultados)
        pasta_resultados = "Data_resultados"
        os.makedirs(pasta_resultados, exist_ok=True)

        caminho_arquivo = os.path.join(pasta_resultados, "resultados_bulk.xlsx")
        df_final.to_excel(caminho_arquivo, index=False)
        
        print(f"\n✅ Concluído! Planilha salva em: {caminho_arquivo}")
        print(df_final[["url", "manipulative_design", "confidence_level"]])