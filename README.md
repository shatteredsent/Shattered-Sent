<From Broken to Bold Faith>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shattered & Sent</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for icons (e.g., social media, back to top) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" xintegrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0V4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc; /* Light blue-gray background */
            scroll-behavior: smooth; /* Smooth scrolling for anchor links */
        }
        /* Custom scrollbar for a cleaner look */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1; /* Gray-300 */
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8; /* Gray-400 */
        }

        /* Keyframe for subtle pulse effect on button */
        @keyframes pulse-once {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        .animate-pulse-once:hover {
            animation: pulse-once 0.5s ease-in-out;
        }

        /* Styling for the Back to Top button */
        #backToTopBtn {
            display: none; /* Hidden by default */
            position: fixed; /* Fixed position */
            bottom: 20px; /* Place at the bottom */
            right: 20px; /* Place at the right */
            z-index: 99; /* Ensure it's above other content */
            background-color: #4f46e5; /* Indigo-600 */
            color: white;
            border: none;
            border-radius: 50%; /* Circular button */
            width: 50px;
            height: 50px;
            font-size: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, transform 0.3s;
        }

        #backToTopBtn:hover {
            background-color: #4338ca; /* Indigo-700 */
            transform: translateY(-3px);
        }
    </style>
</head>
<body class="text-gray-800">
    <!-- Header Section -->
    <header class="bg-white shadow-md py-4 px-6 md:px-12 flex flex-col md:flex-row justify-between items-center rounded-b-xl sticky top-0 z-50">
        <div class="text-3xl font-bold text-indigo-700 mb-4 md:mb-0">Shattered & Sent</div>
        <nav>
            <ul class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-8">
                <li><a href="#home" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Home</a></li>
                <li><a href="#about" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">About</a></li>
                <li><a href="#content" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Content</a></li>
                <li><a href="#resources" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Resources</a></li>
                <li><a href="#contact" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="relative text-white py-24 px-6 md:px-12 flex items-center justify-center min-h-[500px] rounded-b-xl shadow-lg mt-4 mx-4 md:mx-auto max-w-7xl overflow-hidden">
        <!-- Background Image from Banner.jpg -->
        <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('Banner.jpg');"></div>
        <!-- Gradient Overlay for better text readability -->
        <div class="absolute inset-0 bg-gradient-to-r from-indigo-800 to-purple-900 opacity-80"></div>

        <div class="relative z-10 text-center">
            <h1 class="text-5xl md:text-6xl font-extrabold leading-tight mb-4 drop-shadow-lg">
                Shattered & Sent
            </h1>
            <p class="text-xl md:text-2xl mb-8 max-w-3xl mx-auto opacity-90 font-medium">
                From Brokenness to Bold Faith
            </p>
            <a href="#content" class="inline-block bg-white text-indigo-700 hover:bg-gray-100 px-8 py-4 rounded-full text-lg font-semibold shadow-xl transform hover:scale-105 animate-pulse-once transition duration-300 ease-in-out">
                Explore Content
            </a>
        </div>
    </section>

    <!-- Content Section -->
    <section id="content" class="py-16 px-6 md:px-12 bg-white rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl">
        <h2 class="text-4xl font-bold text-center text-indigo-700 mb-12">Our Latest Content</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Content Card 1 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/94a3b8/ffffff?text=Blog+Post" alt="Blog Post Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">The Power of Forgiveness</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Dive deep into the liberating power of forgiveness, understanding its biblical foundations and practical application in daily life. Learn how letting go can transform your heart and relationships.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Read More
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Content Card 2 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/a78bfa/ffffff?text=Sermon" alt="Sermon Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Sermon: Living a Sent Life</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Explore what it means to be "sent" by God into the world. This sermon challenges us to embrace our unique calling and serve others with love and compassion, reflecting Christ's light.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Listen Now
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Content Card 3 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/c7d2fe/ffffff?text=Testimony" alt="Testimony Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Testimony: From Brokenness to Hope</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Read a powerful personal testimony of how God's grace can heal brokenness and bring profound hope. This story highlights the journey of faith and divine restoration.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Read Story
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Resources Section -->
    <section id="resources" class="py-16 px-6 md:px-12 bg-indigo-50 rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl">
        <h2 class="text-4xl font-bold text-center text-indigo-700 mb-12">Featured Resources</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Resource Card 1 -->
            <div class="bg-white rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/b7e4c7/ffffff?text=E-Book" alt="E-Book Cover" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">E-Book: Journey Through John</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        A devotional guide exploring the Gospel of John, designed to deepen your understanding of Jesus' life and teachings. Perfect for personal study or small groups.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Download Now
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Resource Card 2 -->
            <div class="bg-white rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/90e0ef/ffffff?text=Podcast" alt="Podcast Thumbnail" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Podcast: Faith in Action Series</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Listen to our latest podcast series discussing practical ways to live out your faith in everyday situations, tackling common challenges with biblical wisdom.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Listen Here
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Resource Card 3 -->
            <div class="bg-white rounded-xl shadow-md overflow-hidden transform hover:scale-105 hover:shadow-lg transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/ffc300/ffffff?text=Study+Guide" alt="Study Guide Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Study Guide: Overcoming Adversity</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        A comprehensive study guide offering biblical perspectives and practical steps for navigating life's challenges and finding strength in God's promises.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Get Guide
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-16 px-6 md:px-12 bg-white rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl">
        <h2 class="text-4xl font-bold text-center text-indigo-700 mb-12">About Shattered & Sent</h2>
        <div class="max-w-4xl mx-auto text-center">
            <p class="text-lg text-gray-700 mb-6 leading-relaxed">
                "Shattered & Sent" is a ministry dedicated to sharing the transformative power of God's love and grace. We believe that even in our brokenness, God can use us for His glorious purposes. Our aim is to provide biblical insights, heartfelt testimonies, and practical wisdom to encourage believers on their spiritual journey.
            </p>
            <p class="text-lg text-gray-700 leading-relaxed">
                Through various forms of content, we seek to inspire, equip, and empower individuals to live out their faith boldly, reflecting Christ's light in every sphere of influence. Join us as we explore what it means to be both "shattered" by life's experiences and "sent" with a divine mission.
            </p>
        </div>
    </section>

    <!-- Call to Action Section -->
    <section class="py-16 px-6 md:px-12 bg-gradient-to-br from-purple-700 to-indigo-800 text-white rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl text-center">
        <h2 class="text-4xl font-bold mb-6 drop-shadow-md">Join Our Community!</h2>
        <p class="text-xl mb-8 max-w-2xl mx-auto opacity-90">
            Receive inspiring updates, new content alerts, and exclusive resources directly to your inbox.
        </p>
        <a href="#contact" class="inline-block bg-white text-purple-700 hover:bg-gray-100 px-10 py-5 rounded-full text-xl font-semibold shadow-xl transform hover:scale-105 animate-pulse-once transition duration-300 ease-in-out">
            Sign Up for Our Newsletter
        </a>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-16 px-6 md:px-12 bg-white rounded-xl shadow-lg mt-8 mb-8 mx-4 md:mx-auto max-w-7xl">
        <h2 class="text-4xl font-bold text-center text-indigo-700 mb-12">Get in Touch</h2>
        <div class="max-w-2xl mx-auto">
            <form class="space-y-6">
                <div>
                    <label for="name" class="block text-lg font-medium text-gray-700 mb-2">Name</label>
                    <input type="text" id="name" name="name" class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 transition duration-200 ease-in-out" placeholder="Your Name">
                </div>
                <div>
                    <label for="email" class="block text-lg font-medium text-gray-700 mb-2">Email</label>
                    <input type="email" id="email" name="email" class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 transition duration-200 ease-in-out" placeholder="you@example.com">
                </div>
                <div>
                    <label for="message" class="block text-lg font-medium text-gray-700 mb-2">Message</label>
                    <textarea id="message" name="message" rows="6" class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 transition duration-200 ease-in-out" placeholder="Your message..."></textarea>
                </div>
                <div class="text-center">
                    <button type="submit" class="inline-block bg-indigo-600 text-white hover:bg-indigo-700 px-8 py-4 rounded-full text-lg font-semibold shadow-lg transform hover:scale-105 transition duration-300 ease-in-out">
                        Send Message
                    </button>
                </div>
            </form>
            <div class="mt-12 text-center text-gray-600">
                <p class="mb-2">You can also reach us at:</p>
                <p class="text-xl font-semibold text-indigo-700">shattered.sent@gmail.com</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="bg-gray-800 text-white py-8 px-6 md:px-12 text-center rounded-t-xl">
        <div class="mb-4">
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out"><i class="fab fa-facebook-f"></i> Facebook</a>
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out"><i class="fab fa-instagram"></i> Instagram</a>
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out"><i class="fab fa-youtube"></i> YouTube</a>
        </div>
        <p class="text-gray-400">&copy; 2025 Shattered & Sent. All rights reserved.</p>
    </footer>

    <!-- Back to Top Button -->
    <button id="backToTopBtn" title="Go to top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        // Get the button
        let backToTopBtn = document.getElementById("backToTopBtn");

        // When the user scrolls down 20px from the top of the document, show the button
        window.onscroll = function() {scrollFunction()};

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                backToTopBtn.style.display = "flex"; // Use flex to center icon
            } else {
                backToTopBtn.style.display = "none";
            }
        }

        // When the user clicks on the button, scroll to the top of the document
        backToTopBtn.addEventListener("click", function() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        });
    </script>
