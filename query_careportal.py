import requests
import redis

class UnexpectedDataFormat(Exception):
	pass

class DataSource():
	def __init__(self):
		self._r = redis.Redis(host='localhost', port=6379, db=0)

	def get_test_text_blob(self):
		return """
	Single mother, age 25, is in need of a mattress for her 6 year old daughter. Mother has sheets, pillows and a frame for a queen size bed however she had to get rid of the mattress and cannot financially afford a new mattress. The 6 year old daughter has her own room but has to sleep on the couch, with her brother or with her mother every night.
	Children:  6 year old female, 4 year old male
		"""
	def _query_cp(self, case_id):
		if not isinstance(id, int):
			raise UnexpectedDataFormat("id must be an int")

		print("woah, acuatlly querying: {}".format(case_id))
		return "queried {}".format(case_id)
		r = requests.get('https://system.careportal.org/api/map/request-details?id={case_id}'.format(case_id=case_id))
		
		return r.json()

	def get_case_desc(self, case_json):
		dsc_key = 'case_description'
		if dsc_key not in case_json.keys():
			raise UnexpectedDataFormat('No case case_description found.')
		return case_json[dsc_key]

	def get_case_by_id(self, id):
		if not isinstance(id, int):
			raise UnexpectedDataFormat("id must be an int")
		v = self._r.get(id)
		if v:
			return v
		fresh = self._query_cp(id)
		self._r.set(id, fresh)

	def ListAllCases(self):
		print('listing all cases')
		for i in range(2):
			print('\tlisting case '+str(i))
			yield self.get_case_by_id(i)
	def shutdown(self):
		self._r.shutdown(save=True)

r = redis.Redis(host='localhost', port=16379, db=0)
r.set('a','b')
r.set('b','c')
print(r.get('a'))