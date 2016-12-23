# WikiExtractor_To_the_one_text

Simple extension for Python script that extracts and cleans text from a Wikipedia database dump. 
Most of the codes are from [WikiExtrator](https://github.com/attardi/wikiextractor)

##Installation

`(sudo) python setup.py install`

## Usage

`python WikiExtractor.py Wiki_dump.xml -options`

ex)
`python WikiExtractor.py enwiki-latest-pages-articles.xml -b 500K -o extracted`

For detailed options, see [WikiExtrator](https://github.com/attardi/wikiextractor)

`python To_the_one_text.py Input_directory Name_of_the_single_output_file`
