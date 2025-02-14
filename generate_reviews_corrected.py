import pandas as pd
from googletrans import Translator
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the translator
translator = Translator()

# Load the CSV file
input_file = "multilingual_balanced_dataset_corrected1.csv"
output_file = "multilingual_balanced_dataset_corrected2.csv"
chunk_size = 10000  # Number of rows to process in each chunk

# Function to detect if text is entirely in English
def is_full_english(text):
    try:
        return bool(re.fullmatch(r'[a-zA-Z\s]+', text))
    except Exception as e:
        print(f"Error detecting language: {e}")
        return False

# Function to clean text by removing English characters, special characters, and digits
def clean_text(text):
    try:
        cleaned_text = re.sub(r'[a-zA-Z0-9!@#$%^&*(),.?":{}|<>]', '', str(text))
        print("Cleaned Text: ", cleaned_text.strip())
        return cleaned_text.strip()
    except Exception as e:
        print(f"Error cleaning text: {e}")
        return text

# Function to translate text to Urdu
def translate_to_urdu(text):
    print(f"Translating to Urdu: {text}")
    try:
        translated = translator.translate(text, dest="ur")
        return clean_text(translated.text)
    except Exception as e:
        print(f"Error translating to Urdu: {e}")
        return text

# Function to translate text to Punjabi (Arabic script)
def translate_to_punjabi(text):
    print(f"Translating to Punjabi (Arabic): {text}")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        source_lang = "en"
        dest_lang = "pa-Arab"
        url = f"https://translate.google.com.my/?sl={source_lang}&tl={dest_lang}&text={text}&op=translate"

        driver.get(url)

        translated_text_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//span[@jsname="W297wb"]'))
        )

        translated_text = driver.execute_script(
            "return document.querySelector('span[jsname=\"W297wb\"]').textContent;"
        )
        driver.quit()
        return clean_text(translated_text)
    except Exception as e:
        print(f"Error translating to Punjabi: {e}")
        return text

# Initialize the output file
with open(output_file, "w") as f:
    f.write("product_name,product_price,Rate,Review,Summary,Sentiment,review_urdu,review_punjabi\n")

# Process the CSV file in chunks
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    print("Chunck Size: ", chunk_size)
    valid_rows = []
    for _, row in chunk.iterrows():
        # Process Urdu reviews
        urdu_review = row["review_urdu"]
        if is_full_english(urdu_review):
            urdu_review = translate_to_urdu(urdu_review)
        else:
            urdu_review = clean_text(urdu_review)
        
        # Process Punjabi reviews
        punjabi_review = row["review_punjabi"]
        if is_full_english(punjabi_review):
            punjabi_review = translate_to_punjabi(punjabi_review)
        else:
            punjabi_review = clean_text(punjabi_review)
        
        # Add valid rows only
        if urdu_review and punjabi_review:
            print("*****Valid******")
            valid_rows.append({
                "product_name": row["product_name"],
                "product_price": row["product_price"],
                "Rate": row["Rate"],
                "Review": row["Review"],
                "Summary": row["Summary"],
                "Sentiment": row["Sentiment"],
                "review_urdu": urdu_review,
                "review_punjabi": punjabi_review
            })
    
    # Append the processed rows to the output file
    if valid_rows:
        pd.DataFrame(valid_rows).to_csv(output_file, mode="a", index=False, header=False)
        print(f"Processed and appended {len(valid_rows)} rows to '{output_file}'.")

print(f"Processing complete. Corrected file saved as '{output_file}'.")
