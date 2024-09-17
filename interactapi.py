import requests

base_url = "https://jsonplaceholder.typicode.com"
def fetch_all_todos():
    # Define the base URL for the JSONPlaceholder API
    # base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve posts
    response = requests.get(f"{base_url}/todos")

    # Check if the request was successful (status code 200)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        # Parse the JSON response
        #posts = response.json()

        # Display the first few posts
        # for post in posts[:5]:
        #     print(f"Post ID: {post['id']}")
        #     print(f"Title: {post['title']}")
        #     print(f"Body: {post['body']}")
        #     print("\n" + "-" * 40)
        todos = response.json()
        for todo in todos[:4]:
            print(f"User ID: {todo['userId']}")
            print(f"Todos ID: {todo['id']}")
            print(f"title: {todo['title']}")
            print(f"completed: {todo['completed']}")
            print("\n" + "-" * 40)
    else:
        print(f"Error: Unable to retrieve todos. Status Code: {response.status_code}")

#
def get_user(todos_id):
    # Define the base URL for the JSONPlaceholder API
    # base_url = "https://jsonplaceholder.typicode.com"


    response = requests.get(f"{base_url}/todos/{todos_id}")

    # Check if the request was successful (status code 200)
    print(f"Response status code: {response.status_code}")
    if(response.status_code==200):
        todo=response.json()
        print(f"Todo full response : {todo}")
        print(f"User ID: {todo['userId']}")
        response2=requests.get(f"{base_url}/users/{todo['userId']}")
        if(response2.status_code==200):
            user=response2.json()
            print(f"Name: {user['name']}")
            print(f"User Name: {user['username']}")
            print(f"email: {user['email']}")
            print(f"website: {user['website']}")
        else:
            print(f"Error: Unable to retrieve user. Status Code: {response.status_code}")

    else:
        print(f"Error: Unable to retrieve todo. Status Code: {response.status_code}")



if __name__ == "__main__":
    # Call the function to fetch and display posts
    fetch_all_todos()
    todo_id=input("Enter the todo id : ")
    get_user(todo_id)

