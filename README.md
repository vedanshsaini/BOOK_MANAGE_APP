# BOOK_MANAGE_APP

Clone the repository: Clone the Git repository to your local machine using the git clone command.

-------git clone <repository-url>

Navigate to the project directory: Open your terminal or command prompt and change your current directory to the cloned project folder.

------cd book-manager

Create a virtual environment: Run the command to create a virtual environment inside the project folder.
------python -m venv venv

Activate the virtual environment: Activate the virtual environment based on your operating system.

-----venv\Scripts\activate

Install dependencies: Install the project dependencies using pip, as specified in the README.

----------pip install -r requirements.txt

Apply migrations: Apply database migrations to set up the database schema.


----------python manage.py migrate

Run the development server: Start the Django development server.

-----------python manage.py runserver
Access the application: Open your web browser and go to http://localhost:8000 to access the Book Manager application.
