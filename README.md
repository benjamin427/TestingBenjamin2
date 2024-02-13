This framework was developed to test the e-commerce website PHP Travels

Project setup:

Go to the Windows terminal to create a project folder
Type the command mkdir "name of your folder" press enter
Type the command to change directory to be in the created folder cd "name of your folder" press enter

Setting up virtual environment:

Once you're inside the folder on where the virtual environment will be located type the following for setup.
Type py -m venv "name you choose for the environment" press enter
Type "name of the environment"/Scripts/activate.bat press enter
After you have followed the previous steps, you should see an indicator of the name of the virtual environment on the command line

Creating a requirements file:

Type the command pip freeze > requirements.txt press enter.
Type requirements.txt to open the created file
After the created file is open, enter the following dependencies as the requirements 
  
Requirements

pytest==7.4.3
openpyxl==3.1.2
reports==0.4.1
selenium==4.16.0
pytest-html==4.1.1

After you save the requirements.txt file type the command pip install -r requirements.txt
You will see all the information of the tools that were previously saved being installed into the virtual environment.

To execute test in the project:
Open your IDE and select to view the terminal inside (or you can use the desktop terminal you already used).
Type the command to change the directory to be inside the virtual environment root folder
Next, type the command to change the directory to be inside the folder that will contain all of the test case files.
Type the command pytest "name of the file" press enter.
After entering the command, you will notice the pytest command will execute the file and display the information of the file being executed, and the end results after the execution is complete.

To execute report in the project:
Type the command pytest --html=report.html
After executing the comand, a report folder will be generated in the folder structure that will contain an html file.

