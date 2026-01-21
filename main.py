import asyncio
from database import Database

DB_URL = "postgresql://postgres:xhvIWIdSZYOSOvTQTEieUFzyiDOJjCCk@caboose.proxy.rlwy.net:56387/railway"

async def main():
    db = Database(DB_URL)
    await db.connect()

    await db.create_tables()

    # await db.add_student("Sam")
    # await db.add_student("Dean")
    # await db.add_student("Castiel")
    #
    # await db.add_course("Database")
    # await db.add_course("OOP")
    # await db.add_course("Operating Systems")

    # await db.drop_tables()

    await db.close()

asyncio.run(main())
