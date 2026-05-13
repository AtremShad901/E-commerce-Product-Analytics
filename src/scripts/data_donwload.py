import sys 
import os 

import gdown 

DATA_BASE_ID      = "1TbFmbWxP9DM30u8U7XvQsnFmZ_ZSs5ZU"
DATA_RAW_ID       = "1-rVgvQ1iwOvL_GPbq87WvgsMu69UCdH1"
DATA_PROCESSED_ID = "1KdUSBpppiShaHmyvGDyZJJUqy8UZwRq_"
def gdoown_donwload(file_id , path , name ):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, f"{path}{name}", quiet=False)

if __name__ == "__main__":
    # Установка Базы данных 
    path_database = "database/"
    name_database = "analytics.db"
    os.makedirs(path_database, exist_ok=True)
    gdoown_donwload(DATA_BASE_ID , path_database ,name_database)

    
    # Установка raw data 
    path_raw = "data/raw/"
    name_raw = "user_events_ecommerce_product_analytics.csv"
    os.makedirs(path_raw, exist_ok=True)
    gdoown_donwload(DATA_RAW_ID , path_raw ,name_raw)
    
    # Установка processed data 
    path_processed  = "data/processed/"
    name_processed =  "clean_data.csv"
    os.makedirs(path_processed, exist_ok=True)    
    gdoown_donwload(DATA_PROCESSED_ID , path_processed ,name_processed)
