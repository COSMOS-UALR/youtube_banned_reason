import asynctest

from request import Request

class TestBannedRequests(asynctest.TestCase):
    R = Request()

    async def test_banned_requests(self):
        await self.R.create_connections()
        self.assertTrue(await self.R.get_banned_reason('-rc1hGlFqr8'))

    async def test_good_video(self):
        await self.R.create_connections()
        v = await self.R.get_banned_reason('Y6Rd9ZQBVG0')
        self.assertEqual(v, {'banned_status': None, 
            'banned_reason': None,
            'banned_message': None})

    async def test_all_banned_reasons(self,):
        await self.R.create_connections()
        # private videos
        self.assertEqual(await self.R.get_banned_reason('-rc1hGlFqr8'), {'banned_status': 'LOGIN_REQUIRED', 'banned_reason': 'This video is private.', 'banned_message': 'This video is private.'})
        # account ternimated
        self.assertEqual(await self.R.get_banned_reason('-KnqC5-fHik'), {'banned_status': 'ERROR', 'banned_reason': 'Video unavailable', 'banned_message': 'Video unavailable'})
        # video unavailable
        self.assertEqual(await self.R.get_banned_reason('cm5_-X85pnl'), {'banned_status': 'ERROR', 'banned_reason': 'Video unavailable', 'banned_message': 'Video unavailable'})
        # against TOS
        self.assertEqual(await self.R.get_banned_reason('FckNFcypc90'), {'banned_status': 'ERROR', 'banned_reason': "This video has been removed for violating YouTube's Terms of Service.", 'banned_message': "This video has been removed for violating YouTube's Terms of Service."})



