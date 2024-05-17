import requests

def get_example():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    if response.status_code == 200:
        print("GET request successful!")
        
        posts = response.json()
        for i, post in enumerate(posts, start=1):
            print(f"Post {i}:")
            print(post)
            print()
        
        titles = response.json()
        print("Titles of all posts:")
        for i, title in enumerate(titles, start=1):
            print(f"Post {i} title:", title['title'])
    else:
        print("Failed to retrieve data")

def main():
    print("Executing GET example...")
    get_example()

if __name__ == "__main__":
    main()
