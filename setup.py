from setuptools import setup, find_packages

setup(
    name="prior_depth_anything",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'torch>=2.0.0',              # Flexible: compatible with mttr-radiance's torch versions
        'numpy>=1.24.0',             # Flexible: works with numpy 1.25.2+
        'huggingface_hub>=0.26.0',   # Flexible: compatible with transformers requirements
        'einops>=0.6.0',             # Flexible: works with 0.8.1+
        'Pillow>=10.0.0',            # Flexible: works with 11.0.0+
        'torchvision>=0.15.0',       # Flexible: compatible with various torch versions
        'opencv-python>=4.5.0',      # Flexible: works with 4.10.0+
        'torch_cluster',             # No version constraint - use whatever is available
        'safetensors>=0.3.0',        # Flexible: works with 0.4.5+
        'matplotlib>=3.5.0'          # Flexible: works with 3.9.3+
    ],
    entry_points={
        "console_scripts": [
            "priorda = prior_depth_anything.cli:create_and_execute"
        ]
    },
    description="A pytorch implementation of Prior-Depth-Anything",
    author="Zehan Wang, Siyu Chen, Lihe Yang, Jialei Wang, Ziang Zhang, Hengshuang Zhao, Zhou Zhao", 
    author_email="wangzehan01@zju.edu.cn",
    url="https://github.com/SpatialVision/Prior-Depth-Anything"
)