import googleapiclient.discovery
import googleapiclient.errors
import csv

# API key to access the YouTube Data API
api_key = "AIzaSyABltYVWVyvzRn2epeNEPN5uy3NpTYAvTE"

# YouTube channel ID
channel_id = "UC9Pj0EUibBF295jWHRSDJqg" # schannel

# Create a YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Retrieve the channel's video playlist ID
channel_response = youtube.channels().list(
    part="contentDetails",
    id=channel_id
).execute()

playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Retrieve the videos from the playlist
videos = []
next_page_token = None

while True:
    playlist_items = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    videos += playlist_items['items']
    next_page_token = playlist_items.get('nextPageToken')

    if not next_page_token:
        break

# Save the video information to a CSV file
with open('channel_videos.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['title', 'description', 'tags', 'publishedAt', 'videoId']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for video in videos:
        title = video['snippet']['title']
        description = video['snippet']['description']
        tags = ",".join(video['snippet']['tags']) if 'tags' in video['snippet'] else ""
        published_at = video['snippet']['publishedAt']
        video_id = video['snippet']['resourceId']['videoId']

        writer.writerow({
            'title': title,
            'description': description,
            'tags': tags,
            'publishedAt': published_at,
            'videoId': video_id
        })
