🖼️ Python Flask Image Converter Suite

This project is a simple, web-based image converter application built using Python (Flask) for the backend processing and standard HTML/CSS/JavaScript for the frontend user interface. It provides a convenient, local tool for various common image file conversions.

✨ Features

The application supports the following one-click image conversions:

JPG to PNG

PNG to JPG

WEBP to PNG

BMP to PNG

PNG to PDF

⚠️ Note on Conversions

When converting JPG to PNG, the application adds transparency if the source image supports it (though JPG generally does not).

When converting PNG to JPG, any existing transparency will be lost, as JPG does not support transparent layers.

All frontend pages include a file size check, limiting uploads to 5MB to prevent slow processing.

💻 Technologies

Backend: Python (Flask)

Image Processing: Pillow (PIL)

Frontend: HTML, CSS, and vanilla JavaScript for file handling and API interaction.

🚀 Setup and Installation

Prerequisites

You must have Python 3.x installed on your system.

1. Clone the Repository

git clone <your-repo-link>
cd <your-repo-name>


2. Install Dependencies

The application relies on Flask for the web server and Pillow for image manipulation.

pip install Flask Pillow


3. Run the Server

Start the Flask development server by running the main application file (app.py).

python app.py


4. Access the Application

Once the server is running, open your web browser and navigate to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)


The home page (index.html) will display a list of all available converters.

📂 Project Structure

The project is structured into logical files to separate the web server, APIs, and the client-side interfaces.

.
├── app.py              # Main Flask server and API endpoints (Python)
├── index.html          # Homepage with links to all converters
├── jpgtopng.html       # Frontend for JPG -> PNG conversion
├── pngtojpg.html       # Frontend for PNG -> JPG conversion
├── webptopng.html      # Frontend for WEBP -> PNG conversion
├── bmptopng.html       # Frontend for BMP -> PNG conversion
└── pngtopdf.html       # Frontend for PNG -> PDF conversion
