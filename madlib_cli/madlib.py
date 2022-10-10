import re
from nltk.corpus import wordnet
# '/home/slowres/401/lab3/.venv/nltk_data'
# '/home/slowres/401/lab3/.venv/nltk_data'
# corpora/wordnet

#path = "assets/dark_and_stormy_night_template.txt"
path = "assets/story.txt"

def validate_input(input):
    word = wordnet.synsets(input)
    if (word):
        return True
    return False

def read_template(path) :  
    """
    Reads the file and return it
    """

    content = ''
    
    try:
        with open(path) as f:
            content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError   

    return content

#x = read_template(path)

def parse_template(content):
    """
    It receives string and it returns 
    a tuple that contains the string with place
    holders and their names
    """ 
    string = content    
    pattern = r"\{([a-zA-Z0-9 '-]+)\}"
    result = re.findall(pattern,string)
    newString = string

    for word in result:
        newString = newString.replace(word,'')


    stripped = newString
    parts = tuple(result)

    return (stripped,parts)

#strippedstring , list_inputs = parse_template(x)

def getInputs (inputs):

    userInputs = []
    for prompt in inputs:
        userinput = input('Please Insert '+ prompt + ': ')
        userInputs.append(userinput)
        
        

            
    return userInputs

#inputs = getInputs(list_inputs)

def merge(strippedstring , inputs):

    """
    It receives stripped string and the user inputs,
    it returns the filled string
    """ 

    mergedString = strippedstring.format(*inputs)

    return mergedString

#merged = merge(strippedstring,inputs)

def create_response(merged):
    path = "assets/response.txt"
    try:
        with open(path,'w') as f:
            content = f.write(merged)
    except FileNotFoundError:
        print("No file found")    

    return path

#print(read_template(create_response(merged)))

    



