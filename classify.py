import string

from nltk.tag.stanford import StanfordNERTagger

jar = "stanford-ner-2015-04-20/stanford-ner-3.5.2.jar"
model = "stanford-ner-2015-04-20/classifiers/" 


class BadInput(Exception):
	pass

class PII_Detector(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(PII_Detector, self).__init__()
		self.st_3class = StanfordNERTagger(model + "english.all.3class.distsim.crf.ser.gz", jar, encoding='utf8') 
		self.st_4class = StanfordNERTagger(model + "english.conll.4class.distsim.crf.ser.gz", jar, encoding='utf8')
		self.st_7class = StanfordNERTagger(model + "english.muc.7class.distsim.crf.ser.gz", jar, encoding='utf8')

		self.sensitivity = {
			0: self.st_3class,
			1: self.st_4class,
			2: self.st_7class,
		}
	def get_model(self, sens):
		return self.sensitivity.get(sens, self.st_4class)

	def person_count(self, data, sensitivity=1):
		if isinstance(data, str):
			data = data.translate(str.maketrans('', '', string.punctuation)).split()
		if not isinstance(data, list):
			raise BadInput("Need list to process")
		if not isinstance(data[0], str):
			raise BadInput("Need list of strings to process")
			
		print(data)
		results = self.get_model(sensitivity).tag(data)
		return len([word for word, c in results if c == 'PERSON'])

		

