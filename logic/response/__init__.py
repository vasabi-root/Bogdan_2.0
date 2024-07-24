from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path_to_resource = "../../config/.env"
resource_file_path = os.path.join(script_dir, relative_path_to_resource)

load_dotenv(resource_file_path)