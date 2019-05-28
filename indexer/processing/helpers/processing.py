from os.path import realpath, dirname
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer


class Processing:
    def __init__(self):
        # self.path = dirname(dirname(dirname(realpath(__file__)))) + "/data/"
        self.stop_words_slovene = None
        self.init_stop_words()

    def init_stop_words(self):
        """
        Initializes stop words from corpus
        :return:
        """
        self.stop_words_slovene = set(stopwords.words("slovenian")).union(set(
            ["ter", "nov", "novo", "nova", "zato", "še", "zaradi", "a", "ali", "april", "avgust", "b", "bi", "bil",
             "bila", "bile", "bili", "bilo", "biti",
             "blizu", "bo", "bodo", "bojo", "bolj", "bom", "bomo", "boste", "bova", "boš", "brez", "c", "cel", "cela",
             "celi", "celo", "d", "da", "daleč", "dan", "danes", "datum", "december", "deset", "deseta", "deseti",
             "deseto",
             "devet", "deveta", "deveti", "deveto", "do", "dober", "dobra", "dobri", "dobro", "dokler", "dol", "dolg",
             "dolga", "dolgi", "dovolj", "drug", "druga", "drugi", "drugo", "dva", "dve", "e", "eden", "en", "ena",
             "ene",
             "eni", "enkrat", "eno", "etc.", "f", "februar", "g", "g.", "ga", "ga.", "gor", "gospa", "gospod", "h",
             "halo",
             "i", "idr.", "ii", "iii", "in", "iv", "ix", "iz", "j", "januar", "jaz", "je", "ji", "jih", "jim", "jo",
             "julij", "junij", "jutri", "k", "kadarkoli", "kaj", "kajti", "kako", "kakor", "kamor", "kamorkoli", "kar",
             "karkoli", "katerikoli", "kdaj", "kdo", "kdorkoli", "ker", "ki", "kje", "kjer", "kjerkoli", "ko", "koder",
             "koderkoli", "koga", "komu", "kot", "kratek", "kratka", "kratke", "kratki", "l", "lahka", "lahke", "lahki",
             "lahko", "le", "lep", "lepa", "lepe", "lepi", "lepo", "leto", "m", "maj", "majhen", "majhna", "majhni",
             "malce", "malo", "manj", "marec", "me", "med", "medtem", "mene", "mesec", "mi", "midva", "midve", "mnogo",
             "moj", "moja", "moje", "mora", "morajo", "moram", "moramo", "morate", "moraš", "morem", "mu", "n", "na",
             "nad",
             "naj", "najina", "najino", "najmanj", "naju", "največ", "nam", "narobe", "nas", "nato", "nazaj", "naš",
             "naša",
             "naše", "ne", "nedavno", "nedelja", "nek", "neka", "nekaj", "nekatere", "nekateri", "nekatero", "nekdo",
             "neke", "nekega", "neki", "nekje", "neko", "nekoga", "nekoč", "ni", "nikamor", "nikdar", "nikjer",
             "nikoli",
             "nič", "nje", "njega", "njegov", "njegova", "njegovo", "njej", "njemu", "njen", "njena", "njeno", "nji",
             "njih", "njihov", "njihova", "njihovo", "njiju", "njim", "njo", "njun", "njuna", "njuno", "no", "nocoj",
             "november", "npr.", "o", "ob", "oba", "obe", "oboje", "od", "odprt", "odprta", "odprti", "okoli",
             "oktober",
             "on", "onadva", "one", "oni", "onidve", "osem", "osma", "osmi", "osmo", "oz.", "p", "pa", "pet", "peta",
             "petek", "peti", "peto", "po", "pod", "pogosto", "poleg", "poln", "polna", "polni", "polno", "ponavadi",
             "ponedeljek", "ponovno", "potem", "povsod", "pozdravljen", "pozdravljeni", "prav", "prava", "prave",
             "pravi",
             "pravo", "prazen", "prazna", "prazno", "prbl.", "precej", "pred", "prej", "preko", "pri", "pribl.",
             "približno", "primer", "pripravljen", "pripravljena", "pripravljeni", "proti", "prva", "prvi", "prvo", "r",
             "ravno", "redko", "res", "reč", "s", "saj", "sam", "sama", "same", "sami", "samo", "se", "sebe", "sebi",
             "sedaj", "sedem", "sedma", "sedmi", "sedmo", "sem", "september", "seveda", "si", "sicer", "skoraj",
             "skozi",
             "slab", "smo", "so", "sobota", "spet", "sreda", "srednja", "srednji", "sta", "ste", "stran", "stvar",
             "sva",
             "t", "ta", "tak", "taka", "take", "taki", "tako", "takoj", "tam", "te", "tebe", "tebi", "tega", "težak",
             "težka", "težki", "težko", "ti", "tista", "tiste", "tisti", "tisto", "tj.", "tja", "to", "toda", "torek",
             "tretja", "tretje", "tretji", "tri", "tu", "tudi", "tukaj", "tvoj", "tvoja", "tvoje", "u", "v", "vaju",
             "vam",
             "vas", "vaš", "vaša", "vaše", "ve", "vedno", "velik", "velika", "veliki", "veliko", "vendar", "ves", "več",
             "vi", "vidva", "vii", "viii", "visok", "visoka", "visoke", "visoki", "vsa", "vsaj", "vsak", "vsaka",
             "vsakdo",
             "vsake", "vsaki", "vsakomur", "vse", "vsega", "vsi", "vso", "včasih", "včeraj", "x", "z", "za", "zadaj",
             "zadnji", "zakaj", "zaprta", "zaprti", "zaprto", "zdaj", "zelo", "zunaj", "č", "če", "često", "četrta",
             "četrtek", "četrti", "četrto", "čez", "čigav", "š", "šest", "šesta", "šesti", "šesto", "štiri", "ž", "že",
             "svoj", "jesti", "imeti", "\u0161e", "iti", "kak", "www", "km", "eur", "pač", "del", "kljub", "šele",
             "prek",
             "preko", "znova", "morda", "kateri", "katero", "katera", "ampak", "lahek", "lahka", "lahko", "morati",
             "torej"]))

    def open_web_page(self, file_path):
        """
        This method opens html file and returns its content
        :param file_path: file path
        :return: file content
        """
        with open(file_path, encoding="utf8") as f:
            return f.read()

    def get_text_from_web_page(self, file_path):
        """
        This method extracts text from html file
        :param file_path: path to file
        :return: text content as single line string
        """
        # get file content
        html_doc = self.open_web_page(file_path)
        # init bs4 with html parser
        soup = BeautifulSoup(html_doc, 'html.parser')
        # html_content = soup.get_text()
        # html_content = ' '.join(html_content.split())
        # print(html_content)
        # remove all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()  # rip it out
        # extract text content from HTML file
        html_content = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in html_content.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # remove multiple white spaces and new lines, join into one line
        html_content = ' '.join(chunk for chunk in chunks if chunk)
        # clean text
        # html_content = re.sub('\W+', '', html_content)
        # print(html_content)
        return html_content

    def process_text(self, text):
        """
        This method takes html content and preprocesses text
        :param text: html content
        :return: word tokens
        """
        # text to lowercase
        text = text.lower()
        # print(text)

        # perform text lemmatization
        # check if this actually helps - we decided not to use it
        # lemmatizer = WordNetLemmatizer()
        # text = lemmatizer.lemmatize(text)

        # tokenize text
        # word_tokens = word_tokenize(text)
        # If we get strange results from queries uncomment line above and remove lines bellow
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(text)

        # remove stop words
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words_slovene]
        # print(filtered_sentence)

        return filtered_sentence


if __name__ == "__main__":
    print("running processing module\n")
    p = Processing()
    print("Extracting text")
    content = p.get_text_from_web_page("../../data/evem.gov.si/evem.gov.si.1.html")
    print("Processing tekst")
    result = p.process_text(content)
    print(result)
