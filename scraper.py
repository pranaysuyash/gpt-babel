import requests
from bs4 import BeautifulSoup
import json

def scrape_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag with the JSON content
        script_tag = soup.find('script', type='application/json')
        if not script_tag:
            return None
        
        # Extract the JSON string
        json_text = script_tag.string

        # Load the JSON to a Python dictionary
        data = json.loads(json_text)

        # Navigate through the JSON to extract the desired data
        page_props = data.get('props', {}).get('pageProps', {})
        gizmo_data = page_props.get('gizmo', {}).get('gizmo', {})
        
        # Extract the relevant information
        extracted_data = {
            'id': gizmo_data.get('id', ''),
            'organization_id': gizmo_data.get('organization_id', ''),
            'short_url': gizmo_data.get('short_url', ''),
            'author': {
                'user_id': gizmo_data.get('author', {}).get('user_id', ''),
                'display_name': gizmo_data.get('author', {}).get('display_name', ''),
                'is_verified': gizmo_data.get('author', {}).get('is_verified', False),
            },
            'display': {
                'name': gizmo_data.get('display', {}).get('name', ''),
                'description': gizmo_data.get('display', {}).get('description', ''),
                'welcome_message': gizmo_data.get('display', {}).get('welcome_message', ''),
                'prompt_starters': gizmo_data.get('display', {}).get('prompt_starters', []),
                'profile_picture_url': gizmo_data.get('display', {}).get('profile_picture_url', '')
            }
        }

        return extracted_data

    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6+
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6+
    
    return None
