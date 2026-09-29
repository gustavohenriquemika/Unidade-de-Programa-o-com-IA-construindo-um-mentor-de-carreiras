# Desafio OpenRouter: Análise de Consumo de Tokens 📊

Este repositório contém a resolução do desafio prático de monitoramento de tokens consumidos utilizando a API do OpenRouter e o modelo `google/gemini-2.5-flash:free`.

## 🚀 Objetivo do Desafio
O script executa duas requisições idênticas em contexto (mentoria de carreira em IA), mas varia a complexidade e a extensão do prompt enviado pelo usuário para avaliar o impacto direto no faturamento/consumo de tokens (`prompt_tokens`, `completion_tokens` e `total_tokens`).

## 🛠️ Tecnologias Utilizadas
* Python 3
* Biblioteca Oficial `openai`
* Google Colab (Secrets para gerenciamento de chaves)

## 📌 Aprendizados
* Prompts mais descritivos e detalhados aumentam o número de **Tokens de Entrada (Prompt Tokens)**.
* Prompts que contextualizam o cenário do usuário ajudam o modelo a gerar respostas mais assertivas e personalizadas, o que também impacta os **Tokens de Saída (Completion Tokens)**.
