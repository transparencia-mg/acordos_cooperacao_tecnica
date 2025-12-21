#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path
import sys

DATA_DIR = Path("data")
OUTPUT = Path("datapackage/datapackage.json")

if not DATA_DIR.exists():
    print("❌ Pasta 'data/' não encontrada")
    sys.exit(1)

csv_files = sorted(DATA_DIR.glob("acordos_cooperacao_tecnica.csv"))

if not csv_files:
    print("❌ Nenhum arquivo CSV encontrado com padrão:")
    print("   acordos_cooperacao_tecnica*.csv")
    sys.exit(1)

resources = []

for csv in csv_files:
    # tenta extrair ano do nome do arquivo
    partes = csv.stem.split("_")
    ano = partes[-1] if partes[-1].isdigit() else "geral"

    resources.append({
        "name": f"acordos-cooperacao-tecnica-{ano}",
        "title": f"Acordos de Cooperação Técnica – {ano.upper()}",
        "description": (
            "Conjunto de dados de acordos de cooperação técnica que não envolvem "
            "transferência de recursos financeiros, firmados pelos órgãos e entidades "
            "do Governo do Estado de Minas Gerais."
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
                {"name": "natureza_cooperacao", "type": "string"},
                {"name": "inicio_vigencia", "type": "string"},
                {"name": "fim_vigencia", "type": "string"},
                {"name": "situacao", "type": "string"},
                {"name": "link_documento", "type": "string"},
                {"name": "numero_documento", "type": "string"}
            ]
        }
    })

datapackage = {
    "profile": "data-package",
    "name": "acordos-cooperacao-tecnica",
    "title": "Acordos de Cooperação Técnica do Governo de Minas Gerais",
    "description": (
        "Base de dados de acordos de cooperação técnica sem transferência de "
        "recursos financeiros firmados pelos órgãos do Governo de Minas Gerais."
    ),
    "owner_org": "controladoria-geral-do-estado-cge",
    "license": "CC-BY-4.0",
    "resources": resources
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(
    json.dumps(datapackage, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print(f"✔ datapackage.json gerado com {len(resources)} recurso(s)")
