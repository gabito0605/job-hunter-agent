# 🔍 Job Hunter Agent

Agente de AI construido con Claude API y web search que analiza un perfil profesional y busca vacantes relevantes en tiempo real.

## ¿Qué hace?
- Toma un perfil profesional como input
- Busca vacantes actuales en internet usando web search
- Filtra por modalidad (excluye 100% presencial)
- Devuelve vacantes rankeadas con links y tips para aplicar

## Tecnologías
- Python
- Anthropic Claude API (claude-sonnet-4-6)
- Web Search tool
- python-dotenv

## Cómo usarlo
1. Clona el repo
2. Crea un archivo `.env` con tu API key: `ANTHROPIC_API_KEY=tu-key`
3. Instala dependencias: `pip install anthropic python-dotenv`
4. Corre: `python agent.py`