PYTHON ?= python3

.PHONY: install run demo test clean

install:
	$(PYTHON) -m pip install -e ".[dev]"

run:
	PYTHONPATH=src $(PYTHON) -m founder_ai_workflow_roi.cli run --input data/sample_workflows.csv --company-config config/company_profile.yml --scoring-config config/scoring_rules.yml --output-dir outputs

demo:
	PYTHONPATH=src $(PYTHON) -m founder_ai_workflow_roi.cli demo

test:
	PYTHONPATH=src $(PYTHON) -m pytest

clean:
	rm -f outputs/*.csv outputs/*.md
