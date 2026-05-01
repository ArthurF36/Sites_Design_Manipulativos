import os

# ============================================
# CONFIGURAÇÃO DAS APIs
# ============================================
def obter_configuracoes_api():
    key_gemini = "GOOGLE_API_KEY"
    key_openai = "OPENAI_API_KEY"

    api_key_gemini = os.getenv(key_gemini)
    api_key_openai = os.getenv(key_openai)

    if not api_key_gemini:
        raise ValueError(f"ERRO: variável de ambiente '{key_gemini}' não encontrada!")
    elif not api_key_openai:
        raise ValueError(f"ERRO: variável de ambiente '{key_openai}' não encontrada!")

    return {
        "gemini": {
            "endpoint": f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key_gemini}",
            "headers": {},
            "payload_format": "gemini"
        },
        "openai": {
            "endpoint": "https://api.openai.com/v1/chat/completions",
            "headers": {
                "Authorization": f"Bearer {api_key_openai}",
                "Content-Type": "application/json"
            },
            "payload_format": "openai"
        }
    }