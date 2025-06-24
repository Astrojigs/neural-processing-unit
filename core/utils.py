import asyncio
from crawl4ai import *

url = input('Enter Url: ')
name = input('filename: ')


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        print('Returning content from file...')
        return result.markdown


with open(f"{name}.txt" if '.txt' not in name else name, "w", encoding='utf-8') as file:
    content = asyncio.run(main())
    print('Writing content in file...')
    file.write(content)
    print('File updated with content.')
