class MarkerManager:
	geojson_path = "../geojson/markers.geojson"

	def add_marker(self, title, icon, lat, long):
		# Split the geoJson file into lines.
		geojson_file = open(self.geojson_path, "r")
		array_of_lines = geojson_file.read().splitlines()
		geojson_file.close()

		line_to_add = '{"type": "Feature","geometry": {"type": "Point","coordinates": [%s,%s]},"properties": ' + \
			'{"title": "%s","icon": "%s"}},'
		line_to_add = line_to_add % (str(lat), str(long), title, icon)
		array_of_lines.insert(len(array_of_lines) - 1, line_to_add)

		# Reopen the file for writing.
		geojson_file = open(self.geojson_path, "w")
		for line in array_of_lines:
			geojson_file.write(line + "\n")
		geojson_file.close()


# Main code.
generator = MarkerManager()
try:
	title = str(input("Name of the location\n: "))
	lat = str(input("Latitude\n: "))
	long = str(input("Longitude\n: "))
	icon = str(input("Icon\n: "))
	generator.add_marker(title, icon, lat, long)
except KeyboardInterrupt:
	quit()
