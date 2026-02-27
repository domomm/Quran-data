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

You can simply get the output files if that is all you need. They can be found in the data/out folder. Here are the output files that you can find along with their short description:

1. quran-md-ayahs-no-audio.csv: processed dataset from Burqaan/quran-md-ayahs from huggingface.
2. quran-md-indopak-joined.csv: joined processed dataset from Burqaan/quran-md-ayahs with indopak arabic text

If you would like to reproduce the outputs, please run the following in order:

1. quran_md_ayahs_process_raw.py
2. join_quran_md_indopak.py

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
4. data/quran_word_and_letter_count.csv. It is the exported csv of data/letters-word-count-quran.xlsx.
5. data/desired-format.csv: Example of desired format

## Python Files (and notebook)

### quran_md_ayahs_process_raw.py

Load Burqaan/quran-md-ayahs from [huggingface](https://huggingface.co/datasets/Buraaq/quran-md-ayahs) through [Datasets](https://huggingface.co/docs/hub/en/datasets-usage). Remove audio related columns and remove duplicates. Outputs resulting data to data/quran-md-ayahs-no-audio.csv.

### join_quran_md_indopak.py

Load data/quran-md-ayahs-no-audio.csv and data/indopak.json, joins them based on ayah and surah number. Remove unnecessary columns and rename columns. Outputs resulting data to data/quran-md-indopak-joined.csv.

### notebook.ipynb

Notebook to do quick analysis on resulting data.

## Todo

* [X] Extract and try print source data that we have (except the excel file)
  * [X] indopak.json
  * [X] quranmd transliteration, uthmani, and other metadata from hugging face
* [ ] process excel file
  * [ ] manually extract csv for (most likely) each surah
  * [ ] numcheck:
    * [ ] word and letter count for a few surah
    * [ ] word and letter count for all the quran
  * [ ] pretty print csv through pandas
* [ ] joins
  * [X] join indopak and quran md
  * [ ] join with letter count and word count
