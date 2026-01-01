# 📑 Gemini Invoice Expert: AI Data Extractor

A specialized Multi-modal application that transforms invoices into searchable data. Using Google Gemini 2.5 Flash, this tool acts as an expert document analyzer to extract dates, line items, totals, and tax information from uploaded invoice images.

![UI](/images/image1.png)

## Features

* **🔍 Precision Extraction:** Specifically tuned via system prompting to act as an expert in financial documents.
* **📂 Multiple Format Support:** Process invoices in JPG, JPEG, and PNG formats.
* **💬 Natural Language Queries:** Ask specific questions like "What is the total GST?" or "Who is the vendor?" instead of just getting a generic summary.
* **🖼️ Visual Confirmation:** Displays the uploaded document within the app to ensure clarity.
* **🤖 Advanced AI:** Leverages the high-speed reasoning of the gemini-2.5-flash model.

![Working](/images/image2.png)
![Result](/images/image3.png)

## Works with different Languages

![Hindi](/images/image4.png)
![Hindi](/images/image5.png)

## Skills Showcased

* **Python** Core programming language
* **Streamlit**	Frontend framework for the web interface
* **Google GenAI** Accessing the gemini-2.5-flash model
* **Python-Dotenv** Secure management of API keys
* **Image Processing**	Pillow (PIL)
* **Prompt Engineering** Learned the art of System Prompting to guide AI behavior (forcing the AI to act as an "Invoice Expert")
* **Multimodal Data Handling:** Developed logic to process and send both text and binary image data (PIL objects) to Large Language Models

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

**1. Clone the Repository** 

    git clone <your-repository-url>
    cd <your-project-folder>
**2. Install Dependencies**

    pip install -r requirements.txt

**3. Set Up Your API Key**

    Get an API key from Google AI Studio.
    Create a file named .env in your project root.
    Add your key to the file:
    Code snippet
    GOOGLE_API_KEY=your_secret_api_key_here

**4. Run the App**

    streamlit run your_filename.py

## Conclusion

The Invoice Information Extractor demonstrates the practical application of Multimodal LLMs in automating document workflows. By combining visual perception with specialized system instructions, this project successfully bridges the gap between unstructured image data and actionable business insights.