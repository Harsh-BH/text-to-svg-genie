# Text-to-SVG Genie

A machine learning solution for the Kaggle "Text-to-SVG Generation" competition that converts text descriptions into high-quality SVG images.

## 🚀 Overview

Text-to-SVG Genie is an AI system that generates Scalable Vector Graphics (SVG) code from text descriptions. Given a text prompt describing an image, the model generates SVG code that renders the described scene as accurately as possible.

This project was developed for the Kaggle competition aimed at building specialized solutions that outperform general-purpose LLMs in generating image-rendering code, providing greater transparency in the process.

## 📋 Features

- Transform text descriptions into SVG code
- Ensure compliance with competition constraints
- Generate aesthetically pleasing vector images
- Optimize for both visual fidelity and description faithfulness

## 🔧 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/text-to-svg-genie.git
cd text-to-svg-genie
pip install -r requirements.txt
```

## 📦 Dependencies

The project relies on the following key libraries:
- kagglehub - For Kaggle package integration
- numpy/pandas - For data handling
- scipy/scikit-learn - For computational tasks
- PyTorch - For deep learning models
- Matplotlib - For visualization

## 🎯 Competition Constraints

Our model adheres to the following competition requirements:
- Generated SVGs are less than 10,000 bytes
- Only allowlisted SVG elements and attributes are used
- No rasterized image data or external sources
- No CSS style elements
- SVG generation completes within 5 minutes per prompt

## 📊 Evaluation Metrics

The model is optimized for the SVG Image Fidelity Score, which combines:
1. VQA task results using PaliGemma model
2. OCR text detection (with penalties for excess text)
3. CLIP-based Aesthetic Score
4. Final score: harmonic mean of VQA and Aesthetic scores

## 💻 Usage

### Using the Model

```python
# Import the model
from text_to_svg_genie.model import Model

# Initialize the model
model = Model()

# Generate SVG from a text description
text_prompt = "A red apple sitting on a wooden table"
svg_code = model.predict(text_prompt)

# Save the SVG to a file
with open("apple.svg", "w") as f:
    f.write(svg_code)
```

### Testing with Sample Prompts

Run the demo script to test the model with sample prompts:

```bash
python demo.py
```

## 🧠 Technical Approach

Our approach combines:

1. **Text Understanding**: Extracting key visual elements from descriptions
2. **Scene Composition**: Determining optimal layout and element relationships
3. **SVG Generation**: Creating vector elements that best represent the described scene
4. **Constraint Optimization**: Ensuring outputs meet competition requirements

## 📂 Project Structure

```
text-to-svg-genie/
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignore file
├── text_to_svg_genie/     # Main package directory
│   ├── __init__.py        # Package initialization
│   ├── model.py           # Model implementation
│   ├── svg_generator.py   # SVG generation utilities
│   └── utils.py           # Helper functions
├── examples/              # Example SVGs and outputs
├── demo.py                # Demonstration script
└── tests/                 # Test suite
```

## 📈 Performance

Our model aims to:
- Generate accurate representations of described scenes
- Create aesthetically pleasing vector graphics
- Optimize for the competition evaluation metrics
- Complete generation within required time constraints

## 📝 License

[Your chosen license]

## 🔗 Resources

- [Competition Details](https://www.kaggle.com/competitions/text-to-svg-generation)
- [Official Starter Notebook](https://www.kaggle.com/code/kaggle/text-to-svg-starter)
- [SVG Constraints Documentation](https://www.kaggle.com/code/kaggle/svg-constraints)