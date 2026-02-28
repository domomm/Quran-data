import pandas as pd

df_wl_count_source = pd.read_csv("data/source/quran-word-and-letter-count.csv")

# Filter out rows where 'Verse' is NaN, then rename columns to match chosen naming.
df_wl_count = df_wl_count_source[df_wl_count_source['Verse'].notna()]
column_rename = {
    'SURA': 'surah_id',
    'VERSE': 'ayah_id',
    'WORDS': 'word_count',
    'LETTERS': 'letter_count',
    'Verse': 'verse_sura_id'
}
df_wl_count = df_wl_count.rename(columns=column_rename)
# Remove exception row,verse sura id should have not been written down in this row
df_wl_count = df_wl_count[(df_wl_count['verse_sura_id'] != '84') & (df_wl_count['word_count'] != '285')]
df_wl_count.to_csv("data/out/quran-word-and-letter-count-cleaned.csv", index=False)
