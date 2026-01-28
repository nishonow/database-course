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
                student_id INT REFERENCES student(id) ON DELETE CASCADE,
                course_id INT REFERENCES courses(id) ON DELETE CASCADE,
                PRIMARY KEY (student_id, course_id)
            )
            """)

            await conn.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id SERIAL PRIMARY KEY,
                name TEXT
            )
            """)

    async def alter_students(self):
        async with self.pool.acquire() as conn:
            await conn.execute("""
                ALTER TABLE student ADD COLUMN surname TYPE TEXT
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

    async def add_student_course(self, student_id, course_id):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO student_courses (student_id, course_id) VALUES ($1, $2)",
                student_id,
                course_id,
            )

    async def show_students(self):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT * FROM students")
            return rows

    async def show_students_courses(self, id):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT courses.id, courses.name FROM courses
                JOIN student_courses ON courses.id = student_courses.course_id
                WHERE student_courses.student_id = $1
                """,
                id,
            )
            return rows

    async def get_all_students_with_courses(self):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT students.id, students.name, courses.id AS course_id, courses.name AS course_name
                FROM students
                LEFT JOIN student_courses ON students.id = student_courses.student_id
                LEFT JOIN courses ON student_courses.course_id = courses.id
                """
            )
            return rows

    async def get_student_course_count(self):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT students.id, students.name, COUNT(student_courses.course_id) AS total_courses
                FROM students
                LEFT JOIN student_courses ON students.id = student_courses.student_id
                GROUP BY students.id, students.name
                """
            )
            return rows

    async def update_student(self, id, name):
        async with self.pool.acquire() as conn:
            await conn.fetch("""
                UPDATE students SET name = $1 WHERE id = $2
            """, name, id)

    async def count_students(self):
        async with self.pool.acquire() as conn:
            count = await conn.fetchval("SELECT COUNT(*) FROM students")
            return count

    async def count_courses(self):
        async with self.pool.acquire() as conn:
            count = await conn.fetchval("SELECT COUNT(*) FROM courses")
            return count

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

