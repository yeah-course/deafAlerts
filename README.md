# deafAlerts
Using google YAMnet to classify sounds, and creating desktop alerts for people hard of hearing


## Instructions for use:

## Installation

### Requirements
- Python 3.13 
- A working microphone (only needed for live input)

### 1. Clone the repository
```bash
git clone https://github.com/yeah-course/deafAlerts.git
cd deafAlerts
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv313
```

Windows:
```bash
.venv313\Scripts\activate
```

macOS / Linux:
```bash
source .venv313/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the YAMNet model
The model is not included in this repo because of its size. Download it from
[TensorFlow Hub](https://tfhub.dev/google/yamnet/1) and extract it into a
folder called `yamnet_model/` in the project root.

## Usage

Classify an audio file (16 kHz mono WAV works best):
```bash
python main2.py
```
currently you have to manually find the part of the source code to enter a sound file 

> Live microphone input is implemented but currently untested due to
> hardware issues. File-based classification works.