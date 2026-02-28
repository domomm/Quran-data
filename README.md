# Quran database

This repository combines multiple data sources of Quran data to obtain a dataset with the following information:

* surah id
* ayah id
* surah name ar
* surah name en
* surah name transliteration
* ayah count
* ayah uthmani
* ayah indopak
* ayah en
* ayah transliteration
* word count
* letter count

## Usage

### Output data

You can simply get the output files if that is all you need. They can be found in the data/out folder. Here are the output files that you can find along with their short description:

1. quran-md-ayahs-no-audio.csv: processed dataset from Burqaan/quran-md-ayahs from huggingface.
2. quran-word-and-letter-count-cleaned.csv: Cleaned version of data/source/quran-word-and-letter-count.csv
3. quran-md-indopak-wl-count.csv: **Final dataset csv**. Joined indopak.json, quran-word-and-letter-count-cleaned.csv, and quran-md-ayahs-no-audio.csv. Data is also cleaned so that unnecessary columns are dropped.

   **Important note**: It is normal that the CSV will not show the arabic content (`ayah_uthmani` and `ayah_indopak`) at the correct column. This is caused by the encoding: the arabic content is encoded so that it is visualized to always start on the right. So, if you open the CSV, the arabic content will always appear at the most right (whereas normally the most right columns are word_count and letter_count). This is also true if you print the table (for example via `print(df.head())` in pandas).

   You can rest assured that if you take the content of the arabic columns, the result will be correct. You can check by running such code:

   ```
   import pandas as pd

   df = pd.read_csv("data/out/quran-md-indopak-wl-count.csv", encoding="utf-8-sig")

   # Print the content of a column of the first row
   print(df.iloc[0]["ayah_uthmani"])
   print(df.iloc[0]["ayah_indopak"])

   ```

### Reproducing output
First, set up a python venv. Run the following in bash:

```
python -m venv .venv
.venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

Please run the following python files in order:

1. quran_md_ayahs_process_raw.py
2. process_word_letter_count.py
3. final_join.py

## Source Data

The source data can be found in data/source. Here is the list of the source data, along with descriptions.

1. https://huggingface.co/datasets/Buraaq/quran-md-ayahs. Contains the following columns:

   1. surah id
   2. ayah id
   3. surah name ar
   4. surah name en
   5. surah name transliteration
   6. ayah ar (uthmani)
   7. ayah count
   8. ayah en
   9. ayah transliteration
2. data/indopak.json. Contain the following columns:

   1. surah
   2. ayah
   3. indopak transcript
3. data/letters-word-count-quran.xlsx. Contain the following information:

   1. letter count per ayah
   2. word count per ayah
4. data/quran-word-and-letter-count.csv. It is the exported csv of data/letters-word-count-quran.xlsx.
5. data/desired-format.csv: Example of desired format

## Python Files (and notebook)

### quran_md_ayahs_process_raw.py

Load Burqaan/quran-md-ayahs from [huggingface](https://huggingface.co/datasets/Buraaq/quran-md-ayahs) through [Datasets](https://huggingface.co/docs/hub/en/datasets-usage). Remove audio related columns and remove duplicates. Outputs resulting data to data/out/quran-md-ayahs-no-audio.csv.

### process_word_letter_count.py

Load data/source/quran-word-and-letter-count.csv. Cleans the source data. Outputs resulting data to data/out/quran-word-and-letter-count-cleaned.csv.

### final_join.py

Load data/out/quran-md-ayahs-no-audio.csv, data/source/indopak.json, data/out/quran-word-and-letter-count-cleaned.csv. The source data is joined them based on ayah and surah number. Remove unnecessary columns and rename columns based on chosen standard. Outputs resulting data to data/out/quran-md-indopak-wl-count.csv.

### notebook.ipynb

Notebook to do quick analysis on resulting data.
