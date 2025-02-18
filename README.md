# Sentiment Analysis Using mBERT for Urdu and English  

## Project Overview  
### Purpose  
This project implements sentiment analysis using mBERT (Multilingual BERT) to classify sentiments in Urdu and English text. The model is fine-tuned to improve accuracy across diverse datasets, addressing challenges in multilingual NLP, particularly for low-resource languages.  

## Features  
- Sentiment classification using mBERT for multilingual text.  
- Fine-tuned model for improved accuracy on Urdu and English datasets.  
- Optimized NLP preprocessing techniques for better text representation.  

## Preprocessing Techniques  
- **Stopword Removal**: Eliminates common words that do not contribute to sentiment.  
- **Tokenization**: Splits text into words or subwords for better input representation.  
- **Lemmatization**: Reduces words to their base forms to handle variations.  
- **Punctuation Removal**: Removes unnecessary symbols to enhance model learning.  
- **Lowercasing**: Converts all text to lowercase for uniform processing.  
- **Urdu Text Preprocessing**: Utilizes `urduhack` for efficient Urdu text processing.  

## Data Collection  
- **Google Translate & Selenium**: Used for scraping and translating sentiment-labeled text for Punjabi and Urdu.  
- **Datasets**: Sentiment-labeled text data in Urdu, English, and Punjabi.  

## Project Structure  
- **Colab Notebooks**: Data preprocessing, model fine-tuning, and evaluation scripts.  
- **Datasets**: Urdu and English sentiment-labeled text data.  
- **Models**: Fine-tuned mBERT checkpoints for inference.  
- **Scripts**: Python scripts for preprocessing, training, and evaluation.  

## Research Questions  
- How does mBERT improve sentiment classification for Urdu and English?  
- What preprocessing techniques enhance model performance in multilingual NLP?  
- How can mBERT be optimized for low-resource languages like Urdu?  

## Acknowledgments  
**Data Sources**: Publicly available sentiment analysis datasets, Google Translate, and web-scraped content using Selenium.  
**Tools**: Python, Transformers (Hugging Face), TensorFlow/PyTorch, Google Colab, Selenium, Urduhack.  
