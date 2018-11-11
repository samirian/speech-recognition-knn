import csv
import random
import math
import operator


class KNN:

	def __init__(self, filename=None):
		self.number_of_features = 15
		self.classes = None
		self.maximum_distance = 30
		self.trainingSet = None
		if filename != None:
			self.filename = filename

	def fit(self, filename=None):
		#takes the file path contatining training set and returns dataset and training set
		if filename == None:
			filename = self.filename

		csvfile = open(filename, newline='')
		lines = csv.reader(csvfile)
		trainingSet = []
		dataset = list(lines)
		n = len(dataset)
		for x in range(n):
			for y in range(self.number_of_features):
				dataset[x][y] = float(dataset[x][y])
			trainingSet.append(dataset[x])

		self.trainingSet = trainingSet
		self.getClasses()
		return self.trainingSet

	def predict(self, test_vector):
		#takes test vector and returns the nearest class
		neighbors = self.getNeighbors(test_vector)
		return self.getResponse(neighbors)

	def getNeighbors(self, test_vector):
		#calculate the distance between the test vector and every vector in the training set
		distances = []
		n = len(self.trainingSet)
		for x in range(n):
			currentTrainingVector_class = self.trainingSet[x][-1]
			currentTraining_vector = self.trainingSet[x][:-1]
			distance = self.euclideanDistance(test_vector, currentTraining_vector)
			distances.append((currentTrainingVector_class, distance))
		return distances
 
	def getResponse(self, neighbors):
		meanDistance = []
		for Class in self.classes:
			mean = 0
			i = 0
			for neighbor in neighbors:
				if neighbor[0] == Class:
					i += 1
					mean += neighbor[1]
			mean = mean/i
			meanDistance.append((Class,mean))
		print(meanDistance)
		nearest_neighbor = 'other'
		nearest_distance = self.maximum_distance
		for distance in meanDistance:
			if distance[1] < nearest_distance:
				nearest_neighbor = distance[0]
				nearest_distance = distance[1]
		return nearest_neighbor

	def getClasses(self):
		self.classes = []
		self.classes.append(self.trainingSet[0][-1])
		j = 0
		for instance in self.trainingSet:
			if self.classes[j] == instance[-1]:
				continue
			else:
				self.classes.append(instance[-1])
				j += 1

	def euclideanDistance(self, X1, X2):
		#X1 and X2 are vectors
		distance = 0
		n = len(X1)
		for i in range(n):
			distance += pow((X1[i] - X2[i]), 2)
		return math.sqrt(distance)

		
def main():
	# prepare data
	knn = KNN('x_train.csv')
	trainingSet= knn.fit()
	test_vector = [ 8.16766976, 30.08112037, 19.74793781, 17.08006437, 16.59073765 ,14.29253129 ,14.02638769 ,12.11092982 ,11.97937172 ,10.42852447, 10.15512419 , 8.71620447 , 7.89137352 , 6.71788546,  6.29216503]
	#test_vector = [  6.76219812,  -5.78551243,  28.31823747,  20.85305022,  24.81655334, 20.93059013,  11.72645347,   4.8889403,   12.74907507,  18.50140694, 22.27399877,   9.57592675, -11.64693939,   1.83020371,  -7.54924958]
	#test_vector = [ 8.16766976, 30.08112037, 19.74793781, 17.08006437, 16.59073765, 14.29253129, 14.02638769, 12.11092982, 11.97937172, 10.42852447, 10.15512419, 8.71620447, 7.89137352, 6.71788546, 6.29216503]
	result = knn.predict(test_vector)
	print(result)

main()