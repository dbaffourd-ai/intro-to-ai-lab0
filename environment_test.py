import sys
import platform
import os

def verify_environment():
    results = []
    python_version = sys.version.split()[0]
    results.append(f"✅ Python Version: {python_version}")
    results.append(f"✅ OS: {platform.system()} {platform.release()}")

    required_packages = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn'
    }

    for package_name, display_name in required_packages.items():
        try:
            module = __import__(package_name)
            version = getattr(module, '__version__', 'unknown')
            results.append(f"✅ {display_name}: {version}")
        except ImportError:
            results.append(f"❌ {display_name}: NOT INSTALLED")

    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    in_conda = 'CONDA_PREFIX' in os.environ

    if in_venv:
        results.append(f"✅ Virtual Environment: Active ({sys.prefix})")
    elif in_conda:
        results.append(f"✅ Conda Environment: Active ({os.environ['CONDA_PREFIX']})")
    else:
        results.append("⚠️  Virtual Environment: Not active")

    return "\n".join(results)

if __name__ == "__main__":
    print("=" * 50)
    print("LAB 0: ENVIRONMENT VERIFICATION")
    print("=" * 50)
    print(verify_environment())
    print("=" * 50)