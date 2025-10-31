# EnergIA 2.0 - Automação e Monitoramento Inteligente de Energia

## Visão Geral
O EnergIA 2.0 é um sistema de automação residencial desenvolvido em Python, com interface em Streamlit e backend em Flask.  
O projeto permite monitorar, controlar e otimizar o consumo de energia de uma casa em tempo real.  
A aplicação integra comandos de voz, atualização automática do status de consumo e alertas de alto gasto energético.

## Funcionalidades
- Controle individual de cômodos: ligar e desligar luzes ou equipamentos de cada ambiente.
- Monitoramento da bateria: cálculo dinâmico do consumo e nível de energia restante.
- Assistente de voz integrada com SpeechRecognition e pyttsx3.
- Alerta automático de alto consumo quando todos os cômodos estão ligados.
- Interface Streamlit com atualização em tempo real.

## Tecnologias Utilizadas
- Python 3.10+
- Flask
- Streamlit 1.30.0
- SpeechRecognition
- pyttsx3
- Requests
git clone https://github.com/SEU_USUARIO/EnergIA2.0.git
cd EnergIA2.0

## Comandos de Voz Disponíveis

Tipo | Exemplo de Comando | Ação
-----|--------------------|------
Ligar cômodo | "Ligar cozinha" | Liga o cômodo especificado
Desligar cômodo | "Desligar quarto" | Desliga o cômodo especificado
Ligar todos | "Ligar tudo" | Liga todos os cômodos
Desligar todos | "Desligar tudo" | Desliga todos os cômodos
Status geral | "Status da casa" | Informa o nível da bateria e os cômodos ligados
Encerrar | "Encerrar programa" | Encerra o assistente de voz

## Exemplo de Alerta
"Atenção! Todos os cômodos estão ligados. O consumo está muito alto.  
Considere desligar algum aparelho para economizar energia."

## Possíveis Melhorias Futuras
- Integração com sensores físicos (Arduino/ESP32)
- Dashboard com histórico de consumo
- Controle via aplicativo mobile
- Reconhecimento de voz offline (sem uso da API do Google)

## Video no YouTube: https://www.youtube.com/watch?v=HfQVeb4lwtg

## Créditos
Pedro Henrique Lisboa – RM: 565722
Pedro Henrique dos Santos Cardoso - RM: 563268
Gabriel Gibin Leoncio – RM: 565462
Rafael do Nascimento Silva – RM: 566263
Rai Augusto Ribeiro – RM: 562870
