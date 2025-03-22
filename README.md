# AI Web Scraper

An intelligent web scraping solution that combines the power of AI with web scraping capabilities to extract and analyze data from websites. This project uses Ollama for AI processing, Selenium for web automation, and Beautiful Soup for HTML parsing. What sets this scraper apart is its smart CAPTCHA bypassing capabilities and IP blocking prevention mechanisms, making it highly efficient for scraping protected websites while maintaining ethical browsing practices and ensuring continuous data collection without interruptions.

## 📌 Features

- AI-powered web scraping using Ollama
- Intelligent CAPTCHA bypassing mechanism
- Advanced IP blocking prevention system
- Smart request rate limiting and rotation
- Dynamic website handling with Selenium
- Intelligent data extraction and parsing
- Structured data output in table format
- Easy-to-use interface
- Efficient and reliable data collection from protected websites

## 🖼️ Demo & Output

### Web Interface

![Web Interface](./images/web_interface.png)
_The user-friendly interface where you can input any website URL and describe what data you want to extract_

### Scraping Process

![Scraping Process](./images/scraping_process.png)
_Terminal output showing the intelligent scraping process with automatic CAPTCHA detection and handling_

### Sample Output

![Sample Output](https://github.com/AkshaySingh2005/AI_Web_Scrapper/blob/main/Screenshot%202025-03-22%20123741.png)

_Example of structured data output - Property information organized in a clean, readable table format_

The scraper intelligently processes websites and generates structured table outputs, making it easy to analyze and process the scraped data. As shown in the example above, it can handle complex data like property listings, including details such as:

- Property specifications (BHK, Size)
- Price ranges
- Location details
- Builder information
- Registration numbers

## 🚀 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- Chrome browser
- Git

### Installing Ollama

1. **Windows Installation (WSL2 Required)**:

   - First, install WSL2 if you haven't already:
     ```bash
     wsl --install
     ```
   - Download and install Ollama for Windows:
     - Visit [Ollama's official website](https://ollama.ai/download)
     - Follow the Windows installation instructions
     - After installation, Ollama will be accessible through WSL2

2. **Linux Installation**:

   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

3. **MacOS Installation**:
   - Download the official Ollama package from [ollama.ai/download](https://ollama.ai/download)
   - Install the downloaded package
   - Launch Ollama from your Applications folder

After installing Ollama, pull the required model:

```bash
ollama pull mistral
```

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone [your-repository-url]
   cd ai_webScrapper
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your configuration:
   ```
   OLLAMA_BASE_URL=http://localhost:11434
   ```

## 💻 Usage

1. Make sure Ollama is running in the background
2. Run the main script:
   ```bash
   python main.py
   ```

## 🔧 Project Structure

- `main.py`: Entry point of the application
- `scrape.py`: Contains web scraping logic using Selenium
- `parse.py`: Handles data parsing and AI processing
- `requirements.txt`: Lists all Python dependencies
- `.env`: Configuration file for environment variables

## ⚠️ Important Notes

- Ensure Chrome WebDriver is compatible with your Chrome browser version
- The project requires an active internet connection
- Make sure Ollama is running before starting the application
- WSL2 is required for Windows users to run Ollama
- The tool implements responsible scraping practices to prevent IP blocks
- Recommended to use with a VPN or proxy service for additional protection

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](your-issues-url).

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ollama for providing the AI capabilities
- Selenium for web automation
- Beautiful Soup for HTML parsing
