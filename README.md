# Quran whole database

Requested by Massih

## Desired output

Here are the desired columns based on .data/desired-format.csv:

1. surah id
2. ayah id
3. surah name ar
4. surah name en
5. surah name transliteration
6. ayah count
7. ayah uthmani
8. ayah indopak
9. ayah en
10. ayah transliteration
11. word count
12. letter count

## Original Data

1. .data/uthmani.json extracted from https://qul.tarteel.ai/resources/quran-script/56 :

   1. surah
   2. ayah
   3. word index
   4. word in uthmani transcript
2. https://huggingface.co/datasets/Buraaq/quran-md-ayahs :

   1. surah id
   2. ayah id
   3. surah name ar
   4. surah name en
   5. surah name transliteration
   6. ayah ar (uthmani)
   7. ayah count
   8. ayah en
   9. ayah transliteration
3. ./data/indopak.json :

   1. surah
   2. ayah
   3. indopak transcript
4. ./data/letters-word-count-quran.xlsx : (needs to be processed first)

   1. letter count
   2. word count

## Todo

* [ ] Pretty print all data that we have (except the excel file)
  * [X] indopak.json
  * [ ] transliteration from hugging face
  * [X] uthmani.json
* [ ] process excel file
  * [ ] manually extract csv for (most likely) each surah
  * [ ] turn the csv into one big csv
  * [ ] numcheck:
    * [ ] word and letter count for a few surah
    * [ ] word and letter count for all the quran
  * [ ] pretty print csv through pandas
