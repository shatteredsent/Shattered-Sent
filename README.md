<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Shattered Sent | Healing Through Redemption</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    :root {
      --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
      --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #4a6741 100%);
      --text-primary: #1a202c;
      --text-secondary: #4a5568;
      --text-light: #718096;
      --surface-white: #ffffff;
      --surface-gray: #f7fafc;
      --border-light: #e2e8f0;
      --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--surface-gray);
      color: var(--text-primary);
      line-height: 1.6;
      margin: 0;
      padding: 0;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* Animated background particles */
    .bg-animation {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
      overflow: hidden;
    }

    .particle {
      position: absolute;
      width: 4px;
      height: 4px;
      background: rgba(102, 126, 234, 0.3);
      border-radius: 50%;
      animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.7; }
      50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
    }

    /* Header styles */
    header {
      background: var(--primary-gradient);
      color: white;
      padding: 4rem 2rem 6rem;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
    }

    header::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.2"/><circle cx="20" cy="80" r="0.5" fill="white" opacity="0.2"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
      pointer-events: none;
    }

    .header-content {
      position: relative;
      z-index: 2;
      max-width: 1200px;
      margin: 0 auto;
    }

    header h1 {
      font-size: clamp(2.5rem, 5vw, 4rem);
      font-weight: 700;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
      animation: fadeInUp 1s ease-out;
    }

    .tagline {
      font-size: clamp(1.1rem, 2.5vw, 1.5rem);
      font-weight: 300;
      opacity: 0.95;
      margin-bottom: 2rem;
      animation: fadeInUp 1s ease-out 0.2s both;
    }

    .header-description {
      max-width: 600px;
      margin: 0 auto;
      font-size: 1.1rem;
      opacity: 0.9;
      line-height: 1.7;
      animation: fadeInUp 1s ease-out 0.4s both;
    }

    /* Main content */
    main {
      max-width: 1200px;
      width: 100%;
      margin: -3rem auto 0;
      padding: 0 2rem 4rem;
      position: relative;
      z-index: 3;
    }

    /* Video section */
    .video-section {
      background: var(--surface-white);
      border-radius: 24px;
      padding: 3rem;
      box-shadow: var(--shadow-xl);
      margin-bottom: 3rem;
      border: 1px solid var(--border-light);
      animation: fadeInUp 1s ease-out 0.6s both;
    }

    .section-header {
      text-align: center;
      margin-bottom: 2.5rem;
    }

    .section-title {
      font-size: 2rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 0.5rem;
      position: relative;
      display: inline-block;
    }

    .section-title::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 50%;
      transform: translateX(-50%);
      width: 60px;
      height: 3px;
      background: var(--secondary-gradient);
      border-radius: 2px;
    }

    .section-subtitle {
      color: var(--text-secondary);
      font-size: 1.1rem;
      font-weight: 400;
    }

    .video-wrapper {
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
      border-radius: 16px;
      box-shadow: var(--shadow-lg);
      margin-bottom: 2rem;
      background: linear-gradient(45deg, #f0f2f5, #e2e8f0);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .video-wrapper:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-xl);
    }

    .video-wrapper iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
      border-radius: 16px;
    }

    .loading-placeholder {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      color: var(--text-secondary);
    }

    .loading-spinner {
      width: 40px;
      height: 40px;
      border: 3px solid var(--border-light);
      border-top: 3px solid #667eea;
      border-radius: 50%;
      animation: spin 1s linear infinite;
      margin: 0 auto 1rem;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    /* Subscribe section */
    .subscribe-section {
      text-align: center;
      padding: 2rem;
      background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
      border-radius: 16px;
      border: 1px solid rgba(102, 126, 234, 0.1);
    }

    .subscribe-title {
      font-size: 1.5rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 1rem;
    }

    .subscribe-description {
      color: var(--text-secondary);
      margin-bottom: 2rem;
      font-size: 1.1rem;
    }

    /* Call-to-action section */
    .cta-section {
      background: var(--dark-gradient);
      color: white;
      padding: 4rem 3rem;
      border-radius: 24px;
      text-align: center;
      margin-bottom: 3rem;
      position: relative;
      overflow: hidden;
      animation: fadeInUp 1s ease-out 0.8s both;
    }

    .cta-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="stars" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="0.5" fill="white" opacity="0.3"/></pattern></defs><rect width="100" height="100" fill="url(%23stars)"/></svg>');
      pointer-events: none;
    }

    .cta-content {
      position: relative;
      z-index: 2;
    }

    .cta-title {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .cta-description {
      font-size: 1.2rem;
      opacity: 0.9;
      max-width: 600px;
      margin: 0 auto 2rem;
      line-height: 1.7;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 3rem 2rem;
      color: var(--text-light);
      background: var(--surface-white);
      border-top: 1px solid var(--border-light);
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
    }

    .footer-brand {
      font-size: 1.5rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 1rem;
    }

    .footer-tagline {
      font-size: 1rem;
      margin-bottom: 2rem;
      color: var(--text-secondary);
    }

    .copyright {
      font-size: 0.9rem;
      opacity: 0.8;
    }

    /* Animations */
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Responsive design */
    @media (max-width: 768px) {
      header {
        padding: 3rem 1rem 4rem;
      }

      main {
        padding: 0 1rem 3rem;
        margin-top: -2rem;
      }

      .video-section,
      .cta-section {
        padding: 2rem 1.5rem;
        border-radius: 16px;
      }

      .section-title {
        font-size: 1.75rem;
      }

      .cta-title {
        font-size: 2rem;
      }
    }

    @media (max-width: 480px) {
      .video-section,
      .cta-section {
        padding: 1.5rem 1rem;
      }
    }

    /* Enhanced YouTube subscribe button styling */
    .youtube-subscribe {
      display: inline-block;
      background: #ff0000;
      color: white;
      padding: 12px 24px;
      border-radius: 24px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1rem;
      transition: all 0.3s ease;
      box-shadow: var(--shadow-md);
    }

    .youtube-subscribe:hover {
      background: #cc0000;
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
    }
  </style>
</head>
<body>
  <!-- Animated background -->
  <div class="bg-animation" id="bgAnimation"></div>

  <header>
    <div class="header-content">
      <h1>Shattered Sent</h1>
      <div class="tagline">Healing • Redemption • Hope</div>
      <p class="header-description">
        Join us on a journey of transformation and healing. Through authentic stories, 
        meaningful conversations, and unwavering hope, we explore the path from brokenness to wholeness.
      </p>
    </div>
  </header>

  <main>
    <section class="video-section">
      <div class="section-header">
        <h2 class="section-title">Latest Message</h2>
        <p class="section-subtitle">Watch our most recent video and be inspired</p>
      </div>
      
      <div class="video-wrapper" id="latestVideo">
        <div class="loading-placeholder">
          <div class="loading-spinner"></div>
          <p>Loading latest video...</p>
        </div>
      </div>

      <div class="subscribe-section">
        <h3 class="subscribe-title">Stay Connected</h3>
        <p class="subscribe-description">
          Subscribe to never miss a message of hope and healing
        </p>
        <div class="g-ytsubscribe"
             data-channelid="UCjhAWGLaxd124jxAdD_digQ"
             data-layout="default"
             data-count="default">
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="cta-content">
        <h2 class="cta-title">Your Story Matters</h2>
        <p class="cta-description">
          Every journey through darkness leads to light. Every broken piece can be made whole again. 
          You are not alone in your struggle, and your healing matters more than you know.
        </p>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-content">
      <div class="footer-brand">Shattered Sent</div>
      <div class="footer-tagline">Healing • Redemption • Hope</div>
      <div class="copyright">&copy; 2025 Shattered Sent. All rights reserved.</div>
    </div>
  </footer>

  <!-- YouTube Subscribe Button -->
  <script src="https://apis.google.com/js/platform.js"></script>
  
  <!-- Enhanced scripts -->
  <script>
    // Create animated background particles
    function createParticles() {
      const bgAnimation = document.getElementById('bgAnimation');
      const particleCount = 50;

      for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 6 + 's';
        particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
        bgAnimation.appendChild(particle);
      }
    }

    // Enhanced YouTube video loading
    const apiKey = 'AIzaSyBA0y6E7SltRstGwtSSX_X05Puran6YMUA';
    const channelId = 'UCjhAWGLaxd124jxAdD_digQ';
    
    async function loadLatestVideo() {
      try {
        const response = await fetch(`https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet&order=date&maxResults=1&type=video`);
        const data = await response.json();
        
        if (data.items && data.items.length > 0) {
          const videoId = data.items[0].id.videoId;
          const videoTitle = data.items[0].snippet.title;
          
          const iframe = `
            <iframe 
              src="https://www.youtube.com/embed/${videoId}" 
              title="${videoTitle}"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
            </iframe>`;
          
          document.getElementById('latestVideo').innerHTML = iframe;
        } else {
          throw new Error('No videos found');
        }
      } catch (error) {
        console.error('Error loading video:', error);
        document.getElementById('latestVideo').innerHTML = `
          <div class="loading-placeholder">
            <p style="color: #e53e3e;">⚠️ Unable to load the latest video</p>
            <p style="font-size: 0.9rem; margin-top: 0.5rem;">Please check back later or visit our YouTube channel directly.</p>
          </div>`;
      }
    }

    // Smooth scroll animations on scroll
    function handleScrollAnimations() {
      const elements = document.querySelectorAll('.video-section, .cta-section');
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
          }
        });
      }, {
        threshold: 0.1
      });

      elements.forEach(el => {
        observer.observe(el);
      });
    }

    // Initialize everything when page loads
    document.addEventListener('DOMContentLoaded', () => {
      createParticles();
      loadLatestVideo();
      handleScrollAnimations();
    });
  </script>
</body>
</html>
