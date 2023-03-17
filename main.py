import requests as r
import json
from tqdm import tqdm

urls = [
    "https://www.instagram.com/reel/CoVqDZKJeEK/",
]


def get_urls_from_profile(username: str):
    """Get the urls of the reels from the given username."""
    try:
        page = r.get(f"https://www.instagram.com/{username}/?__a=1&__d=dis")
        data = json.loads(page.text)

        reels = data["graphql"]["user"]["edge_felix_video_timeline"]["edges"]
        urls = [
            f"https://www.instagram.com/reel/{reel['node']['shortcode']}/"
            for reel in reels
        ]

    except Exception as error:
        return error

    return urls


def download_reels(urls):
    """Download the reels from the given urls."""
    index = 0
    try:
        for url in tqdm(urls):
            page = r.get(f"{url}?__a=1&__d=dis")
            data = json.loads(page.text)

            reel_link = data["graphql"]["shortcode_media"]["video_url"]
            reel = r.get(reel_link)
            with open(f"videos/video{index}.mp4", "wb") as f:
                f.write(reel.content)
            index += 1

    except Exception as error:
        return error

    return "Reels Downloaded Successfully"


# def get_reels_from_chat():


if __name__ == "__main__":
    # urls = get_urls_from_profile("ranasmag")

    download_reels(urls)
