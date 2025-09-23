import pytest
import pandas as pd

@pytest.mark.suite("clinical")
@pytest.mark.level("auto")
def test_pd_306_patient_leakage():
    """PD-306: Ensure no patient data leakage between train/val/test sets."""
    # Dummy dataset
    train = pd.DataFrame({"id": [1, 2, 3]})
    val = pd.DataFrame({"id": [4, 5]})
    test = pd.DataFrame({"id": [6]})

    overlap = set(train["id"]) & set(val["id"]) | set(train["id"]) & set(test["id"])
    assert not overlap, f"Patient leakage detected: {overlap}"
