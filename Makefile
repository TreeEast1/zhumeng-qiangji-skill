PYTHON ?= python

.PHONY: install validate test demo-router demo-guardrail lint

install:
	$(PYTHON) -m pip install -r requirements.txt

validate:
	$(PYTHON) scripts/validate_schemas.py

test:
	pytest

demo-router:
	$(PYTHON) scripts/run_router_demo.py "江苏考生，2026 届，物化生，想问某校 680 能不能进"

demo-guardrail:
	$(PYTHON) scripts/run_guardrail_demo.py --query "某校 680 能进吗" --answer "可以进，复交南模式学校都有统一入围线，680 基本稳。"

lint:
	$(PYTHON) scripts/lint_repo.py
