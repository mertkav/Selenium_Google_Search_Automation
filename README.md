#Python Selenium TEST on Google Search 

Note: I used [PyCharm IDE](https://www.jetbrains.com/pycharm/) as it's easy to import necessary libraries and has an isolated virtual environment.



### NOTES
If you're facing ChromeDriver issues, use the DriverManager library

## Step 2: Test displaying Test Results

Setup your test script as a unit test file by the following:
1. Structure test as a class with param as "unittest.TestCase"
2. Create a setup and teardown method for your driver
    - annotate it with @classmethod 
3. Insert your webdriver script into the method
4. Go to "Run" > "Edit Configurations", then add your test file as a "Python Test"
    - make sure the target file is the class file you just created
5. When you right-click your python test file, you can click "Run" and it will run as unit tests


 
## Step 3: Implement Page Object Model

Page Object Model makes it easier to: 
1. Build automation scripts quickly. If someone defined the page object and methods already, you can use it.
2. More developer friendly. It's easier to understand the test behavior at a higher level
3. Easier maintain so if several page objects change, you can edit it quickly



- POM Model includes the Pages, Tests and Locators files.
  - Utils.Locators include the Locators that we require to use.
  - Pages file includes Search and Results. 
  - Tests file includes the unittest of the Search and Results documents.



