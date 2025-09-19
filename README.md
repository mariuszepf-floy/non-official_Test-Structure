# Testing Repository

This repository contains 78 test cases for our medical product testing.
The structure is organized by Suites (regulatory alignment) and Automation Levels (execution strategy).

Repository Structure
tests/
│
├── smoke/        # 🟩 Smoke & Compliance (43 tests)
│   ├── auto/     # Fully automated security & output checks
│   ├── semi/     # Semi-automated (requires review)
│   └── manual/   # Manual checks (eIFU, CE marking, disclaimers)
│
├── system/       # 🟨 System Validation (16 tests)
│   ├── auto/     # Hardware, runtime, infra checks
│   └── semi/     # Performance & benchmarking
│
├── pipeline/     # 🟦 Data Pipeline (10 tests)
│   ├── auto/     # API basics
│   ├── semi/     # DICOM attributes & encoding
│   └── manual/   # Full end-to-end workflow
│
└── clinical/     # 🟥 Clinical Validation (9 tests)
    ├── auto/     # Patient leakage script
    └── manual/   # Data quality, UAT, clinical purpose

Tagging System

Each test uses pytest markers for suite and automation level:

import pytest

@pytest.mark.suite("smoke")
@pytest.mark.level("auto")
def test_tls_port_open():
    # TODO: implement TLS port check
    assert True

Suites: smoke, system, pipeline, clinical

Levels: auto, semi, manual

Manual tests are skipped automatically but remain in reports for traceability:

@pytest.mark.suite("clinical")
@pytest.mark.level("manual")
@pytest.mark.skip(reason="Manual validation required: UAT with clinicians")
def test_user_acceptance():
    pass

CI/CD Integration

Tests are executed in three GitHub Actions jobs:

🟢 Automation Block → runs all auto tests (~65% of cases)

🟡 Semi-Automation Block → runs semi tests, flagged for review (~25%)

🔴 Manual Block → manual tests are reported as pending (~10%)

Workflow: .github/workflows/tests.yml

Benefits

Maximum automation: majority of tests run fully in CI/CD

Traceability: all Suites & test IDs visible for audits (IEC 62304, IEC 81001-5-1)

Clarity: manual and semi-automated tests are flagged, not hidden

How to Use

Generate test files (already prepared with placeholders):

python generate_tests.py

Run automated tests locally:

pytest -m "level('auto')"

Run semi-automated tests:

pytest -m "level('semi')"

Manual tests remain pending and must be performed according to the QA/Clinical checklist.

Key principle:
Changes trigger Suites → Suites trigger Auto/Semi/Manual tests → CI/CD runs what is automatable.
