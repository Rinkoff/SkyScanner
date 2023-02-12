# SkyScanner

----------------------------------------------------------------------------------------------------------------------
## What is SkyScanner 
This is a Crawler/Scraper that crawl and collect data from website that
serves us to find cheap airline tickets departing from Bulgaria.
----------------------------------------------------------------------------------------------------------------------
### How to use SkyScanner
 1. Clone project:
    ` git clone https://github.com/Rinkoff/SkyScanner.git`
 2. Install the necessary dependencies:
    ```
    cd SkyScanner
    
    #Create your virtual environment for the project
    python -m venv .venv
    
    #Activate your virtual envinronment(Example:For Windows)
    .\.venv\Scripts\activate.bat
    
    #Install requirments
    pip install -r requirements.txt
    ```

 3. Create your own database and import it into the file directory:
   ` mysql -u root -p skyscannerdb < skyscannerdb.sql`

 4. Run SkyScanner.
    `python SkyScanner.py`