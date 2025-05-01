from setuptools import setup, find_packages

setup(
    name="starvector",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "transformers>=4.30.0",
        "tokenizers>=0.13.0",
        "sentencepiece>=0.1.99",
        "accelerate>=0.20.0",
        "pydantic>=2.0.0",
        "Pillow>=9.0.0",
        "numpy<2.0.0",
    ],
)
