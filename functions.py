

#function that shows all availables options
def view_options():
    print('Hello, what are we going to do?\n'
          '1 - Register collaborator\n'
          '2 - View records\n'
          '3 - Create work schadule\n'
          '4 - Edit registration'
          )
    
#function that register collaborators  
def register_collaborator(collaborators):
    collaborator = {}
    collaborator ['name'] = input("Enter the collaborator's name: ")
    collaborator ['time'] = input("Enter the collaborator's time: ")
    collaborator ['scale'] = input('Enter the scale (6x1 or 5x2): ')
    collaborators.append(collaborator)
    
    print(f'Collaborator {collaborator['name']} successfully registered!')

    