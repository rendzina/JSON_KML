#!/usr/bin/python
# parse_json_route.py
# Usage: parse_json_route.py -i <inputfile>

import sys, getopt, os, json

def main(argv):
	inputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
	except getopt.GetoptError:
		print 'parse_json_route.py -i <inputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'parse_json_route.py -i <input json file>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
			stem = os.path.splitext(inputfile)[0]
			kml_outputfile = stem + '.kml'
			kml_outfile_handle = open(kml_outputfile, 'w')
			header = '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document><name>' + kml_outputfile + '</name><open>1</open><Style id="s_ylw-pushpin_hl"><IconStyle><scale>1.3</scale><Icon><href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href></Icon><hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/></IconStyle><LineStyle><color>ff00bd00</color><width>2</width></LineStyle></Style><StyleMap id="m_ylw-pushpin"><Pair><key>normal</key><styleUrl>#s_ylw-pushpin</styleUrl></Pair><Pair><key>highlight</key><styleUrl>#s_ylw-pushpin_hl</styleUrl></Pair></StyleMap><Style id="s_ylw-pushpin"><IconStyle><scale>1.1</scale><Icon><href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href></Icon><hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/></IconStyle><LineStyle><color>ff00bd00</color><width>2</width></LineStyle></Style><Placemark><name>Road journey</name><styleUrl>#m_ylw-pushpin</styleUrl><LineString><tessellate>1</tessellate><coordinates>'
			footer = '</coordinates></LineString></Placemark></Document></kml>'
			kml_outfile_handle.write(header)

			with open(inputfile, 'r') as trace:
				obj = json.load(trace)
      	 
				for d in obj:
					geom = "{},{},0 ".format(d["locationLongitude"],d["locationLatitude"])
					#geom = "%f,%f,0 " % (d["locationLongitude"],d["locationLatitude"])
					#geom = d["locationLongitude"],",",d["locationLatitude"],",",0," "
					kml_outfile_handle.write(geom)
    	
			kml_outfile_handle.write(footer)
			kml_outfile_handle.close
		else:
			print 'Please provide parameter JSON file'

if __name__ == "__main__":
	main(sys.argv[1:])
