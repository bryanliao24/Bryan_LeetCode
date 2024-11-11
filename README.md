### Use pip to install the necessary libraries:
`pip install -r requirements.txt`

### Fireworks API Setup
Make sure to obtain an API key from Fireworks AI. This key will be used to authorize API calls.

### Live Server for Frontend
Open index.html in a Live Server (such as the Live Server extension in Visual Studio Code) to view the frontend.

### KYC_Processing/code/
│
├── app.py               # Main file to handle API requests
├── prompts.py           # Stores different prompt templates
├── extract_data.py      # Handles calls to Fireworks AI API
├── validate_data.py     # Logic for data validation
└── requirements.txt     # Dependencies required for the project
└── index.html           # Frontend for document upload and processing

### Start the Application
To run the application, use the following command and pass in your API key:
`python app.py --apiKey YOUR_FIREWORKS_API_KEY`
This will start a Flask server on localhost:5000.

### Open the Frontend
Open index.html in a Live Server to interact with the application.
