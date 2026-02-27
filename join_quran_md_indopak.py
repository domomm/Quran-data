import json
import pandas as pd
from tabulate import tabulate

"""
This files joins the indopak.json with the quran-md-ayahs-no-audio.csv
on surah_id and ayah_id, to create a combined dataset with both the metadata
and the indopak text.
"""

# 1. Load indopak, transpose it, print shape and head.

indopak_path = "data/indopak.json"
indopak_df = pd.read_json(indopak_path, encoding="utf-8-sig")
print("source indopak shape:", indopak_df.shape)

# Transposition needed
indopak_transpose = indopak_df.transpose()
print("indopak transpose shape:", indopak_transpose.shape)

print("\nIndopak DataFrame:")
print(tabulate(indopak_transpose.head(), headers='keys', tablefmt='psql'))

# 2. Load quran-md-ayahs-no-audio.csv, join with indopak on surah_id and ayah_id, print shape and head.

quran_md_path = "data/quran-md-ayahs-no-audio.csv"
quran_md_df = pd.read_csv(quran_md_path, encoding="utf-8-sig")
print("source quran-md shape:", quran_md_df.shape)

# Join indopak and quran-md on surah_id and ayah_id
joined_df = pd.merge(quran_md_df, indopak_transpose, left_on=['surah_id', 'ayah_id'], right_on=['surah', 'ayah'], how='inner')

# Rename columns to be more clear, drop redundant columns, print shape and head.
joined_df = joined_df.rename(columns={'text': 'ayah_indopak', 'ayah_ar': 'ayah_uthmani'})
joined_df = joined_df.drop(columns=['surah', 'ayah', 'verse_key', 'id'])
print("joined shape:", joined_df.shape)

print("\nJoined DataFrame:")
print(tabulate(joined_df.head(), headers='keys', tablefmt='psql'))

# 3. Export the joined dataset to a new CSV file.
output_path = "data/quran-md-indopak-joined.csv"
joined_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n✅ Success! Joined data saved to: {output_path}")
