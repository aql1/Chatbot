# Chatbot Application

This is a chatbot application built with **Streamlit**, **LangChain**, and **OpenAI** that interacts with CSV files uploaded by the user. The chatbot supports multilingual inputs (e.g., English and Arabic) and provides context-aware responses based on the uploaded file.

---

## Features

- Upload a CSV file for dynamic interaction.
- Language detection for input (supports English and Arabic).
- Provides accurate and context-aware answers based on the CSV content.
- Handles errors gracefully with user-friendly feedback.

---

## Requirements

Ensure the following dependencies are installed in your Python environment:

- Python 3.10+
- Streamlit
- LangChain
- OpenAI
- python-dotenv
- langdetect

---

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Chatbot.git
   cd Chatbot
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   - Create a `.env` file in the root directory:
     ```plaintext
     OPENAI_API_KEY='your-openai-api-key-here'
     ```

5. **Run the Application:**

   ```bash
   streamlit run chatbot.py
   ```

---

## Usage

1. **Upload a CSV File:**

   - Open the Streamlit application in your browser.
   - Upload a CSV file via the interface.

2. **Interact with the Chatbot:**

   - Type your queries in the text input box.
   - Press "Enter" or click the "Send" button to submit your question.

3. **Receive Responses:**

   - The chatbot processes your input, analyzes the CSV file, and provides an appropriate response.

---

## File Structure

```
Chatbot/
├── chatbot.py         # Main application file
├── .env.example       # Example environment variables file
├── .gitignore         # Excluded files and directories
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation (this file)
```

---

## Notes

- Ensure your API key is securely stored in the `.env` file.
- The `venv` folder and `.env` file are excluded from version control using `.gitignore`.
- The chatbot gracefully handles errors, including unsupported operations or missing CSV files.

---

## Example CSV Interaction

Upload a CSV file with the following structure:

```csv
Name,Age,Location
John,30,New York
Jane,25,London
Ali,28,Dubai
```

### Example Interaction

- **User:** Who is the oldest?
- **AI:** John is the oldest at 30 years old.

---