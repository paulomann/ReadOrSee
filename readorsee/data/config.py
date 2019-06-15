from os.path import dirname, join

ROOT = join(dirname(dirname(__file__)), "..")

PATH_TO_QUESTIONNAIRE = join(ROOT, "data/raw/questionnaire.csv")
PATH_TO_INSTAGRAM_DATA = join(ROOT, "data/external/instagram")
PATH_TO_INTERIM_DATA = join(ROOT, "data/interim")
PATH_TO_PROCESSED_DATA = join(ROOT, "data/processed")
ENV_VARIABLES = join(ROOT, "instagram_access.env")
PATH_TO_CLFS_OPTIONS = join(ROOT, "models/options.json")

# ELMO related variables
PATH_TO_EXTERNAL_TWITTER_DATA = join(ROOT,
    "data/external/twitter/tweets_without_hashtag.txt")
PATH_TO_PROCESSED_TO_TRAIN_TWEETS = join(ROOT,
    "data/processed/tweets/train_tweets/")
PATH_TO_PROCESSED_TO_HELDOUT_TWEETS = join(ROOT,
    "data/processed/tweets/heldout_tweets/")
PATH_TO_VOCABULARY_DATA = join(ROOT, "data/processed/tweets/vocabulary.txt")

# Normal elmo:
PATH_TO_ELMO_WEIGHTS = join(ROOT, "models/elmo/elmo_pt_weights.hdf5")
PATH_TO_ELMO_OPTIONS = join(ROOT, "models/elmo/elmo_pt_options.json")
PATH_TO_ELMO_FC_WEIGHTS = join(ROOT, 
    "models/elmo/fc_weights/elmo_fc_weights_{}_{}days.hdf5")
    
# Fine tuned elmo:
PATH_TO_FT_ELMO_WEIGHTS = join(ROOT,
    "models/elmo/fine_tuned_elmo/elmo_pt_fine_tuned_weights.hdf5")
PATH_TO_FT_ELMO_OPTIONS = join(ROOT, 
    "models/elmo/fine_tuned_elmo/elmo_pt_fine_tuned_options.json")
PATH_TO_TUNED_ELMO_FC_WEIGHTS = join(ROOT, 
    "models/elmo/fine_tuned_elmo/fc_weights/elmo_fc_weights_{}_{}days.hdf5")

# FastText related variables
PATH_TO_FASTTEXT_PT_EMBEDDINGS = join(ROOT, "models/fasttext/cc.pt.300.bin.gz")
PATH_TO_FASTTEXT_FC_WEIGHTS = join(ROOT, 
    "models/fasttext/fc_weights/fasttext_fc_weights_{}_{}days.hdf5")