</body>
</html>
<script>
  // Get the button
  const backToTopBtn = document.getElementById("backToTopBtn");

  // Show/hide the button on scroll
  window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
      if (backToTopBtn.style.display !== "flex") {
        backToTopBtn.style.display = "flex";
        
        // Add pulse animation
        backToTopBtn.classList.add("animate-pulse-once");
        setTimeout(() => {
          backToTopBtn.classList.remove("animate-pulse-once");
        }, 500); // Matches animation duration
      }
    } else {
      backToTopBtn.style.display = "none";
    }
  };

  // Scroll to top on button click
  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
</script>

<!-- Load YouTube Platform Script (for Subscribe button) -->
<script src="https://apis.google.com/js/platform.js"></script>

<!-- Responsive Video Container -->
<div class="video-wrapper" id="latestVideo"></div>

<!-- Subscribe Button -->
<div class="subscribe-btn">
  <div class="g-ytsubscribe"
       data-channelid="UCjhAWGLaxd124jxAdD_digQ"
       data-layout="default"
       data-count="default">
  </div>
</div>

<!-- Load Latest Video via YouTube API -->
<script>
  const apiKey = 'AIzaSyBA0y6E7SltRstGwtSSX_X05Puran6YMUA';
  const channelId = 'UCjhAWGLaxd124jxAdD_digQ';

  fetch(`https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&part=snippet,id&order=date&maxResults=1`)
    .then(response => response.json())
    .then(data => {
      const videoId = data.items[0].id.videoId;
      const embedHtml = `
        <iframe 
          src="https://www.youtube.com/embed/${videoId}" 
          title="Latest YouTube Video"
          frameborder="0" 
          allowfullscreen>
        </iframe>`;
      document.getElementById('latestVideo').innerHTML = embedHtml;
    })
    .catch(error => {
      console.error('Error loading latest video:', error);
    });
</script>

<!-- Style for responsiveness and layout -->
<style>
  .video-wrapper {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
    max-width: 100%;
    margin-bottom: 20px;
  }

  .video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .subscribe-btn {
    text-align: center;
    margin-top: 10px;
  }
</style>
