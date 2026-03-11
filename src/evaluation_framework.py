# Evaluation Framework for Plant Disease Detection

## Overview
This script evaluates the performance of plant disease detection models using various metrics. The evaluation includes confusion matrices, class imbalance analysis, cross-crop generalization, and inference speed benchmarks.

## Comprehensive Metrics

### 1. Confusion Matrices
The confusion matrix provides insight into the classification performance of the model. It helps in understanding true positives, true negatives, false positives, and false negatives.

### 2. Class Imbalance Analysis
Analyzing class imbalance is crucial for understanding the model's behavior on minority and majority classes. It helps to identify if the model is biased towards majority classes.

### 3. Cross-Crop Generalization
Cross-crop generalization evaluates how well the model performs on unseen crops, ensuring that the model can generalize across different plant species.

### 4. Inference Speed Benchmarks
Inference speed benchmarks measure how quickly the model can make predictions. This is particularly important for real-time applications.

## Usage
```bash
python evaluation_framework.py --input <input_data> --model <model_path>
```

## Requirements
- Python 3.x
- Required libraries: numpy, pandas, sklearn, matplotlib

