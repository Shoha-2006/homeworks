import requests
import csv
import os




folder_name = "CsvsFromApi"
os.makedirs(folder_name, exist_ok=True)





resources = {
    "posts": "posts.csv",
    "comments": "comments.csv",
    "albums": "albums.csv",
    "photos": "photos.csv",
    "todos": "todos.csv",
    "users": "users.csv"
}

for resource, filename in resources.items():
    url = f"https://jsonplaceholder.typicode.com/{resource}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        full_filename = os.path.join(folder_name, filename)
        
        with open(full_filename, mode="wt", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
        
        print(f"Data from {resource} has been written to {full_filename}")
    else:
        print(f"Failed to fetch {resource}")
