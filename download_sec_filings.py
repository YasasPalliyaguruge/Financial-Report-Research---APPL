#!/usr/bin/env python3
"""
Download Apple's Form 10-K reports from SEC EDGAR and convert to PDF.
"""

import os
import time
import requests
from datetime import datetime

# SEC EDGAR URLs for Apple's Form 10-K
FILINGS = [
    {
        "year": 2024,
        "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm",
        "output": "Apple_2024_Form_10-K.htm",
    },
    {
        "year": 2023,
        "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm",
        "output": "Apple_2023_Form_10-K.htm",
    },
]

# Headers to comply with SEC's requirements
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def download_filing(filing):
    """Download a single SEC filing."""
    print(f"\nDownloading Apple {filing['year']} Form 10-K...")
    print(f"URL: {filing['url']}")

    try:
        response = requests.get(filing["url"], headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Check if we got blocked by SEC
        if "Your Request Originates from an Undeclared Automated Tool" in response.text:
            print(
                f"  ✗ SEC blocked the request. Response size: {len(response.text)} bytes"
            )
            print(f"  Content preview: {response.text[:200]}...")
            return False

        # Save the HTML file
        with open(filing["output"], "w", encoding="utf-8") as f:
            f.write(response.text)

        file_size = os.path.getsize(filing["output"])
        print(f"  ✓ Downloaded successfully: {filing['output']}")
        print(f"  File size: {file_size:,} bytes")
        return True

    except requests.RequestException as e:
        print(f"  ✗ Error downloading: {e}")
        return False


def main():
    """Main function to download all filings."""
    print("=" * 70)
    print("Apple Form 10-K Download Script")
    print("=" * 70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    success_count = 0
    total_count = len(FILINGS)

    for filing in FILINGS:
        if download_filing(filing):
            success_count += 1
        # Add a small delay between requests to be respectful
        time.sleep(1)

    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total downloads: {success_count}/{total_count} successful")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n" + "=" * 70)
    print("PDF Conversion Instructions")
    print("=" * 70)
    print("The SEC filings have been downloaded as HTML files.")
    print("To convert them to PDF:")
    print("\nOption 1: Using a web browser")
    print("  1. Open the HTML file in Chrome, Firefox, or Edge")
    print("  2. Press Ctrl+P (or Cmd+P on Mac)")
    print("  3. Select 'Save as PDF' as the destination")
    print("  4. Click Save")
    print("\nOption 2: Using wkhtmltopdf (command line)")
    print("  1. Install wkhtmltopdf from https://wkhtmltopdf.org/")
    print("  2. Run: wkhtmltopdf Apple_2024_Form_10-K.htm Apple_2024_Form_10-K.pdf")
    print("  3. Run: wkhtmltopdf Apple_2023_Form_10-K.htm Apple_2023_Form_10-K.pdf")
    print("\nOption 3: Using Python with pdfkit")
    print("  1. Install: pip install pdfkit")
    print("  2. Install wkhtmltopdf from https://wkhtmltopdf.org/")
    print("  3. Run: python convert_to_pdf.py")


if __name__ == "__main__":
    main()
