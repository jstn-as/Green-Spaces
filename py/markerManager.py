class MarkerManager:
	geojson_path = "../geojson/markers.geojson"
	json_path = "../json/stats.json"
	events_path = "../json/events.json"

	def add_marker(self, _title, _icon, _lat, _long, _rating, _events):
		# Get the marker data from the geojson file.
		geojson_file = open(self.geojson_path, "r")
		marker_array = geojson_file.read().splitlines()
		geojson_file.close()

		# Get the stat data from the json file.
		json_file = open(self.json_path, "r")
		stat_array = json_file.read().splitlines()
		json_file.close()

		# Add the new marker to the geojson file.
		line_to_add = '{"type": "Feature","geometry": {"type": "Point","coordinates": [%s,%s]},"properties": ' + \
			'{"title": "%s","icon": "%s"}},'
		line_to_add = line_to_add % (str(_lat), str(_long), _title, _icon)
		marker_array.insert(len(marker_array) - 1, line_to_add)

		# Add the stats of the marker to the json file.
		line_to_add = '{"title": "%s","rating": %s, "events": [%s]},'
		line_to_add = line_to_add % (_title, _rating, _events)
		stat_array.insert(len(stat_array) - 1, line_to_add)

		# Check the commas in both arrays.
		marker_array = self.check_commas(marker_array)
		stat_array = self.check_commas(stat_array)

		# Rewrite the geojson file.
		geojson_file = open(self.geojson_path, "w")
		for line in marker_array:
			geojson_file.write(line + "\n")
		geojson_file.close()

		# Rewrite the json file.
		json_file = open(self.json_path, "w")
		for line in stat_array:
			json_file.write(line + "\n")
		json_file.close()

	def remove_marker(self, index):
		# Get the marker data the geojson file.
		geojson_file = open(self.geojson_path, "r")
		marker_array = geojson_file.read().splitlines()
		geojson_file.close()

		# Get the stat data from the json file.
		json_file = open(self.json_path, "r")
		stat_array = json_file.read().splitlines()
		json_file.close()

		# Check the commas in both arrays.
		marker_array = self.check_commas(marker_array)
		stat_array = self.check_commas(stat_array)

		# Rewrite the geojson file ignoring the target index.
		geojson_file = open(self.geojson_path, "w")
		for i in range(len(marker_array)):
			if i != index:
				geojson_file.write(marker_array[i] + "\n")
		geojson_file.close()

		json_file = open(self.geojson_path, "w")
		for i in range(len(stat_array)):
			if i != index:
				json_file.write(marker_array[i] + "\n")
		json_file.close()

	def add_event(self, id, activity, type, date, time, duration):
		events_file = open(self.events_path, "r")
		events_array = events_file.read().splitlines()
		events_file.close()

		event = '{"id": %s, "activity": "%s", "type": "%s", "date": "%s", "time": "%s", "duration": "%s"},'
		event = event % (id, activity, type, date, time, duration)

		events_array.insert(len(events_array) - 1, event)
		events_array = self.check_commas(events_array)

		events_file = open(self.events_path, "w")
		for line in events_array:
			events_file.write(line + "\n")
		events_file.close()

	def get_markers(self):
		geojson_file = open(self.geojson_path, "r")
		return geojson_file.read().splitlines()

	def get_stats(self):
		json_file = open(self.json_path, "r")
		return json_file.read().splitlines()

	def check_commas(self, array):
		for item in range(len(array) - 3):
			if array[item + 1][-1:] == '}':
				array[item + 1] += ","
		if array[len(array) - 2][-1:] == ',':
			array[len(array) - 2] = array[len(array) - 2][:-1]
		return array


# Main code.
markerManager = MarkerManager()
try:
	while True:
		option = int(input("\n~ Choose an option ~\nList: 0\nAdd: 1\nRemove: 2\nEdit: 3\nAdd Event: 4\nQuit: 5\n: "))

		if option == 0:
			print("\n~ Listing the markers ~")
			markers = markerManager.get_markers()
			stats = markerManager.get_stats()
			for i in range(len(markers) - 2):
				print("{0}: {1}".format(i, markers[i + 1]))
				print("   " + stats[i + 1])

		elif option == 1:
			title = str(input("\n~ Adding a marker ~\nName of the location\n: "))
			lat = str(input("Latitude (0.09)\n: "))
			long = str(input("Longitude (52.01)\n: "))
			icon = str(input("Icon\n: "))
			rating = str(input("Rating\n: "))
			events = str(input("Events\n: "))
			markerManager.add_marker(title, icon, lat, long, rating, events)

		elif option == 2:
			print("\n~ Removing a marker ~")
			markers = markerManager.get_markers()
			for i in range(len(markers) - 2):
				print("{0}: {1}".format(i, markers[i + 1]))
			markerToRemove = int(input("Which marker do you want to remove?\n: "))
			markerManager.remove_marker(markerToRemove + 1)

		elif option == 4:
			print("\n~ Adding an event ~")

		elif option == 5:
			quit()
except KeyboardInterrupt:
	quit()
