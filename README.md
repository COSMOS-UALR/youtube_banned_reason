# YouTube Banned Reason
A script to find the banned reason for YouTube videos. This works by reading json/csv/xlsx files containing YouTube video data. It will grab the video ids from those files and query the YouTube iframe API to get the video's banned reason. We will update the Import files with this information and save them to the Export folder. 

The script will add these columns to the video data: `banned_status`, `banned_reason`, `banned_message` (all say pretty much the same thing). If a video is available, these columns will be empty.

# Run the script
1. Git clone the repository
2. Activate a virtual environment
3. Install the requirements `pip install -r requirements.txt`
4. Import the files you want to process into the 'Import' folder
    - Supported file formats are json, csv, and xlsx
5. Edit the `video_id_column_name` variable in the `process.py` file to the name of the column containing the video ids
6. Run the script `python process.py`
7. The output will be in the `Export` folder
    - Currently set to export as xlsx

# Cookies & API Keys
For the API to work, you need a propritary API key and a cookie from the YouTube iFrame player. There is currenlty one in this project, but we do not know when it will expire. One way to generate your own is to open the `player.html` file and fetch the cookie and key from the player:
1. In Chrome, open `player.html`.
2. Open the developer side panel (Ctrl+Shift+I).
3. Click on the 'Network' Tab.
![Network tab](/img/devpanel.png)
4. Filter network events by `Name` to order alphabetically.
![Filter by name](/img/filterpanel.png)
5. Look for the event starting with `player?key=` and click on it.
6. Scroll down to reveal the `Request Headers` and make a note of the API key (within the `path` parameter) as well as the `cookie`.
![Filter by name](/img/parameters.png)

If you are having issues contact Joseph or Thomas. 
