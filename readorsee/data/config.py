from os.path import dirname, join

ROOT = join(dirname(dirname(__file__)), "..")

PATH_TO_QUESTIONNAIRE = join(ROOT, "data/raw/questionnaire.csv")
PATH_TO_INSTAGRAM_DATA = join(ROOT, "data/external/instagram")
PATH_TO_INTERIM_DATA = join(ROOT, "data/interim")
PATH_TO_PROCESSED_DATA = join(ROOT, "data/processed")
ENV_VARIABLES = join(ROOT, "instagram_access.env")

# ELMO related variables
PATH_TO_EXTERNAL_TWITTER_DATA = join(ROOT,
    "data/external/twitter/tweets_without_hashtag.txt")
PATH_TO_PROCESSED_TO_TRAIN_TWEETS = join(ROOT,
    "data/processed/tweets/train_tweets/")
PATH_TO_PROCESSED_TO_HELDOUT_TWEETS = join(ROOT,
    "data/processed/tweets/heldout_tweets/")
PATH_TO_VOCABULARY_DATA = join(ROOT, "data/processed/tweets/vocabulary.txt")
