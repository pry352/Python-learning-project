def add_setting(settings,setting):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    if key in settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key] = value
        return (f"Setting '{key}' added with value '{value}' successfully!")
    
def update_setting(settings,setting):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    if key in settings:
        settings[key] = value
        return (f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings,key):
    key = str(key).lower()
    if key in settings:
        del settings[key]
        return (f"Setting '{key}' deleted successfully!")
    else:
        return ('Setting not found!')
    
def view_settings(settings):
    if not settings:
        return ('No settings available.')
    else:
        teks = ['Current User Settings:']
        for key,value in settings.items():
            teks.append(f"{key.capitalize()}: {value}")
    return '\n'.join(teks)+'\n'

if __name__ == "__main__":
    test_settings = {'Theme':'dark','Notifications':'enabled','Volume':'high'}
    print("User Configuration Manager")
    while True:
        print("\n"+"="*30)
        print("1. View Settings")
        print("2. Add Setting")
        print("3. Update Setting")
        print("4. Delete Setting")
        print("5. Exit")
        print("="*30)

        select = input("Please enter the available number : ")

        print("="*30)

        if select == '1':
            print(view_settings(test_settings))
        elif select == '2':
            input_key = input('Input setting name : ')
            input_value = input('Input value name : ')
            result = add_setting(test_settings,(input_key,input_value))
            print(result)
        elif select == '3':
            input_key = input('Input setting name that will be updated : ')
            input_value = input('Input value that will be updated : ')
            result = update_setting(test_settings,(input_key,input_value))
            print(result)
        elif select == '4':
            input_key = input('Input setting name that you want to be deleted : ')
            result = delete_setting(test_settings,input_key)
        elif select == '5':
            print('Thanks for using this program. See you next time!')
            break
        else:
            print('Invalid input')