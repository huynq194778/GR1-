import googleapiclient.discovery
import googleapiclient.errors
import csv

# API key for the YouTube Data API v3
API_KEY = 'AIzaSyABltYVWVyvzRn2epeNEPN5uy3NpTYAvTE'

# Create a YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

# Define the hashtag you want to search for
hashtag = 'iPhone'

# Use the search endpoint to search for videos with the specified hashtag
search_response = youtube.search().list(
    q=hashtag,
    type='video',
    part='id,snippet',
    maxResults=50
).execute()

# Extract the video IDs from the search results
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Initialize an empty list to hold the video data
video_data = []

# Use the videos endpoint to retrieve information about each video
for video_id in video_ids:
    video_response = youtube.videos().list(
        id=video_id,
        part='snippet,statistics'
    ).execute()

    # Extract the data for this video
    video = {}
    video['video_id'] = video_id
    video['title'] = video_response['items'][0]['snippet']['title']
    video['channel_name'] = video_response['items'][0]['snippet']['channelTitle']
    video['publish_time'] = video_response['items'][0]['snippet']['publishedAt']
    video['view_count'] = video_response['items'][0]['statistics']['viewCount']

    # Append the data for this video to the list
    video_data.append(video)

# Save the video data to a CSV file
with open('video_data_new.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['video_id', 'title', 'channel_name', 'publish_time', 'view_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for video in video_data:
        writer.writerow(video)
