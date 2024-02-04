import time
start_time = time.time()
import nltk


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import json


# Custom labels from Gmail(test client)
custom_labels = ['General', 'Bank', 'Miscellanous', 'University', 'Programming', 'Jobs']



def preprocess(text):
    text = text.lower() # convert all text to lowercase
    text = re.sub(r"\s+", " ", text) # remove long spaces
    text = re.sub(r'<https?://[^>]*>|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "", text)
    tokens = word_tokenize(text) # tokenizing
    tokens = [t for t in tokens if t.isalpha()] # remove non-alphabetic tokens
    stop_words = set(stopwords.words('english')) # stop words that don't add much meaning
    tokens = [t for t in tokens if not t in stop_words] # removing stop words
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(t) for t in tokens] # stemming
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens] # lemmatization
    return ' '.join(tokens)


# load data from msg_json
def get_data():
    data_str = []
    with open("msgs.json", "r") as read_file:
        data = json.load(read_file)
        data_str.extend(data['msg_strs'])
    return data_str
        

# loads data from a file
data_str = get_data()

count = 0
# data_str is a list of strings of emails that need to be classified
for data in data_str:
    result = preprocess(data)
    data_str[count]= result
    count+=1

def update(key, data_str):
    with open("./msgs.json", 'r+') as msg_file:
        data = json.load(msg_file)
        data[key] = data_str
        msg_file.seek(0)
        json.dump(data, msg_file)
        msg_file.truncate()
    print("JSON FILE UPDATED!!!")


update("msg_strs", data_str)

print("\n---Your program took %.2f seconds ---" % (time.time() - start_time))