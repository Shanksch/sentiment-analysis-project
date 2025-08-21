import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

     text = text.lower()

     text = re.sub(r'<.*?>', '', text)

     text = re.sub(r'[^a-zA-Z\s]', '', text)

     tokens = text.split()

     cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

     return ' '.join(cleaned_tokens)
     