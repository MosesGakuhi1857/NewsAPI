class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,description,time,url,image,title):
        
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title

class Category:
    '''
     Category class to define the categories object
    '''

    def __init__(self,author,description ,time,url,image,title):
        self.author = author
        self.description =description
        self.time = time
        self.url = url
        self.image = image
        self.title =title

class Source:
    '''
    Source class define the source objects
    '''
    def __init__(self,id,name,description,url):
        
        self.id = id
        self.name = name
        self.description=description
        self.url=url

class Headlines:

    '''
     Class that defines the Headlines objects
    '''

    def __init__(self,description,time,url,image,title):
        
        self.description = description
        self.time = time
        self.url = url
        self.image= image
        self.title = title