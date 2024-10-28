# Mashup Song Downloader

**Mashup** is a web application that allows users to create a mashup of multiple songs by downloading videos from YouTube. The app is built using React for the front end, with the backend processing handled by a server that communicates with YouTube's API to fetch and download videos.

## Features

- User-friendly interface to input the name of a singer and the number of videos.
- Downloads videos from YouTube using the backend service.
- Provides real-time feedback on the downloading process.
- Sends results to the entered mail after processing is complete.

## Tech Stack

- **Front-end:** React, Tailwind CSS
- **Back-end:** Node.js, Express.js
- **YouTube Downloading:** YouTube API, `youtube-dl`

## Python Libraries

The Python script in this project uses the following key libraries:

### 1. `pydub`

- **Purpose:** This library is used for audio manipulation and processing.
- **Installation:** 
  ```bash
  pip install pydub
  ```

### 2. `yt-dlp`

- **Purpose:** A powerful YouTube downloader, `yt-dlp` allows downloading videos or extracting audio from YouTube and other video platforms.
- **Installation:**
  ```bash
  pip install yt-dlp
  ```

### 3. `yagmail`

- **Purpose:** A simple library for sending emails via Gmail.
- **Installation:**
  ```bash
  pip install yagmail
  ```

### Environment Variables for `yagmail`

To avoid hardcoding email credentials in the Python script, use environment variables or `.env` files. Here's an example of how to set up your Gmail credentials:

```bash
export EMAIL_USER="your_email@gmail.com"
export EMAIL_PASS="your_password"
```

## Installation

### Prerequisites

- [Node.js](https://nodejs.org/) (version 14.x or later)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/) for package management

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sidharthd7/Mashup
   cd Mashup
   ```

2. **Install the dependencies:**

   For the client:
   ```bash
   cd client
   npm install
   ```

   For the server:
   ```bash
   cd server
   npm install
   ```

3. **Run the client:**
   ```bash
   cd client
   npm run dev
   ```

4. **Run the server:**
   ```bash
   cd server
   node server.js
   ```

5. **Open the app in your browser:**
   Navigate to [http://localhost:5173](http://localhost:5173) for the client-side interface.

## Usage

1. Enter the singer's name in the provided text box.
2. Enter the number of YouTube videos to be downloaded for the mashup.
3. Click the **Submit** button.
4. The app will display the downloading status in real time.
5. Once the process completes, the result will be shown on the screen.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

