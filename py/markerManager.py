class MarkerManager:
	geojson_path = "../geojson/markers.geojson"

	def add_marker(self, title, icon, lat, long):
		# Split the geoJson file into lines.
		geojson_file = open(self.geojson_path, "r")
		marker_array = geojson_file.read().splitlines()
		geojson_file.close()

		line_to_add = '{"type": "Feature","geometry": {"type": "Point","coordinates": [%s,%s]},"properties": ' + \
			'{"title": "%s","icon": "%s"}},'
		line_to_add = line_to_add % (str(lat), str(long), title, icon)
		marker_array.insert(len(marker_array) - 1, line_to_add)

		# Reopen the file for writing.
		geojson_file = open(self.geojson_path, "w")
		for line in marker_array:
			geojson_file.write(line + "\n")
		geojson_file.close()

	def remove_marker(self, index):
		# Get the lines of the geojson file.
		geojson_file = open(self.geojson_path, "r")
		marker_array = geojson_file.read().splitlines()
		geojson_file.close()

		geojson_file = open(self.geojson_path, "w")
		for i in range(len(marker_array)):
			if i != index:
				geojson_file.write(marker_array[i] + "\n")
		geojson_file.close()

	def get_markers(self):
		geojson_file = open(self.geojson_path, "r")
		return geojson_file.read().splitlines()


# Main code.
markerManager = MarkerManager()
try:
	while True:
		option = int(input("\n~ Choose an option ~\nList: 0\nAdd: 1\nRemove: 2\nEdit: 3\nQuit: 4\n: "))

		if option == 0:
			print("\n~ Listing the markers ~")
			markers = markerManager.get_markers()
			for i in range(len(markers) - 2):
				print("{0}: {1}".format(i, markers[i + 1]))

		elif option == 1:
			title = str(input("\n~ Adding a marker ~\nName of the location\n: "))
			lat = str(input("Latitude\n: "))
			long = str(input("Longitude\n: "))
			icon = str(input("Icon\n: "))
			markerManager.add_marker(title, icon, lat, long)

		elif option == 2:
			print("\n~ Removing a marker ~")
			markers = markerManager.get_markers()
			for i in range(len(markers) - 2):
				print("{0}: {1}".format(i, markers[i + 1]))
			markerToRemove = int(input("Which marker do you want to remove?\n: "))
			markerManager.remove_marker(markerToRemove + 1)

		elif option == 4:
			quit()
except KeyboardInterrupt:
	quit()
