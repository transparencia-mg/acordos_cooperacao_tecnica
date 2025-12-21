#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path
import sys

print("🔎 Iniciando geração do datapackage de Acordos de Cooperação Técnica")

BASE_DIR = Path(".").resolve()
DATA_DIR = BASE_DIR / "data"
OUTPUT = BASE_DIR / "datapackage" / "datapackage.json"

print(f"📁 Diretório base: {BASE_DIR}")
print(f"📂 Procurando CSVs em: {DATA_DIR}")

if not DATA_DIR.exists():
    print("❌ ERRO: pasta 'data/' não encontrada")
    sys.exit(1)

csv_files = sorted(DATA_DIR.glob("acordos_cooperacao_tecnica.csv"))

print(f"📄 Arquivos CSV encontrados: {len(csv_files)}")

for f in csv_files:
    print(f"   - {f.name}")

if not csv_files:
    print("❌ ERRO: nenhum arquivo encontrado com padrão 'acordos_cooperacao_tecnica.csv'")
    sys.exit(1)

resources = []

for csv in csv_files:
    print(f"🧩 Processando arquivo: {csv.name}")

    resources.append({
        "name": "acordos-cooperacao-tecnica",
        "title": "Acordos de Cooperação Técnica – Base Consolidada",
        "description": (
            "Conjunto de dados de acordos de cooperação técnica que não envolvem transferência de recursos financeiros, firmados pelos órgãos e entidades do Governo do Estado de Minas Gerais."
        ),
        "path": f"data/{csv.name}",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "profile": "tabular-data-resource",
        "schema": {
            "fields": [
                {"name": "ano", "type": "string"},
                {"name": "numero_termo", "type": "string"},
                {"name": "numero_sei", "type": "string"},
                {"name": "orgao_acordo", "type": "string"},
                {"name": "parceiro_acordo", "type": "string"},
                {"name": "objeto", "type": "string"},
                {"name": "inicio_vigencia", "type": "string"},
                {"name": "fim_vigencia", "type": "string"},
                {"name": "situacao", "type": "string"},
                {"name": "link_documento", "type": "string"},
                {"name": "numero_documento", "type": "string"}
            ]
        }
    })

if not resources:
    print("❌ ERRO: lista de recursos vazia — datapackage não será criado")
    sys.exit(1)

datapackage = {
    "profile": "data-package",
    "name": "acordos-cooperacao-tecnica",
    "title": "Acordos de Cooperação Técnica do Governo de Minas Gerais",
    "description": (
        "Base de dados de acordos de cooperação técnica que não envolvem transferência de recursos financeiros firmados pelos órgãos do Governo de Minas Gerais."
    ),
    "owner_org": "controladoria-geral-do-estado-cge",
    "license": "CC-BY-4.0",
    "resources": resources
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

print(f"💾 Gravando datapackage em: {OUTPUT}")

try:
    OUTPUT.write_text(
        json.dumps(datapackage, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
except Exception as e:
    print("❌ ERRO ao gravar datapackage.json")
    print(e)
    sys.exit(1)

print(f"✅ datapackage.json gerado com sucesso ({len(resources)} recurso(s))")

