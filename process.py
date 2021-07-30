import asyncio
from tqdm import tqdm

from utils.file import import_data, save_data
from utils.request import Request

class Process(Request):
    def __init__(self, ):
        super().__init__()
        

    async def main(self,):
        video_id_column_name = "video_id"


        await self.create_connections()
        for data, fname in import_data():
            tasks = [self.get_banned_reason(row[video_id_column_name]) for row in data]
            results = [await t for t in tqdm(asyncio.as_completed(tasks), desc="Getting Banned Reason", total=len(tasks))]
            self.save_results(data, results, fname)


    def save_results(self, data, results, fname):
        for d, r in zip(data, results):
            d.update(r)
        save_data(data, fname, 'xlsx')

if __name__ == '__main__':
    p = Process()
    asyncio.run(p.main())



