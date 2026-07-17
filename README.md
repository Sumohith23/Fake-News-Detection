# Fake-News-Detection
This Python script sets up a web application called the "Fake News Detector" using Streamlit and Google's Gemini API.  
Here is a breakdown of how the code works:

Application Overview:
Purpose: The application acts as a tool to evaluate the authenticity of news articles by leveraging an AI model to act as an expert fact-checker. 
Frameworks Used: It uses streamlit for the front-end user interface and google.generativeai to connect to Google's AI models.  

Key Components:

Setup and Authentication:
The script uses dotenv to securely load environment variables.  
It retrieves the GEMINI_API_KEY from the environment to configure the AI model.  
If the API key is not found, it halts the app and displays an error message to the user. 

Model Initialization:

It initializes the gemini-2.5-flash model, which handles the text analysis.

User Interface (UI):
It configures the Streamlit page with a specific title ("Fake News Detector") and a newspaper emoji icon ("📰").  
It creates a large text input box (st.text_area) with a height of 250 pixels where users can paste the news article they want to analyze.

Analysis Logic:
The analysis is triggered when the user clicks the "Analyze News" button.  
It first checks if the text area is empty, issuing a warning if no text was provided.  
If text is present, it constructs a specific prompt instructing the AI to act as an "expert fact checker".

Requested AI Output:
The prompt asks the AI to analyze the text and return a cleanly formatted response containing five specific elements:
A Verdict (categorized as Real, Fake, or Uncertain).  
A Confidence Score formatted as a percentage (0-100%).  
The Reasons behind its conclusion.  A detailed Explanation.  
Suggested Sources for the user to manually verify the claims.

Execution and Error Handling:
While the AI processes the request, the app displays a loading spinner reading "Analyzing...".  
If successful, it prints a success message and outputs the AI's generated text directly to the webpage.  
If the API call fails, it catches the exception and displays the specific error to the user
