import query_careportal
import classify



def main():
	detector = classify.PII_Detector()
	source = query_careportal.DataSource()
	# print(detector.person_count("Hi I'm Bob, Nancy son", sensitivity=2))

	for case in source.ListAllCases():
		print(case)


	source.shutdown()



if __name__ == "__main__":
	main()
