from TrainingSetUtil import *


# redenering, de kans op spam is de totale som van de kans
# dat ieder woord voorkomt indien we weten dat het spam is
def classify(training, message, prior=0.5, contole=3.7e-4):
    msg_prob = 1
    for word in get_words(message):
        if word in training:
            msg_prob *= training[word]
        else:
            msg_prob *= contole

    return msg_prob * prior


