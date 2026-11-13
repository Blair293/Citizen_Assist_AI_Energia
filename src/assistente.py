from .energia import EnergyScenario, analyze

class EnergyAssistant:
    def __init__(self, scenario=None):
        self.scenario = scenario or EnergyScenario()
        self.results = analyze(self.scenario)

    @staticmethod
    def money(value):
        return ("R$ {:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", "."))

    def comparison_report(self):
        r = self.results
        return (
            "ANÁLISE DO CENÁRIO (estimativas):\n"
            f"- Iluminação antiga: {r['old_kwh']:.2f} kWh/mês ({self.money(r['old_cost'])}).\n"
            f"- Com LED: {r['led_kwh']:.2f} kWh/mês ({self.money(r['led_cost'])}).\n"
            f"- Economia com LED: {r['saved_kwh']:.2f} kWh/mês ou {self.money(r['saved_monthly'])}/mês.\n"
            f"- Investimento em LEDs: {self.money(r['led_investment'])}; retorno simples: {r['led_payback_months']:.1f} meses.\n"
            f"- Geração solar estimada: {r['solar_generation']:.2f} kWh/mês; compensação modelada: {r['solar_offset']:.2f} kWh/mês.\n"
            f"- Valor equivalente: {self.money(r['solar_monthly_value'])}/mês; investimento hipotético: {self.money(r['solar_cost'])}; "
            f"retorno simples: {r['solar_payback_months']:.1f} meses.\n"
            "A compensação solar foi limitada ao consumo de referência. Valores não são garantias."
        )

    def answer(self, question):
        q = question.lower()
        if any(w in q for w in ["led", "lâmpada", "lampada", "iluminação", "iluminacao"]):
            return (f"Trocar {self.scenario.quantity} lâmpadas de {self.scenario.old_lamp_w:g} W por LEDs de "
                    f"{self.scenario.led_lamp_w:g} W reduz o consumo estimado em {self.results['saved_kwh']:.2f} kWh/mês. "
                    "O resultado depende da potência real e do tempo de uso.")
        if any(w in q for w in ["solar", "fotovolta", "renovável", "renovavel", "painel"]):
            return (f"O sistema hipotético de {self.scenario.solar_system_kwp:g} kWp geraria cerca de "
                    f"{self.results['solar_generation']:.2f} kWh/mês nas premissas adotadas. "
                    "A geração real depende da localização, telhado, sombra e clima; solicite avaliação técnica.")
        if any(w in q for w in ["conta", "custo", "preço", "preco", "econom"]):
            return (f"Com tarifa ilustrativa de {self.money(self.scenario.tariff_per_kwh)}/kWh, "
                    f"a economia estimada com LED é {self.money(self.results['saved_monthly'])} por mês. "
                    "Use a tarifa da sua distribuidora para uma estimativa mais realista.")
        if any(w in q for w in ["compar", "análise", "analise", "relatório", "relatorio"]):
            return self.comparison_report()
        return ("Posso ajudar com consumo, LED, custos e energia solar. Pergunte 'Como economizar com LED?' "
                "ou 'Como funciona a energia solar?', ou digite 'analise' para ver a comparação.")
