# TrackCheck

In this project apply only CRUD method for ```Company``` model 

#### Used Technologies 
- FastApi
- SQLAlchemy
- Alembic
- PostgresSQL

#### Installation
1. Clone the repository:
    ```bash 
    git clone https://github.com/g1Den1s-it/TrackCheck.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Build and run the PostgresSQl container: 
    ```bash
    docker compose build
    ```
    ```bash
    docker compose up
    ```
4. Set up the database:
    ```bash
    alembic upgrade head
    ```
5. Run the application:
    ```bash
    python main.py
    ```