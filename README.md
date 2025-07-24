<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Latest YouTube Video Embed</title>

  <!-- Responsive video styling -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f8fafc;
      color: #111827;
    }

    .video-wrapper {
      position: relative;
      padding-bottom: 56.25%; /* 16:9 aspect ratio */
      height: 0;
      overflow: hidden;
      max-width: 100%;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    .video-wrapper iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }

    .subscribe-btn {
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>

  <h2>📺 Latest from My YouTube Channel</h2>

  <!-- Latest video loads here -->
  <div class="video-wrapper" id="latestVideo"></div
