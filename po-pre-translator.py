import requests
import polib
import argparse

# DeepL API key
DEEPL_API_KEY = 'PASTE_YOUR_API_KEY_HERE'
# Language of "msgid" in .po file
SOURCE_LANG = 'EN'
# Language of "msgstr" in .po file
TARGET_LANG = 'DE'

def translate_text(text, target_language=TARGET_LANG):
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': target_language,
        'source_lang': SOURCE_LANG
    }
    response = requests.post(url, data=params)
    result = response.json()

    # Uncomment the following line for debugging purposes
    # print(result)
    
    # Check for 'translations' key
    if 'translations' in result:
        translated_text = result['translations'][0]['text']
        return translated_text
    # ADD ELIF STATEMENTS to inform user if api key is invalid, missing parameter, etc.
    else:
        raise KeyError("The 'translations' key is missing in the API response.")

def translate_po_file(input_file, output_file):
    po = polib.pofile(input_file)
    for entry in po:
        if not entry.msgstr:
            translated_text = translate_text(entry.msgid)
            # Uncomment the following line to hide output of translations
            print(f"{SOURCE_LANG}: {entry.msgid} -> {TARGET_LANG}: {translated_text}")
            entry.msgstr = translated_text
    po.save(output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Translate PO files using the DeepL API.")
    parser.add_argument('-i', '--input', default='messages.po', help="Input PO file (default: messages.po)")
    parser.add_argument('-o', '--output', default='messages_translated.po', help="Output PO file (default: messages_translated.po)")
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output
    
    translate_po_file(input_file, output_file)
