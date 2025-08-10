# News Aggregator Web Application

## Project Description
The News Aggregator web application is a dynamic platform built with Python and Flask. It collects and displays news articles from multiple RSS feeds, including BBC News, CNN, Reuters, and The New York Times. The app provides advanced filtering options so that users can narrow down articles by news source and category, and search for articles using keywords. Searches are performed in a case-insensitive manner, ensuring that results are accurate regardless of text casing.

Real-time updates are achieved through AJAX, refreshing the news feed automatically every 30 seconds without requiring a page reload. Articles are sorted by publication date, meaning the latest news appears at the top. The modern, responsive user interface is designed with Bootstrap 5 and enhanced by custom CSS animations, making it appealing and easy to use on desktops, tablets, and mobile devices.

This project is intended to serve as both a practical news aggregation tool and a learning resource for web development. It demonstrates how to integrate RSS feeds, implement dynamic filtering and search, and create a responsive UI with real-time capabilities.

## Features
- **RSS Feed Aggregation:** Collects articles from multiple sources.
- **Filtering:** Filter news by source and category.
- **Search Functionality:** Case-insensitive search within article titles and summaries.
- **Real-time Updates:** Automatically refreshes news feed every 30 seconds via AJAX.
- **Date Sorting:** Displays the newest articles first.
- **Modern Design:** Responsive UI with Bootstrap 5 and custom CSS animations.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bektas-sari/news-aggregator.git
   ```
2. **Change to the Project Directory:**
   ```bash
   cd news-aggregator
   ```
3. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Application:**
   ```bash
   python app.py
   ```
6. **Visit:** [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 👤 Developer

**Bektas Sari**  
Email: bektas.sari@gmail.com  <br>
GitHub: https://github.com/bektas-sari <br>
LinkedIn: www.linkedin.com/in/bektas-sari <br>
Researchgate: https://www.researchgate.net/profile/Bektas-Sari-3 <br>
Academia: https://independent.academia.edu/bektassari <br>

## License
This project is licensed under the MIT License.

