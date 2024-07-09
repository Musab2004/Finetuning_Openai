# Video Description to JSON Converter

This repository contains a Streamlit application that converts video descriptions into JSON format using a fine-tuned OpenAI model and the base GPT-3.5 model. The app provides a text area for inputting the video description and generates a JSON dictionary with a specified structure when the "Generate JSON" button is clicked.

## Directory Structure

- `app.py`: The main Streamlit app script.
- `finetuning_notebook.ipynb`: A Jupyter notebook containing the full process for fine-tuning the OpenAI model.
- `datasets`: Directory containing the data used for fine-tuning the model.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI API
- dotenv

## Installation

1. Clone this repository:

   ```bash
   git clone git@github.com:Musab2004/Finetuning_Openai.git
   cd Finetuning_Openai
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Enter your video description in the provided text area and click on "Generate JSON From Fine Tuned Model" or "Generate JSON from Base model" to get the JSON output.

## Fine-Tuning the Model

The fine-tuning process is detailed in the `fine_tuning_openai_example.ipynb`. This notebook includes the steps to prepare the data, train the model, and evaluate the results.

### Data Preparation

This directory contains the dataset used for fine-tuning the model.
