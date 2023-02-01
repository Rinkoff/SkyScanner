from configparser import ConfigParser
import os


# Define the package directory as the directory where this file is located
package_directory = os.path.dirname(os.path.abspath(__file__))

# Define a function to read the database configuration file
def read_db_congig(filename="config.ini",section="MySQL"):
    # Create a parser object
    parser=ConfigParser()

    # Read the configuration file
    if parser.read(os.path.join(package_directory,filename)):

        # If the config file is found, create an empty dictionary to store the configuration
        db_config={}

        # Check if the specified section exists in the file
        if parser.has_section(section):
            # If the section exists, retrieve all the items in the section
            items=parser.items(section)

            # Iterate over the items and add them to the dictionary
            for item in items:
                db_config[item[0]]=item[1]

            return db_config

        # If the section does not exist, raise an exception
        else:
            raise Exception(f"{section} is not found in the {filename}")

    # If the configuration file is not found, raise an exception
    else:
        raise Exception(f"{filename} is not found")


# if __name__ == '__main__':
#     db_config=read_db_congig("../config.ini","MySQL")
#     print(db_config)