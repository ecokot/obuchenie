import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text

async def main():
    # Обрати внимание на sqlite+aiosqlite — это указание использовать асинхронный диалект
    engine = create_async_engine("sqlite+aiosqlite:///async_demo.db", echo=True)

    async with AsyncSession(engine) as session:
        result = await session.execute(text("SELECT 1 + 1"))
        print(result.scalar())

asyncio.run(main())