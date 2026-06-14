<h1 align="center">Universal Web Table Scraper</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Pandas-3.0.3-red?logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Rich-15.0.0-blueviolet?logo=pandas" alt="Rich">
  <img src="https://img.shields.io/badge/BeautifulSoup-4.15.0-blue?logo=bs" alt="BeautifulSoup">
  <img src="https://img.shields.io/badge/Requests-2.34.2-75c2aa?logo=bs" alt="Requests">
</p>

A lightning-fast, zero-configuration CLI tool designed to extract tabular data from any website and instantly convert it into Machine Learning-ready CSV datasets. 

Whether you are building a custom neural network, fine-tuning an LLM, or performing exploratory data analysis, this tool eliminates the headache of manual web scraping and data sanitation.

---

## What This Tool Does
The Universal Web Table Scraper takes any standard web URL, scans the page for structured data tables, and downloads them directly to your computer. It bypasses messy web formatting, ignores hidden layout grids, and automatically generates clean, isolated CSV files for every valid dataset found on the page.

## Why is this useful for Machine Learning?
Raw web data is notoriously hostile to ML algorithms. This tool acts as the perfect Step 1 in your Data Engineering pipeline by outputting data that is heavily optimized for Scikit-Learn, PyTorch, and TensorFlow workflows:
* **Footnote Erasure:** Web tables often contain bracketed footnotes (e.g., `1,450 [a]` or `Mercury [12]`). This tool automatically detects and strips web-artifacts, leaving pure strings and integers.
* **Strict Grid Enforcement:** Missing columns and duplicated headers are automatically handled, preventing mathematical index crashing when loading the data into a Pandas DataFrame.
* **Ready for Encoding:** Because the text is sanitized at extraction, the resulting CSVs can be immediately fed into Label Encoders or One-Hot Encoders to generate binary matrices for neural networks.

## The CSV Output Format
Extracted tables are saved directly to a `csv_files` folder automatically generated on your **Desktop**. 

Each table is saved as a uniquely indexed file (e.g., `Target_Webpage_Title_table_1.csv`). The CSVs retain the exact header structure of the original webpage, with all rows cleanly aligned.

**Example Output:**
```csv
Planet Name,Mass (10^24kg),Diameter (km),Gravity (m/s^2),Moons
Mercury,0.330,4879,3.7,0
Venus,4.87,12104,8.9,0
Earth,5.97,12756,9.8,1
```

---

## Installation & Usage

This tool is designed to fit your exact workflow. Choose the installation method that best suits your technical convenience.

### Method 1: The Global CLI Command (For Developers)
*Best if you want to use the scraper constantly from any terminal on your computer.*

1. Clone this repository to your machine.
2. Open your terminal inside the downloaded folder.
3. Install the package globally in editable mode:
   ```bash
   pip install -e .
   ```
4. **Usage:** You can now close that terminal. Open a new terminal *anywhere* on your computer and simply type:
   ```bash
   run-scraper
   ```

### Method 2: The Standalone Executable (No Python Required)
*Best if you do not have a Python environment set up, or want to share the tool with non-technical team members.*

1. Navigate to the **Releases** tab on this GitHub repository.
2. Download the `UniversalTableScraper.exe` file.
3. **Usage:** Double-click the `.exe` file. A native terminal UI will open automatically, prompt you for a URL, and save the CSVs directly to your Desktop.

### Method 3: The Raw Python Script (For Tinkerers)
*Best if you want to read, modify, or extend the Python code yourself.*

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Usage:** Run the entry-point script directly from your terminal:
   ```bash
   python run.py
   ```

---

## UI Experience
The CLI features a rich, responsive terminal interface. It provides animated loading spinners during network requests, color-coded success/failure logs, and explicit file-path routing so you always know exactly where your data is being saved.
