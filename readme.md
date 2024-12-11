# Restaurant Idea Generator with LangChain and Streamlit

This project is a **Restaurant Idea Generator** built using LangChain and Streamlit. It helps you generate unique restaurant names and creative menu ideas for your desired cuisine. By leveraging the power of language models.

## Features

- **Generate Unique Restaurant Names**: Based on your selected cuisine.
- **Design Creative Menus**: Suggests a detailed menu in a list format.
- **Streamlit UI**: Simple and interactive web-based interface.

## Tech Stack

- **Python**: Core programming language.
- **LangChain**: Framework for building language model applications.
- **Streamlit**: Framework for creating the user interface.
- **GroqCloud**: LLM provider for generating ideas. (I'm using Llama3 latest)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Pip (Python package installer)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/muhammaduxair/restaurant-idea-generator-langchain.git
   cd restaurant-idea-generator-langchain
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add the following:
   ```env
   GROQ_API_KEY=your_groqcloud_api_key
   ```

5. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

6. **Open in Browser**:
   Streamlit will provide a URL (e.g., `http://localhost:8501`) to view the app.