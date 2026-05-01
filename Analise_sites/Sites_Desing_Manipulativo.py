import os
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

from Buscar_Dados.obter_Key import obter_configuracoes_api as get_key
from Tratar_dados.Menu import Menu

# ============================================
# UTILITÁRIOS DE HTML E RESPOSTA
# ============================================
def obter_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for s in soup(["script", "style", "meta", "noscript", "link"]):
            s.decompose()
        return str(soup.body)[:20000]
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def limpar_json_resposta(texto):
    # Remove blocos de código markdown se existirem
    texto = texto.replace("```json", "").replace("```", "").strip()
    return texto

# ============================================
# FUNÇÃO DE ANÁLISE (HÍBRIDA)
# ============================================
def analisar_site(url, config_ia):
    html = obter_html(url)
    if not html: return None

    prompt = f"Analise o HTML em busca de Design Manipulativo. URL: {url}\nHTML: {html}\nResponda APENAS um JSON: {{ 'name': '{url}', 'manipulative_design': boolean, 'patterns_detected': 'string', 'security_risks': 'string', 'confidence_level': 'alta' }}"

    # Ajusta o payload dependendo de qual IA você escolheu
    if config_ia["payload_format"] == "gemini":
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.1, "response_mime_type": "application/json"}
        }
    else: # Formato OpenAI
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "response_format": { "type": "json_object" }
        }

    try:
        response = requests.post(
            config_ia["endpoint"], 
            json=payload, 
            headers=config_ia["headers"], 
            timeout=30
        )
        
        if response.status_code == 200:
            res_json = response.json()
            # Extração do texto varia por API
            if config_ia["payload_format"] == "gemini":
                texto = res_json["candidates"][0]["content"]["parts"][0]["text"]
            else:
                texto = res_json["choices"][0]["message"]["content"]
                
            return limpar_json_resposta(texto)
    except Exception as e:
        print(f"Erro na API: {e}")
    return None

def salvar_txt(lista_json_strings, caminho_diretorio, api_name):
    # Garante que as pastas existam (cria se não houver)
    os.makedirs(caminho_diretorio, exist_ok = True)
    
    # Gera o nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"analise_{api_name}_{timestamp}.txt"
    caminho_completo = os.path.join(caminho_diretorio, nome_arquivo)
    
    # Formata como um JSON Array [ {}, {} ]
    conteudo_final = "[\n" + ",\n".join(lista_json_strings) + "\n]"
    
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo_final)
    
    print(f"\n📁 Resultados exportados com sucesso para:\n{caminho_completo}")

# ============================================
# EXECUÇÃO
# ============================================
def main():
    try:
        configs = get_key()
    except ValueError as e:
        print(e)
        return
    
    opcao_Ai, api_name = Menu(configs)
    json_acumulados = []

    while True:
        url = input("\nDigite a URL (ou 'sair' ou 's'): ").strip()

        if url.lower() in ['sair', 's']: break
        if not url.startswith(("http://", "https://")): url = "https://" + url

        print(f"🔍 Analisando com {opcao_Ai['payload_format']}...")
        resultado = analisar_site(url, opcao_Ai)
        
        if resultado:
            json_acumulados.append(resultado)
            print("✅ Sucesso!")
        else:
            print("⚠️ Falha na análise deste site.")

    if json_acumulados:
        caminho_pasta = "/workspaces/Sites_Design_Manipulativos/Data/Resultados_Atuais"
        salvar_txt(json_acumulados, caminho_pasta, api_name)
    else:
        print("\nNenhum dado foi gerado para salvar.")

if __name__ == "__main__":
    main()