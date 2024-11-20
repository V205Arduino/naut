from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import time 


app = FastAPI()
startTime = time.time()
page = f'''
---------------------
START OF TRANSMISSION
---------------------
Hello there!
This is a plaintext site.
And yes, it's supposed to be loading this.... slow (purposely slows the loading down at this point)
Oh, it sped up.

Time since 1970, January 1
{startTime}
-------------------
END OF TRANSMISSION
-------------------
'''


async def fake_data_streamer():
    for i in page:
        # if i % 10 == 9:
        #     yield f"{i} \n"
        # else:
        #     yield f"{i}"
        yield f"{i}"
        await asyncio.sleep(0.05)

    # for i in iter(page.splitlines()):
    #     yield f"{i}\n"
    #     await asyncio.sleep(0.5)


# If your generator contains blocking operations such as time.sleep(), then define the
# generator function with normal `def`. Alternatively, use `async def` and run any 
# blocking operations in an external ThreadPool/ProcessPool. (see 2nd paragraph of this answer)
'''
import time

def fake_data_streamer():
    for i in range(10):
        yield b'some fake data\n\n'
        time.sleep(0.5)
'''        

    
@app.get('/')
async def main():
    return StreamingResponse(fake_data_streamer(), media_type='text/event-stream')
    # or, use:
    '''
    headers = {'X-Content-Type-Options': 'nosniff'}
    return StreamingResponse(fake_data_streamer(), headers=headers, media_type='text/plain')
    '''