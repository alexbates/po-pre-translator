# .po Pre Translator

When creating translation files for your projects, software like POEDIT Pro costs $40/year for access to high quality translations from Google Translate and DeepL.

If all you need is to fill out the "msgstr" entries in a .po file, this script will do what you need for free. It uses the DeepL API, which generously offers 500,000 characters per month at no cost.

## Usage

Create a DeepL API key and add it to the script.
```
python po-pre-translator.py
```
This takes a 'messages.po' input, creates an 'messages_translated.po' output, and outputs progress to console.

Customize input and output:
```
python po-pre-translator.py --input messages.po --output messages_translated.po
```