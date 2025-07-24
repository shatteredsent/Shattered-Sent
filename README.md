<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Shattered Sent | Healing Through Redemption</title>

  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #f9fafb;
      color: #1f2937;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    header {
      background-color: #4f46e5; /* Indigo-600 */
      color: white;
      width: 100%;
      text-align: center;
      padding: 2rem 1rem;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    header h1 {
      margin: 0;
      font-size: 2rem;
    }

    main {
      max-width: 800px;
      width: 100%;
      padding: 2rem 1rem;
    }

    h2 {
      text-align: center;
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .video-wrapper {
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      margin-bottom: 1rem;
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
      margin: 1rem 0;
    }

    footer {
      text-align: center;
      font-size: 0.875rem;
      color: #6b7280;
      padding: 2rem 1rem;
    }
  </style>
</head>
<body>

  <header>
    <h1>Shattered Sent</h1>
    <p>Healing. Redemption. Hope.</p>
  </header>

  <main>
    <h2>📺 Watch the Latest Video</h2>

    <div class="video-wrapper" id="latestVideo">
      <p>Loading latest video...</p>
    </div>

    <div class="subscribe-btn">
      <div class="g-ytsubscribe"
           data-channelid="UCjhAWGLaxd124jxAdD_digQ"
           data-layout="default"
           data-count="default">
      </div>
    </div>
  </main>

  <footer>
    &copy; 2025 Shattered Sent. All rights reserved.
  </footer>

  <!-- YouTube Subscribe Button -->
  <script src="https://apis.google.com/js/platform.js"></script>

  <!-- Latest YouTube video script -->
  <script>
    const apiKey = 'AIzaSyBA0y6E7SltRstGwtSSX_X05Puran6YMUA';
    const channelId = 'UCjhAWGLaxd124jxAdD_digQ';

    fetch(`https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet&order=date&maxResults=1&type=video`)
      .then(response => response.json())
      .then(data => {
        const videoId = data.items[0].id.videoId;
        const iframe = `
          <iframe 
            src="https://www.youtube.com/embed/${videoId}" 
            title="Latest Video"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
          </iframe>`;
        document.getElementById('latestVideo').innerHTML = iframe;
      })
      .catch(err => {
        console.error(err);
        document.getElementById('latestVideo').innerHTML = "<p>⚠️ Could not load the latest video.</p>";
      });
  </script>

</body>
</html>
