#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path
import sys

print("🔎 Gerando datapackage – Acordos de Cooperação Técnica")

BASE_DIR = Path(".").resolve()
DATA_DIR = BASE_DIR / "data"
OUTPUT = BASE_DIR / "datapackage" / "datapackage.json"

if not DATA_DIR.exists():
    print("❌ Pasta data/ não encontrada")
    sys.exit(1)

csv_files = list(DATA_DIR.glob("acordos_cooperacao_tecnica.csv"))

if not csv_files:
    print("❌ CSV acordos_cooperacao_tecnica.csv não encontrado")
    sys.exit(1)

resources = []

for csv in csv_files:
    resources.append({
        "name": "acordos-cooperacao-tecnica",
        "title": "Acordos de Cooperação Técnica – Base Consolidada",
        "description": (
            "Acordos de cooperação técnica firmados pelos órgãos e entidades "
            "do Governo do Estado de Minas Gerais, sem transferência de recursos financeiros."
        ),
        "path": f"data/{csv.name}",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "profile": "tabular-data-resource",
        "dialect": {
            "delimiter": ",",
            "quoteChar": "\""
        },
        "schema": {
            "fields": [
                {"name": "ano", "type": "string"},
                {"name": "numero_termo", "type": "string"},
                {"name": "numero_sei", "type": "string"},
                {"name": "orgao_acordo", "type": "string"},
                {"name": "parceiro_acordo", "type": "string"},
                {"name": "objeto", "type": "string"},
                {"name": "inicio_vigencia", "type": "date"},
                {"name": "fim_vigencia", "type": "date"},
                {"name": "situacao", "type": "string"},
                {"name": "link_documento", "type": "string"},
                {"name": "numero_documento", "type": "string"}
            ]
        }
    })

datapackage = {
    "profile": "data-package",
    "name": "acordos-cooperacao-tecnica-mg",
    "title": "Acordos de Cooperação Técnica do Governo de Minas Gerais",
    "description": (
        "Base consolidada de acordos de cooperação técnica firmados "
        "pelos órgãos do Governo de Minas Gerais."
    ),
    "licenses": [
        {
            "name": "CC-BY-4.0",
            "path": "https://creativecommons.org/licenses/by/4.0/",
            "title": "Creative Commons Attribution 4.0"
        }
    ],
    "owner_org": "controladoria-geral-do-estado-cge",
    "resources": resources
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

OUTPUT.write_text(
    json.dumps(datapackage, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("✅ datapackage.json gerado com sucesso")
