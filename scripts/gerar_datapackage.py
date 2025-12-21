#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT = Path("datapackage/datapackage.json")

resources = []

print("📂 Procurando arquivos CSV em data/")

for csv in sorted(DATA_DIR.glob("acordos*.csv")):
    print(f"➕ Incluindo recurso: {csv.name}")

    resources.append({
        "name": f"acordos-cooperacao-tecnica",
        "title": "Acordos de Cooperação Técnica",
        "description": (
            "Acordos de cooperação técnica firmados pelos órgãos e entidades
            do Governo do Estado de Minas Gerais, sem transferência de recursos financeiros."
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
                {"name": "inicio_vigencia", "type": "date"},
                {"name": "fim_vigencia", "type": "date"},
                {"name": "situacao", "type": "string"},
                {"name": "link_documento", "type": "string"},
                {"name": "numero_documento", "type": "string"}
            ]
        }
    })

if not resources:
    raise RuntimeError("❌ Nenhum CSV encontrado na pasta data/")

datapackage = {
    "profile": "data-package",
    "name": "acordos-cooperacao-tecnica",
    "title": "Acordos de Cooperação Técnica do Governo de Minas Gerais",
    "owner_org": "controladoria-geral-do-estado-cge",
    "resources": resources
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(
    json.dumps(datapackage, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("✅ datapackage.json gerado com sucesso")
print(f"📦 Total de recursos: {len(resources)}")
