from datasets import load_dataset
import pandas as pd
from tabulate import tabulate

# 1. Load the dataset from your cache
# It won't re-download; it will just link to the .cache folder
print("Loading dataset from cache...")
ds = load_dataset("Buraaq/quran-md-ayahs", split='train')

# --- PHASE 1: RAW DATA STATS ---
print("\n--- PHASE 1: RAW DATA ---")
print(f"Raw Shape: ({len(ds)}, {len(ds.column_names)})")
print(f"Raw Columns: {ds.column_names}")


# --- PHASE 2: CLEANING & SLIMMING ---
cols_to_keep = [
    'surah_id', 'ayah_id', 'surah_name_ar', 'surah_name_en',
    'surah_name_tr', 'ayah_count', 'ayah_en', 'ayah_tr', 'ayah_ar'
]

print("\nCleaning and dropping duplicates...")
# We select only the columns we want. This effectively ignores the audio.
ds_slim = ds.select_columns(cols_to_keep)

# Convert to Pandas to handle the "30 reciters" duplicates easily
df = ds_slim.to_pandas()

# Drop duplicates based on the Surah and Ayah ID
df_unique = df.drop_duplicates(subset=['surah_id', 'ayah_id'])

# --- PHASE 3: CLEAN DATA STATS ---
print("\n--- PHASE 3: CLEANED DATA ---")
print(f"Cleaned Shape: {df_unique.shape}")
print(f"Cleaned Columns: {list(df_unique.columns)}")

print("First 5 Cleaned Rows")
print(tabulate(df_unique.head(5), headers='keys', tablefmt='psql'))


# --- PHASE 4: EXPORT ---
output_file = "data/quran-md-ayahs-no-audio.csv"
df_unique.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n✅ Success! Data saved to: {output_file}")
