# Citizen Assist AI – Energia Inteligente em Casa

Projeto em Python para a Global Solution 2026.2 – Soluções em Energias Renováveis e Sustentáveis.

## Público e problema
Famílias que desejam controlar a conta de luz, mas têm dificuldade para entender o consumo dos equipamentos e comparar alternativas. O projeto aborda a iluminação residencial e apresenta orientações simples, cálculos e uma comparação com fonte renovável.

## Alternativas
- **Eficiência energética:** trocar cinco lâmpadas de 60 W por cinco LEDs de 9 W.
- **Fonte renovável:** estimar a geração de um sistema fotovoltaico hipotético de 0,5 kWp.

As alternativas são comparadas usando o consumo mensal de cinco lâmpadas antigas como referência. Premissas ilustrativas: uso de 5 h/dia por 30 dias, tarifa de R$ 0,90/kWh, LED a R$ 12/unidade, sistema solar instalado a R$ 3.500, 4,5 horas de sol pico/dia e fator de desempenho 0,80. Substitua esses valores por dados locais e orçamentos reais antes de tomar decisões.

## Como executar
Requer Python 3.10 ou superior. Não há dependências externas.

```bash
python main.py
python -m unittest discover -s tests -v
```

Digite `analise` no programa para ver o relatório, ou pergunte sobre LED, conta de luz ou energia solar. Digite `sair` para encerrar.

## Estrutura
- `main.py`: interface de terminal.
- `src/energia.py`: fórmulas e cálculos.
- `src/assistente.py`: respostas do Citizen Assist AI.
- `data/premissas.json`: dados estimados editáveis.
- `tests/test_energia.py`: testes automatizados.
- `docs/`: análise, referências, testes com usuários.

## Integração
A classe `EnergyAssistant` pode ser importada por outro módulo do Citizen Assist AI:

```python
from src.assistente import EnergyAssistant
assistente = EnergyAssistant()
print(assistente.answer("Como economizar energia com iluminação?"))
```

## Limitações
A simulação não representa uma residência específica. Tarifas variam por distribuidora, impostos e bandeiras. A geração solar depende de localização, telhado, inclinação, sombra, clima e perdas. A conta não necessariamente zera após a instalação, pois podem existir custos e regras de compensação. O retorno simples não considera juros, inflação, manutenção, degradação ou financiamento. Não estimamos CO₂ evitado por não adotar fator de emissão específico e verificável para o local e período. Instalações exigem avaliação técnica e orçamento local.

## Referências institucionais
- ANEEL: https://www.gov.br/aneel/pt-br
- EPE – publicações e Balanço Energético Nacional: https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes
- INMETRO – Programa Brasileiro de Etiquetagem: https://www.gov.br/inmetro/pt-br/assuntos/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem
- ABSOLAR: https://www.absolar.org.br/