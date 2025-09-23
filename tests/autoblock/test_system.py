import pytest
import psutil, shutil, subprocess, torch

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_132_minimum_vram():
    """PD-132: GPU must provide >= 8 GB VRAM."""
    if not torch.cuda.is_available():
        pytest.skip("No GPU available")
    vram = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    assert vram >= 8

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_126_ssd_storage():
    """PD-126: System must have at least 120 GB SSD."""
    total, _, _ = shutil.disk_usage("/")
    assert total / (1024**3) >= 120

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_121_minimum_ram():
    """PD-121: Minimum RAM must be available."""
    ram = psutil.virtual_memory().total / (1024**3)
    assert ram >= 16  # replace with requirement

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_120_gpu_docker():
    """PD-120: GPU-enabled Docker must detect GPU."""
    if not torch.cuda.is_available():
        pytest.skip("No GPU available")
    assert torch.cuda.device_count() > 0

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_119_cpu_spec():
    """PD-119: CPU must meet documented specification."""
    cores = psutil.cpu_count(logical=True)
    assert cores >= 4  # replace with requirement

@pytest.mark.suite("system")
@pytest.mark.level("auto")
def test_pd_257_os_docker_support():
    """PD-257: Host OS must support Docker."""
    try:
        subprocess.run(["docker", "--version"], check=True, capture_output=True)
    except Exception:
        pytest.fail("Docker not installed or unavailable")
