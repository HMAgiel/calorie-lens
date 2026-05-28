# 🍱 calorie-lens — AI-Powered Food Calorie Detection

> **Detect. Analyze. Understand.** — A real-time food recognition system powered by YOLO26n and GPT-4o, delivering instant calorie insights from images and videos.
Streamlit link: [Streamlit/Caroli-Lens]()

---

## 🌟 Overview

**calorie-lens** is an end-to-end AI pipeline that identifies food items from images or video streams and generates intelligent, context-aware nutritional summaries. Built on a custom-trained YOLO26n object detection model and augmented with GPT-4o-mini's reasoning capabilities, it bridges computer vision and natural language to make nutrition tracking intuitive and accessible.

Whether you're a health-conscious user, a dietitian, or a developer exploring AI in food tech — calorie-lens delivers accurate, beautiful, and human-friendly results.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔍 **Real-Time Food Detection** | Detects multiple food items in a single image simultaneously using a custom YOLO26n model |
| 🎥 **Video Stream Analysis** | Processes uploaded MP4 videos frame-by-frame, tracking the highest-confidence food detection |
| 🤖 **AI Nutritional Summaries** | Integrates GPT-4o-mini to generate context-aware, meal-time-specific calorie breakdowns |
| 🕐 **Time-Aware Insights** | Automatically classifies meals as breakfast, lunch, or dinner based on local time (WIB/UTC+7) |
| 🖥️ **Interactive Web UI** | Clean, responsive Streamlit interface — no technical knowledge required |
| 📦 **Multi-File Upload** | Supports batch image uploads with side-by-side annotated result display |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│              (Image & Video Upload Interface)            │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────▼──────────┐
          │   Detection Engine   │
          │  (YOLO26n – Custom   │
          │   Trained Model)     │
          └──────────┬──────────┘
                     │
         ┌───────────▼───────────┐
         │   GPT-4o-mini (OpenAI) │
         │  Nutritional Summary   │
         │  Generator             │
         └───────────────────────┘
```

### Core Modules

- **`app.py`** — Streamlit application layer; handles UI rendering, file I/O, and orchestrates the detection and summary pipeline
- **`detection.py`** — Core inference logic; runs YOLO predictions on images and videos, draws annotated bounding boxes, and calls GPT for summaries
- **`training.py`** — Custom YOLO training pipeline with advanced augmentation strategies (HSV jitter, mosaic, random erasing, RandAugment)

---

## 🧠 Model & Training

The detection model is a **YOLO26n** variant fine-tuned on a custom Indonesian food dataset, trained with the following configuration:

```python
epochs      = 300
batch       = 22
imgsz       = 640
device      = [0, 1]     # Multi-GPU training
patience    = 50          # Early stopping
```

**Augmentation strategy applied during training:**
- HSV color jitter (`hsv_h=0.4`, `hsv_s=0.6`, `hsv_v=0.5`) for lighting robustness
- Mosaic augmentation (`0.7`) for multi-object scene generalization
- Random erasing (`0.6`) to improve occlusion handling
- RandAugment policy for diverse training-time transformations

> Training logs are persisted to `training_yolo.log` with timestamped entries and human-readable duration reporting.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- CUDA-capable GPU (recommended for inference speed)
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/calorie-lens.git
cd calorie-lens

# Install dependencies
pip install ultralytics streamlit openai opencv-python python-dotenv albumentations

# Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY to the .env file
```

### Running the App

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 📸 Usage

1. **Upload one or more food images** (PNG, JPG, WebP) or an **MP4 video**
2. Click **"Detect the food calories"**
3. View annotated bounding boxes with confidence scores on each detected item
4. Read the AI-generated **nutritional summary** tailored to your meal time

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Object Detection | [Ultralytics YOLO26n](https://github.com/ultralytics/ultralytics.git) |
| Language Model | OpenAI GPT-4o-mini |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Augmentation | Albumentations |
| Environment | python-dotenv |

---

## 📁 Project Structure

```
calorie-lens/
├── src/
│   ├── __init__.py
│   └── detection.py        # YOLO inference + GPT summary logic
├── utils/
│   └── training.py         # Model training script
├── model/
│   └── best_calories.pt    # Custom-trained YOLOv8 weights
├── logs/
│   └── training_yolo.log   # Auto-generated training log
├── runs/                   # YOLO training output (auto-generated)
├── app.py                  # Streamlit UI & app orchestration
├── packages.txt            # Streamlit Cloud system dependencies
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
├── .env                    # API keys (not committed)
└── .gitignore
```
---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---