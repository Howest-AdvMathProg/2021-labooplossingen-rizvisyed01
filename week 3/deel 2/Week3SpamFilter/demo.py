from TrainingSetUtil import *
from SpamClassifier import *

print('')
print('Loading training sets...')
spam_training_set = make_training_set(spam_path)
ham_training_set = make_training_set(easy_ham_path)
print('done.')
print('')

# toegevoegd
aantal_spam = 0
aantal_ham = 0

spam1_path = 'data/test/spam_1/'
easy_ham1_path = 'data/test/easy_ham_1/'
hard_ham1_path = 'data/test/hard_ham_1/'
hard_ham2_path = 'data/test/hard_ham_2/'

PATHS = [spam1_path, easy_ham1_path, hard_ham1_path, hard_ham2_path]
for path in PATHS:
    print("Running classifier on files in", path)
    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]
    spam_prob = 0.5
    ham_prob = 0.5
    spam_count = 0
    ham_count = 0

    for mail_name in mails_in_dir:
        spam_prob = classify(spam_training_set, get_mail_from_file(path + mail_name), 0.33)
        ham_prob = classify(ham_training_set, get_mail_from_file(path + mail_name), 0.67)

        if spam_prob > ham_prob:
            spam_count += 1
        else:
            ham_count += 1

    print("Fraction of spam messages: ", round(spam_count / len(mails_in_dir), 4) * 100, "percent")
    print("Fraction of ham messages: ", round(ham_count / len(mails_in_dir), 4) * 100, "percent")
    print("------------------------------------------------------------------------------------")