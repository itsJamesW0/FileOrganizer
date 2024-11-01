Smart File Organizer

Smart File Organizer is a handy Python application that helps you automatically tidy up your files in a specific directory on your Mac. It sorts your files into categories like Images, Documents, Audio, Videos, and Archives, making it easier for you to find what you need.

Key Features

Automatic Sorting: It organizes your files based on their types.
App Management: Moves any application files directly to the /Applications folder.
Easy Organization: Creates separate folders for each category, keeping your Downloads folder neat and tidy.
How to Use It

Download the Script: Get the Smart File Organizer script from the repository.
Open the Script: Use your favorite text editor to open the script.
Set Your Directory: Find the line that specifies the directory you want to organize (like your Downloads folder) and replace the placeholder with the actual path where your files are located.
Run the Script: Save your changes and run the script using Python.
Important Notes

Make sure the directory you want to organize actually exists and has files in it.
This tool is perfect for keeping your Downloads folder organized without the hassle!

How to Automate the Smart File Organizer on Your Mac
1. Create the Organizer App:

Open Automator: Find Automator in your Applications folder or search for it using Spotlight (press Cmd + Space and type "Automator").
Select New Document: When prompted, choose Application as the type of document you want to create.
Add the Run Shell Script Action:
In the Automator window, look for Run Shell Script in the actions list on the left. Drag this action to the main workflow area on the right. Click on the drop
down box in the top right and ensure that you are passing inputs as arguements.
In the script box that appeared, replace the text (echo "$f") with the following command:
/usr/bin/python3 "/path/to/your/file_organizer.py" "$@"
Note: Replace "/path/to/your/file_organizer.py" with the actual path to where you've saved your Python script. Make sure the path is accurate.
Save the App: Go to File > Save and name it Organize Downloads.app. Save it in your Applications folder.

2. Set Up Folder Actions:

Open Your Downloads Folder: Use Finder to navigate to your Downloads folder.
Enable Folder Actions:
Right-click (or control-click) on the Downloads folder and choose Folder Actions Setup from the context menu.
Ensure the box labeled Enable Folder Actions is checked.
Attach Your App:
Click the Add button (the + icon) and select Organize Downloads.app from your Applications folder.
This will ensure that every time you add a new file to your Downloads folder, your organizer app runs automatically.

3. Test It Out:
Download a Test File: Try downloading any file to your Downloads folder to see if the organizer app sorts it correctly. If set up right, it should automatically organize your files into folders.

4. Run at Startup :

Add to Login Items: To ensure the organizer app runs automatically every time you start your computer:
Open System Preferences from the Apple menu.
Select Users & Groups.
Click on your user account and then navigate to the Login Items tab.
Drag Organize Downloads.app into this list to have it launch automatically when you log in.
This will ensure the program will run automatically even when you restart your computer
