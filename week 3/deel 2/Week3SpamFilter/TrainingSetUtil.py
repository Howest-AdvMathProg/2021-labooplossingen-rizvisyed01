import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

# from SpamClassifier import classify

# for reading all the files
from os import listdir
from os.path import isfile, join

# add path to NLTK file
nltk.data.path = ['nltk_data']

# load stopwords
stopwords = set(stopwords.words('english'))

# path training data sets
spam_path = 'data/trainingset/spam/'
easy_ham_path = 'data/trainingset/ham/'


def get_mail_from_file(file_name):
    """
    geef de inhoud van het bestand (e-mail) als één string terug.
    """

    message = ''
    with open(file_name, 'r', encoding="latin-1") as mail_file:

        for line in mail_file:
            # de inhoud van de eigenlijke e-mail start pas na de eerste lege lijn
            if line == '\n':
                # enkel de rest nu verwerken
                for line in mail_file:
                    message += line

    return message


def get_words(message):
    """
    Haal alle unieke woorden uit de e-mail en geef deze als een set terug
    """
    all_words = set(wordpunct_tokenize(message.replace('=\\n', '').lower()))

    # verwijder stopwoorden alsook worden waarvan lengte <=2
    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]

    return msg_words


def make_training_set(path):
    """
    Geef een dictionary terug <woord>: <frequentie>
    """

    # initialisatie
    training_set = {}

    # plaats in een dir alle gevonden e-mail-bestanden uit de doorgegeven map
    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]

    # aantal gevonden bestanden
    total_file_count = len(mails_in_dir)

    # overlopen van de bestanden
    for mail_name in mails_in_dir:

        # message ophalen
        message = get_mail_from_file(path + mail_name)

        # woorden ophalen
        terms = get_words(message)

        # woorden tellen via dictionary
        for term in terms:
            if term in training_set:
                training_set[term] = training_set[term] + 1
            else:
                training_set[term] = 1

    # relatieve frequentie van elk woord berekenen nadat alle files ingelezen zijn
    for term in training_set.keys():
        training_set[term] = float(training_set[term]) / total_file_count

    return training_set




