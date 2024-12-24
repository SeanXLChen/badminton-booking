# Perfectmind Activities Booking Bot

Bot for automating activities bookings on NVRC's Perfectmind system. 

## Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

# Install requirements 
pip install -r requirements.txt

# Run the bot
python run.py
```

## Usage

1. Bot opens Chrome windows for monitoring court sessions
2. Log in manually when prompted
3. Press Enter to begin monitoring
4. Bot auto-refreshes and clicks "Book" when spots open


## Configuration

Edit URLs in run.py:

```python
URLS = "The URL of the activity you want to book"
```

## Requirements

- Python 3.x
- Selenium
- Chrome browser
- NVRC account
- Perfectmind account

## License

Copyright (c) 2024 Xiaolai Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.