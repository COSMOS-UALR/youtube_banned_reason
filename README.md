# YouTube Banned Reason
A script to find the banned reason for YouTube videos

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
For the API to work, you need a propritary API key and a cookie from the YouTube iFrame player. There is currenlty one in this project, but we do not know when it will expire. If you are having issues contact Joseph or Thomas. 
