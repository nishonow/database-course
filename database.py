import asyncpg

class Database:
    def __init__(self, url):
        self.url = url
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.url)

    async def close(self):
        await self.pool.close()

    async def create_tables(self):
        async with self.pool.acquire() as conn:
            await conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name TEXT
            )
            """)

            await conn.execute("""
            CREATE TABLE IF NOT EXISTS student_courses (
                student_id INT,
                course_id INT
            )
            """)

            await conn.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id SERIAL PRIMARY KEY,
                name TEXT
            )
            """)

    async def add_student(self, name):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO students (name) VALUES ($1)",
                name,
            )

    async def add_course(self, name):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO courses (name) VALUES ($1)",
                name,
            )

    async def del_course(self, id):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "DELETE FROM courses WHERE id = $1",
                id,
            )

    async def del_student(self, id):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "DELETE FROM students WHERE id = $1",
                id,
            )

    async def drop_tables(self):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "DROP TABLE IF EXISTS students"
            )
            await conn.execute(
                "DROP TABLE IF EXISTS student_courses"
            )
            await conn.execute(
                "DROP TABLE IF EXISTS courses"
            )

