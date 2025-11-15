# Installation Instructions for Prior-Depth-Anything

## Standard Installation

```bash
uv pip install --no-build-isolation "prior-depth-anything @ git+https://github.com/machenmp/Prior-Depth-Anything.git"
```

## torch_cluster Compatibility Issue

If you encounter errors like `undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb`, you need to install torch_cluster from PyTorch Geometric's wheel repository with a version matching your torch installation.

**For torch 2.2.x with CUDA 12.1:**
```bash
uv pip install torch-cluster -f https://data.pyg.org/whl/torch-2.2.0+cu121.html
```

**For other torch versions**, check the PyTorch Geometric installation page:
https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html

## Key Fix: Missing `__init__.py` in util directory

This fork fixes a packaging bug in the original Prior-Depth-Anything repository where the `prior_depth_anything/depth_anything_v2/util/__init__.py` file was missing, causing `ModuleNotFoundError` during import.

## Integration with mttr-radiance

Add to your `pyproject.toml`:
```toml
dependencies = [
    "prior-depth-anything @ git+https://github.com/machenmp/Prior-Depth-Anything.git",
]
```

Then install with:
```bash
source .venv/bin/activate
uv pip install --no-build-isolation -e .
uv pip install torch-cluster -f https://data.pyg.org/whl/torch-2.2.0+cu121.html
```
