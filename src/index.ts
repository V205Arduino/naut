import { Elysia } from "elysia";
import { getLatestData } from "./octokit";

// const data =  [
//   {
//     "timestamp": 12345,
//     "type" : "book",
//     "title": "Command and Control",
//     "author": "Someone",
//     "stars": 5
//   },
//   {
//     "timestamp": 54321,
//     "type" : "book",
//     "title": "controlling the commanders",
//     "author": "Social Engineer",
//     "stars": 4
//   },
// ]

const app = new Elysia()
  .get('/', 'Hello World')
  .get('/image', Bun.file('mika.webp'))
  .get('/stream', function* () {
    yield 'Hello'
    yield 'World'
  })
  .get('/API', async () => {
    try {
      const data = await getLatestData();
      return data;
    } catch (error) {
      console.error(error);
      return { error: 'Failed to fetch data' };
    }
  })
  .listen(3000);




  
console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);

