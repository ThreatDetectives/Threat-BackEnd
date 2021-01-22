from model import NLPModel
import pickle

# create new model object
model = NLPModel()

#import and open pickled model
classifier_path = './finalized_model.pkl'
with open(classifier_path, 'rb') as file:
  model.classifier = pickle.load(file)

# tweets are coming in as a csv with one column called tweet
class PredictSentiment(query):
  def __init__():
    self.query = query
    
  def get(self):
    # TODO : do I need a parser to find the user's query? What form are the tweets coming in?
    
    # TODO : clean tweets first?

    # vectorize the user's query and make a prediction
    vectorized = model.vectorizer_fit_transform_toarray(query)

    threat_detected = model.detector(vectorized) # TODO : the detector method takes in 2 args X_train and y_train(?)

    prediction = model.predict_proba(vectorized)
    # labeling the prediction outcome
    if prediction == 0:
      pred_text = "Hate Speech"
    if prediction == 1:
      pred_text = "Offensive Language"
    if prediction == 2:
      pred_text = "Neither"

    # create JSON object to sent to front-en
    output = {"Classification": pred_text, "Threat Detected": str(round(threat_detected * 100)) + "%"}
    return output
