import pyperclip
import sys
TEXT = {
    'agree' : """Yes, i agree to the terms and i like u""",
    'busy' :"""sorry, i didn't understand'""",
    'upsell' : """Would you consider this decision"""
}

if len(sys.argv) < 2:
    print(TEXT['busy'])
    sys.exit()
keyphrases = sys.argv[1]

if keyphrases in TEXT:
    pyperclip.copy(TEXT[keyphrases])
    print('Text for ' + keyphrases + ' copied to clipboard')
    print(TEXT[keyphrases])
else:
    print('there is no text for' + keyphrases)