"""
Desafio: Análise de Consumo de Tokens com Mentor de Carreiras
Objetivo: Avaliar o impacto do tamanho do prompt no consumo de tokens (Input, Output e Total).
"""

from google.colab import userdata
from openai import OpenAI

# 1. Inicialização segura do cliente OpenRouter via Secrets do Colab
client = OpenAI(
    base_url="https://openrouter.ai",
    api_key=userdata.get('OPENROUTER_API_KEY')
)

# Definição da persona do sistema (System Prompt)
instrucoes_mentor = (
    "Você é um mentor de carreiras especializado. Ajude o usuário a entender "
    "o mercado de trabalho e os passos necessários para atingir seus objetivos."
)

def executar_teste(descricao_teste, prompt_usuario):
    print(f"\n{"="*10} EXECUTANDO: {descricao_teste} {"="*10}")
    print(f"Prompt enviado: '{prompt_usuario}'\n")
    
    # Chamada da API
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash:free",
        messages=[
            {"role": "system", "content": instrucoes_mentor},
            {"role": "user", "content": prompt_usuario}
        ]
    )
    
    # Captura da resposta de texto
    resposta_texto = response.choices.message.content
    print(f"Resposta do Mentor:\n{resposta_texto}\n")
    
    # Captura das métricas de tokens (Usage)
    tokens_input = response.usage.prompt_tokens
    tokens_output = response.usage.completion_tokens
    tokens_total = response.usage.total_tokens
    
    # Retorna os dados de consumo em um dicionário
    return {
        "input": tokens_input,
        "output": tokens_output,
        "total": tokens_total
    }

# --- TESTE 1: Prompt Curto ---
prompt_curto = "Quero trabalhar com IA."
metricas_curto = executar_teste("Teste 1 - Prompt Curto", prompt_curto)

# --- TESTE 2: Prompt Detalhado ---
prompt_detalhado = (
    "Tenho 25 anos, sou transição de carreira da área de administração e quero trabalhar com Inteligência Artificial. "
    "Tenho interesse específico em Machine Learning, sei um pouco de lógica de programação, mas nunca trabalhei na área de TI. "
    "Quais as tecnologias e soft skills fundamentais que eu deveria focar nos próximos 6 meses para conseguir um estágio?"
)
metricas_longo = executar_teste("Teste 2 - Prompt Detalhado", prompt_detalhado)

# --- COMPARATIVO FINAL DE TOKENS ---
print("\n" + "="*20 + " METRICAS COMPATIVAS DE TOKENS " + "="*20)
print(f"{'Métrica':<18} | {'Prompt Curto':<15} | {'Prompt Detalhado':<15}")
print("-" * 56)
print(f"{'Tokens de Entrada':<18} | {metricas_curto['input']:<15} | {metricas_longo['input']:<15}")
print(f"{'Tokens de Saída':<18} | {metricas_curto['output']:<15} | {metricas_longo['output']:<15}")
print(f"{'Total de Tokens':<18} | {metricas_curto['total']:<15} | {metricas_longo['total']:<15}")
print("=" * 56)

# Conclusão automatizada
if metricas_longo['total'] > metricas_curto['total']:
    print("\nConclusão: O Prompt Detalhado consumiu mais tokens no total.")
    print("Isso ocorre porque o tamanho do input foi maior e prompts mais específicos tendem a gerar respostas mais ricas e longas.")
else:
    print("\nConclusão: O Prompt Curto consumiu mais tokens no total (Incomum - gerou resposta excessivamente longa).")
