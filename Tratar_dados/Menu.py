def Menu(configs):
    print("Bem vindo! Por favor escolha uma das opções abaixo")

    while True:
        print("\n=== SELECIONE O MOTOR DE IA ===")
        print("1 - Gemini 1.5 Flash (Google)")
        print("2 - GPT-4o-Mini (OpenAI)")
        
        entrada = input("\nDigite sua opção (1 ou 2): ").strip()
        
        try:
            # Tenta converter a entrada para número inteiro
            opcao = int(entrada)

            if opcao == 1:
                print("🤖 Modo Gemini ativado.")
                return configs["gemini"], "Gemini"
            elif opcao == 2:
                print("🚀 Modo OpenAI ativado.")
                return configs["openai"], "Openai"
            else:
                # Se for número, mas não for 1 ou 2
                print("❌ Erro: Opção inválida! Escolha apenas 1 ou 2.")
      
        except ValueError:
            # Se o usuário digitar letras, símbolos ou deixar vazio
            print(f"❌ Erro: '{entrada}' não é um número válido. Digite 1 ou 2.")