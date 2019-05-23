# Processing module

## Before you use this module
```
import nltk
nltk.download()
```
New window will open. In this window you can install additional nltk data.
Install stopwords, wordnet and remember the install dir path.
Then copy slovenian file from corpora dir into NLTK_DATA/corpora/stopwords/slovenian

## How it works
This module opens required file, reads its content and performs preprocessing.

### Text extraction from HTML

To extract text from html file we used bs4 library. We set it to parse HTML file. Afterwards we removed all script and style tags so we wont get any in final output.

Afterwards we used library function get_text to extract text from html content.

Extracted text had lots of whitespaces and multiple new lines. Therefore we cleaned extracted text and merge it into single one line string.

### Text preprocessing

This function takes single line string.
First we convert whole content to lowercase.
Afterwards we apply regex tokenizer to tokenize words. We used regex tokenizer so we could remove commas, dots, etc.
Finally we filter word tokens with stopwords. End result is array of words we can use for index.