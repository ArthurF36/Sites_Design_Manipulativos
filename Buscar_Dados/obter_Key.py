import os

# ============================================
# CONFIGURAÇÃO DAS APIs
# ============================================
def obter_configuracoes_api():
    api_key_gemini = os.getenv("GOOGLE_API_KEY")
    api_key_openai = os.getenv("OPENAI_API_KEY")

    if not api_key_gemini:
        raise ValueError(f"ERRO: variável de ambiente '{"GOOGLE_API_KEY"}' não encontrada!")
    elif not api_key_openai:
        raise ValueError(f"ERRO: variável de ambiente '{"OPENAI_API_KEY"}' não encontrada!")

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