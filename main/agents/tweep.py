import tweepy

# Your Twitter API credentials
API_KEY = 'SaE9MsC3Sn0e84m1yMbDbf4NP'
API_SECRET_KEY = '4DupDbNH6gtze7mLfnMlhzFe3aldbIyRXuLV5BaMZwTwUYYpTl'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOtJvQEAAAAAVk8TRehO%2BSuMgEB5kz5q3Xw5Svc%3D0FJvt92KJUNFlea6YxF42wMiXEHaB91HnC0HqwjKgGEHi6CbOq'
ACCESS_TOKEN = '1822933497444732928-hMmW0LxbywsxsbPSKNO3zYHgIxtkrm'
ACCESS_TOKEN_SECRET = 'YrZXYf4MyeE5AqIHR1yZf97Nv8p9PsYThcHE7imAOE7hd'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Function to scrape a Twitter profile
def scrape_twitter_profile(username):
    try:
        # Get user profile information
        user = api.get_user(screen_name=username)

        print(f"User: {user.name}")
        print(f"Bio: {user.description}")
        print(f"Location: {user.location}")
        print(f"Followers: {user.followers_count}")
        print(f"Following: {user.friends_count}")
        print(f"Tweets: {user.statuses_count}")

        # Get the user's recent tweets
        tweets = api.user_timeline(screen_name=username, count=10, tweet_mode="extended")

        for tweet in tweets:
            print(f"\nTweet: {tweet.full_text}")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
username = "jack"  # Replace with the Twitter username you want to scrape
scrape_twitter_profile(username)
