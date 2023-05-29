import csv
import facebook

# Replace the access_token with your own access token
access_token = "236396558948986|rtvIkXCM2AMyMmlo-B8g99aUkX8"
graph = facebook.GraphAPI(access_token, version="3.0")

# Replace the page_id with the ID of the page you want to crawl data from
page_id = "KCrushbetterthanyourcrush"

# Get information about the page
page_info = graph.get_object(id=page_id, fields="name, about, fan_count, website")

# Get the posts published on the page
posts = graph.get_connections(id=page_id, connection_name="posts")

# Create a CSV file to store the data
csv_file = open("page_data.csv", mode="w", encoding="utf-8", newline="")
fieldnames = ["post_id", "message", "created_time", "reactions"]
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

# Iterate over the posts and write data to the CSV file
for post in posts["data"]:
    # Get the reactions for the post
    reactions = graph.get_connections(id=post["id"], connection_name="reactions")
    # Count the number of reactions
    reaction_count = len(reactions["data"])
    # Write the data to the CSV file
    writer.writerow({"post_id": post["id"], "message": post["message"], "created_time": post["created_time"], "reactions": reaction_count})

# Close the CSV file
csv_file.close()
