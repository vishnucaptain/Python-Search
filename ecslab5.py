from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    try:
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res.get('items', [])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    
    api_key = ' ' #enter API
    cse_id = 'f0f6c69a921d049dc'
    
    search_term = input("Input to search: ")
    results = google_search(search_term, api_key, cse_id)
    
    if results:
        for result in results:
            print('Title:', result.get('title'))
            print('Snippet:', result.get('snippet'))
            print('Link:', result.get('link'))
            print()
    else:
        print("No results found.")

if __name__ == '__main__':
    main()