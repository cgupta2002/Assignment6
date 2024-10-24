import sqlite3

class Project:
    def __init__(self, title, description, affiliation, imgName, timeline, link):
        self.__title = title
        self.__description = description
        self.__affiliation = affiliation
        self.__imgName = imgName
        self.__timeline = timeline
        self.__link = link

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, value):
        self.__affiliation = value
    
    @property
    def imgName(self):
        return self.__imgName

    @imgName.setter
    def imgName(self, value):
        self.__imgName = value

    @property
    def timeline(self):
        return self.__timeline

    @timeline.setter
    def timeline(self, value):
        self.__timeline = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    def __str__(self):
        return self.title + " ("  + str(self.timeline) + ") with {}".format(self.affiliation)

    @classmethod
    def delProject(cls, title):
        conn = None
        conn = sqlite3.connect( "projects.db")
        sql='DELETE FROM projects WHERE title=?'
        cur = conn.cursor()
        cur.execute(sql, (title,))
        conn.commit()
        conn.close()

    @classmethod
    def addProject(cls, title, description, affiliation, imgName, timeline, link):
        conn = None
        conn = sqlite3.connect( "projects.db")
        sql='INSERT INTO projects (title, description, affiliation, imgName, timeline, link) values (?,?,?,?,?,?)'
        cur = conn.cursor()
        cur.execute(sql, (title, description, affiliation, imgName, timeline,link, ))
        conn.commit()
        if conn:
            conn.close()

    @classmethod
    def updateProject(cls, title, description, affiliation, imgName, timeline, link):
        conn = None
        conn = sqlite3.connect('projects.db')
        sql='UPDATE projects SET description = ?, affiliation = ?, imgName = ?, timeline = ?, link = ? WHERE title = ?'
        cur = conn.cursor()
        cur.execute(sql, (description, affiliation, imgName, timeline, link, title,))
        conn.commit()
        conn.close()

    @classmethod
    def getAllProjects(cls):
        conn = sqlite3.connect('projects.db')
        cursorObj = conn.cursor()
        cursorObj.execute('SELECT title, description, affiliation, imgName, timeline, link FROM projects;')
        allRows = cursorObj.fetchall()
        movieListOfDictionaries = []
        for row in allRows:
            m = {"title" : row[0], "description": row[1], "affiliation":row[2], 'imgName': row[3], 'timeline':row[4], 'link':row[5] }
            movieListOfDictionaries.append(m)
        if conn:
            conn.close()
        return movieListOfDictionaries

def InsertStartingData():
    conn = sqlite3.connect('projects.db')
    cur = conn.cursor()
    project_data = [
    ('Information Infrastructure II Final Project', 'I created this website in late 2022 to complete the class I TA\'d for a year. This website includes SQL connectivity, Python/Flask development, and basic HTML/CSS skills.', 'Luddy School of Informatics', 'i211.png', '2022','https://cgi.luddy.indiana.edu/~chirgupt/I211_project.cgi'),
    ('Digital Solution Design Final Project', 'This website was a front-end prototype for our project, which was centered around building a platform for the MSIS program. This website was created solely using HTML/CSS.', 'MSIS Program', 's310.png', '2022', 'https://chirgupt.pages.iu.edu/MSIS_Capstone_Project/index.html'),
    ('Information Representation Final Project', 'This website was connected to a SQL database and used PHP to pass data between the website and database.', 'Luddy School of Informatics', 'i308.png', '2022', 'https://cgi.luddy.indiana.edu/~chirgupt/main.php'),
    ('Technology and Business Analysis Final Project', 'This script was my final project using R. I compiled data for my favorite baseball team and compared their team statistics over the past 10 years alongside the stats of the top 5 players each year.','Kelley School of Business', None,'2022','https://github.com/cgupta2002/K304FinalProject')]
    cur.executemany('''INSERT INTO projects (title, description, affiliation, imgName, timeline, link) VALUES (?, ?, ?, ?, ?, ?)''', project_data)
    conn.commit()
    conn.close()

def createProjectDB():
    conn = sqlite3.connect('projects.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS projects (title TEXT NOT NULL,description TEXT NOT NULL,affiliation TEXT NOT NULL,imgName TEXT,timeline TEXT, link TEXT)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    createProjectDB()
    InsertStartingData()
    print(Project.getAllProjects())