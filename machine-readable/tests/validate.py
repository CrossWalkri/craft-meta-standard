#!/usr/bin/env python3
"""Enforce CRAFT's structural obligations. The evaluation-record fixtures validate against
the tree root (dist/craft.schema.json); the receipt fixtures validate against the
InheritanceReceipt companion class. The conformant example of each must validate and every
non-conformant fixture must fail. Run against the GENERATED JSON Schema with a standard
2020-12 validator (not LinkML's own), which is where the conditional obligations (Sections
12.2 and 10) are actually enforced. Exit 0 if all pass, 1 otherwise."""
import json, sys
from pathlib import Path
import yaml, jsonschema

HERE = Path(__file__).resolve().parent.parent
schema = json.loads((HERE / "dist" / "craft.schema.json").read_text())
# A schema that validates a document against one companion class, with the shared $defs
# available for nested references.
receipt_schema = {"$schema": schema.get("$schema"),
                  "allOf": [{"$ref": "#/$defs/InheritanceReceipt"}],
                  "$defs": schema["$defs"]}
ok = True
def check(p, target, should_pass):
    global ok
    try:
        jsonschema.validate(yaml.safe_load(p.read_text()), target)
        if should_pass: print(f"  PASS (valid): {p.name}")
        else: ok = False; print(f"  FAIL (should be invalid): {p.name} validated")
    except jsonschema.ValidationError as e:
        if should_pass: ok = False; print(f"  FAIL (should be valid): {p.name} -> {e.message[:60]}")
        else: print(f"  PASS (correctly rejected): {p.name} -> {e.message[:50]}")

EX = HERE / "examples"
check(EX / "conformant.yaml", schema, True)
for f in sorted(EX.glob("nonconformant-*.yaml")): check(f, schema, False)
check(EX / "receipt-conformant.yaml", receipt_schema, True)
for f in sorted(EX.glob("receipt-nonconformant-*.yaml")): check(f, receipt_schema, False)
sys.exit(0 if ok else 1)
