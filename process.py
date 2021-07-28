import asyncio
from tqdm import tqdm

from utils.file import import_data, save_data
from utils.request import Request

class Process(Request):
    def __init__():
        super().__init__()
        

    async def main(self,):
        video_id_column_name = ""


        self.create_connections()
        for data, fname in import_data():
            tasks = [self.get_banned_reason(video_id) for video_id in data[video_id_column_name]]
            results = [await t for t in tqdm(asyncio.as_completed(tasks), desc="Getting Banned Reason")]
            self.save_results(data, results, fname)


    def save_results(self, data, results, fname):
        for data, results in zip(data, results):
            if results is not None:
                data["banned_status"] = results['status']
                data["banned_reason"] = results['reason']
                data["banned_message"] = "\n".join(results['messages'])
        save_data(data, fname, 'xlsx')





