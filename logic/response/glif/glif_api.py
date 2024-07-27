import requests
import os
from dotenv import load_dotenv
import json
from bs4 import BeautifulSoup

class GlifAPI():
    def __init__(self):
        self.api_key = os.getenv("GLIF_TOKEN")
        pass

    def request(self, mem_id, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]

        try:
            response = requests.post(
                "https://simple-api.glif.app",
                json={"id": mem_id, "inputs": inputs},
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"Error connecting to the server: {e}")
            return None
        except requests.exceptions.Timeout as e:
            print(f"The request timed out: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    def wojak_mems(self, text):
        response = self.request('clxtc53mi0000ghv10g6irjqj', text)

        if response is None:
            return None

        res = json.loads(response.content.decode('utf-8'))
        soup = BeautifulSoup(res['outputFull']['html'], 'html.parser')

        paragraphs = soup.find_all('p')
        return [p.text for p in paragraphs[1:]]

if __name__ == '__main__':
    load_dotenv('config/.env')

    api = GlifAPI()
    print(api.wojak_mems("protoss fan"))