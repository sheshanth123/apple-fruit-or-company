from sklearn.feature_extraction import text
from sklearn.naive_bayes import MultinomialNB
  
def predict_text(input_str):
	with open('apple-fruit.txt', encoding="utf8") as fruit:
		fruit_train_file = fruit.readlines()
	with open('apple-computers.txt', encoding="utf8") as company:
		company_train_file = company.readlines()
	vector = text.TfidfVectorizer(min_df = 0, max_df = .2, stop_words = 'english', ngram_range = (1, 2), max_features = 3000)
	matrix = vector.fit_transform(fruit_train_file + company_train_file)
	target_fruit = [0] * len(fruit_train_file)
	target_company = [1] * len(company_train_file)
	target_final = target_fruit + target_company
	classifier = MultinomialNB(alpha = .2, class_prior=[0.5, 0.5]).fit(matrix, target_final)
	label = classifier.predict(vector.transform([input_str]))
	if label == 0:
		return "fruit"
	else:
		return "computer-company"