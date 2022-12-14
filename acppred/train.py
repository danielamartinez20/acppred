from skelarn.ensemble import RandmForestCLassifier
from acppred.models import Model

def main():

    model = Model(
        estimator=RandomForestClassifier(),
        positive_peptides='data/raw/positive.txt',
        negative_peptides='data/raw/negative.txt'
    )

    model.train()

    model.save('data/models/model.pickle')

if__name__== '__main__':
    main()