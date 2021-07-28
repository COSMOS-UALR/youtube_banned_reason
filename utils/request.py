import aiohttp
import json

class Request():
    def __init__(self,):
        self.session = None

    async def create_connections(self, limit:int=1):
        # conn = aiohttp.TCPConnector(limit=limit)
        # time_out = aiohttp.ClientTimeout(60*2)
        self.session = aiohttp.ClientSession()
        # self.sem = asyncio.Semaphore(limit)

    async def get_banned_reason(self, video_id:str):
        #This key is from youtube (not the data api)
        url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"

        payload = json.dumps({
        "videoId": video_id,
        "context": {
            "client": {
            "clientName": "WEB_EMBEDDED_PLAYER",
            "clientVersion": "1.20210721.1.0",
            "clientScreen": "EMBED"
            }
        }
        })
        #This cookie is required to get the reason, it's from the iframe player
        headers = {
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'content-type': 'application/json',
        'cookie': '__Secure-3PSID=9ge0SktiBayObQFjl-ipRpi5vMSGXx2DLhMtOOB2lro_-7_HJ_Jp3SVJTKu3nNAiIvsX3g.; __Secure-3PAPISID=p5AV_QI_4vzhwLOO/AzygtIkY7QTX5mB-J; VISITOR_INFO1_LIVE=BX2tEd2nRwc; __Secure-3PSIDCC=AJi4QfFcjRKrsxkon2KO-9aiW-8uMaEV0qm5i-D0ADBggop0KRGCYD2i69LoqEN42j2M-Q5eOg; YSC=WJ580-H2AKA'
        }
        async with self.session.post(url, data=payload, headers=headers) as response:
            if response.status == 200:
                resp= await response.json()
                return self.parse_response(resp['playabilityStatus'])
            else:
                print("Error: {}".format(response.reason))
                return None

    def parse_response(self, response):
        if response is None or response['status']=="OK":
            return {'banned_status': None, 
            'banned_reason': None,
            'banned_message': None}
        else:
            return {'banned_status': response['status'], 
                'banned_reason': response['reason'],
                'banned_message': "\n".join(response['message']) if 'message' in response else response['reason']}