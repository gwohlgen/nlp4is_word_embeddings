
"""
    This is the central config file
    @author: Gerhard Wohlgenannt (2017), ITMO University, St.Petersburg, Russia

    Here you can change pathes, add models, add new BOOK_SERIES, new dataset (towards the end of the file).
    But just to start with existing datasets and models, no change is needed
"""


BOOK_SERIES="ASIOF"

MODEL_PATH="../models/"


if BOOK_SERIES == "ASIOF":
    METHODS = [ 
        ('asoif_fastText', 'vec'), # default and: -epoch 25 -ws 12
    ]

# -----------------------------------------------------
# for "doesnt_match" evaluation script
# -----------------------------------------------------

if BOOK_SERIES == "ASIOF":
    PRINT_DETAILS = False ## verbose debugging of eval results

    DOESNT_MATCH_FILE = "../datasets/questions_soiaf_doesnt_match.txt"
    ANALOGIES_FILE = "../datasets/questions_soiaf_analogies.txt"

    ### which sections to show in the paper..
    ANALOGIES_SECTIONS = ['firstname-lastname', 'child-father', 'husband-wife', 'geo-name-location', 'houses-seats', 'total']
    DOESNT_MATCH_SECTIONS = [': family-siblings',  ': names-of-houses', ': archmaesters', ': rivers', ': free cities', 'TOTAL']
