import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

CV_PERFIL = """
Nombre: Gabriel García Santamaria
Puesto actual: Growth Analyst en RappiCard (Abril 2024 - Presente)
Educación: Matemáticas Aplicadas, ITAM (2021-2025)
Habilidades: SQL, Python, R, Excel, Braze (todos avanzados)
Especialidades: Pruebas A/B, inferencia causal, machine learning, riesgo crediticio
Logros: -70% costo de adquisición, -10% morosidad
Industria: Fintech, CDMX
"""

def buscar_chambas():
    print("🔍 Buscando chambas para tu perfil...\n")
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search"
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"""Eres un headhunter experto en fintech mexicano.
                
Con base en este perfil:
{CV_PERFIL}

Busca en internet vacantes ACTUALES (2026) en empresas fintech en México (Nubank, Stori, Konfío, Klar, Aplazo, Clip, etc) 
pero también considera bancos tradicionales con áreas digitales (BBVA, Banorte, Santander).
IMPORTANTE: excluye cualquier vacante que sea 100% presencial, solo remoto o híbrido.

Para cada vacante incluye:
- Empresa y puesto
- Por qué encaja con su perfil
- Sueldo estimado en MXN
- Link directo para aplicar
- 2 tips para destacar en esa empresa específica

Sé específico y práctico."""
            }
        ]
    )
    
    for block in response.content:
        if hasattr(block, "text"):
            print(block.text)

if __name__ == "__main__":
    buscar_chambas()