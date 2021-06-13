import os
import xmltodict
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
xml_dir = current_dir + "\\reuters"
json_dir = current_dir + "\\json"
files = os.listdir(xml_dir)

for path, subdirs, files in os.walk(xml_dir):
    for name in files:
        # Joins the current path with the filename.
        xml_read_path = os.path.join(path, name)
        # Truncates the .xml from the filename and appends .json.
        json_filename = name.rsplit('.', 1)[0] + '.json'
        # Sets the directory where the file will be written. (windows)
        json_write_path = json_dir + "\\" + json_filename

        # Open the xml and parse it.
        with open (xml_read_path) as xml_doc:
            print("Currently parsing: ", xml_read_path)
            data_dict = xmltodict.parse(xml_doc.read())
            xml_doc.close()

            # Put the dictionary data inside a json.
            json_data = json.dumps(data_dict)

            # Write the json to an actual file.
            with open(json_write_path, "w") as json_doc:
                json_doc.write(json_data)
                json_doc.close()
                print(json_write_path, "written.")
