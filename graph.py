import json 


with open("movie_data_n.json" , "r") as data:
	movie_data_info = data.readlines()

	movie_data_list= [] 

	for line in movie_data_info:
		line_json = json.loads(line)
		movie_data_list.append(line_json)

	actor_list = []

	for movie_data in movie_data_list:
		if "Actor" in movie_data.keys():
			for actor_name in movie_data["Actor"]:
				actor_list.append(actor_name)

	actor_network_number = {} 
	actor_network = {}
	actor_network_movie = {}
	for actor in actor_list:
		actor_network_number[f"{actor}"] = 0
		actor_network[f"{actor}"] = []
		actor_network_movie[f"{actor}"] = []
	# print(actor_network_number)


	for actor in actor_network_number.keys() :
		coleage = []
		together = []
		coleage_movie = {}
		for movie_data in movie_data_list:
			if "Actor" in movie_data.keys():
				if actor in movie_data["Actor"]:
					coleage_movie = {}
					actor_network_number[f"{actor}"]+=1
					for actor_name in movie_data["Actor"]:
						coleage_movie[actor_name] =  movie_data["Name"]
						together.append(actor_name)
					coleage.append(coleage_movie)
		actor_network[f"{actor}"] = together
		actor_network_movie[f"{actor}"] = coleage



	graph_matrix = [[0 for i in range(len(actor_list))] for j in range(len(actor_list))]

	for i in range(len(actor_list)):
		for j in range(len(actor_list)):
			graph_matrix[i][j] = actor_network[actor_list[i]].count(actor_list[j])
			if(i==j):
				graph_matrix[i][j] = 0 


		

	#print(movie_data_info)