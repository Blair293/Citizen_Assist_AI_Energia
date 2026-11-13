from src.assistente import EnergyAssistant

def main():
    assistant = EnergyAssistant()
    print("=" * 62)
    print(" CITIZEN ASSIST AI – ENERGIA INTELIGENTE EM CASA")
    print("=" * 62)
    print("Pergunte sobre consumo, LED, custos ou energia solar.")
    print("Digite 'analise' para ver a comparação ou 'sair' para encerrar.\n")
    while True:
        question = input("Você: ").strip()
        if question.lower() in {"sair", "fim", "exit"}:
            print("Assistente: Obrigado por utilizar o Citizen Assist AI!")
            break
        if question.lower() in {"analise", "análise", "comparar", "comparação"}:
            print("Assistente:\n" + assistant.comparison_report())
        elif question:
            print("Assistente: " + assistant.answer(question))
        else:
            print("Assistente: Digite uma pergunta para continuar.")

if __name__ == "__main__":
    main()
