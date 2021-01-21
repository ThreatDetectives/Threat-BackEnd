from model import NLPModel

# create new model object
model = NLPModel()


class PredictSentiment(query):
    
  def get(self):
    # use parser and find the user's query
    args = parser.parse_args()
    user_query = args["query"]
    
    # TODO : clean data first

    # vectorize the user's query and make a prediction
    uq_vectorized = model.vectorizer_transform(np.array([user_query]))
    prediction = model.predict(uq_vectorized) # TODO : need method in model class for this one - should I just use the classifier method?
    pred_proba = model.predict_proba(uq_vectorized)

    # labeling the prediction outcome
    if prediction == 0:
      pred_text = "Hate Speech"
    if prediction == 1:
      pred_text = "Offensive Language"
    if prediction == 2:
      pred_text = "Neither"

    # round the predict proba value and set to new variable
    confidence = round(pred_proba[0], 3)

    # create JSON object
    output = {"prediction": pred_text, "confidence": confidence}
    return output
