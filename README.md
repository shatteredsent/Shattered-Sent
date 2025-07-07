<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shattered & Sent</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
</head>
<body class="text-gray-800">
    <!-- Header Section -->
    <header class="bg-white shadow-md py-4 px-6 md:px-12 flex flex-col md:flex-row justify-between items-center rounded-b-xl">
        <div class="text-3xl font-bold text-indigo-700 mb-4 md:mb-0">Shattered & Sent</div>
        <nav>
            <ul class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-8">
                <li><a href="#home" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Home</a></li>
                <li><a href="#about" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">About</a></li>
                <li><a href="#content" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Content</a></li>
                <li><a href="#contact" class="text-lg text-gray-700 hover:text-indigo-600 font-medium transition duration-300 ease-in-out">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="relative bg-gradient-to-r from-indigo-600 to-purple-700 text-white py-24 px-6 md:px-12 flex items-center justify-center min-h-[500px] rounded-b-xl shadow-lg mt-4 mx-4 md:mx-auto max-w-7xl">
        <div class="absolute inset-0 bg-cover bg-center opacity-20" style="background-image: url('https://placehold.co/1920x1080/6366F1/ffffff?text=Inspiration');"></div>
        <div class="relative z-10 text-center">
            <h1 class="text-5xl md:text-6xl font-extrabold leading-tight mb-6 drop-shadow-lg">
                Transformed by Grace, Empowered for Purpose
            </h1>
            <p class="text-xl md:text-2xl mb-8 max-w-3xl mx-auto opacity-90">
                Discover inspiring Christian content that speaks to the heart, encourages growth, and equips you to live out your faith.
            </p>
            <a href="#content" class="inline-block bg-white text-indigo-700 hover:bg-gray-100 px-8 py-4 rounded-full text-lg font-semibold shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
                Explore Content
            </a>
        </div>
    </section>

    <!-- Content Section -->
    <section id="content" class="py-16 px-6 md:px-12 bg-white rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl">
        <h2 class="text-4xl font-bold text-center text-indigo-700 mb-12">Our Latest Content</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Content Card 1 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/94a3b8/ffffff?text=Blog+Post" alt="Blog Post Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">The Power of Forgiveness</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Dive deep into the liberating power of forgiveness, understanding its biblical foundations and practical application in daily life. Learn how letting go can transform your heart and relationships.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Read More
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
            <!-- Content Card 2 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/a78bfa/ffffff?text=Sermon" alt="Sermon Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Sermon: Living a Sent Life</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Explore what it means to be "sent" by God into the world. This sermon challenges us to embrace our unique calling and serve others with love and compassion, reflecting Christ's light.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Listen Now
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
            <!-- Content Card 3 -->
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transform hover:scale-105 transition duration-300 ease-in-out">
                <img src="https://placehold.co/600x400/c7d2fe/ffffff?text=Testimony" alt="Testimony Image" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-2xl font-semibold text-indigo-600 mb-3">Testimony: From Brokenness to Hope</h3>
                    <p class="text-gray-700 mb-4 line-clamp-3">
                        Read a powerful personal testimony of how God's grace can heal brokenness and bring profound hope. This story highlights the journey of faith and divine restoration.
                    </p>
                    <a href="#" class="text-indigo-500 hover:text-indigo-700 font-medium flex items-center">
                        Read Story
                        <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-16 px-6 md:px-12 bg-indigo-50 rounded-xl shadow-lg mt-8 mx-4 md:mx-auto max-w-7xl">
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
                <p class="text-xl font-semibold text-indigo-700">info@shatteredandsent.org</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="bg-gray-800 text-white py-8 px-6 md:px-12 text-center rounded-t-xl">
        <div class="mb-4">
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out">Facebook</a>
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out">Instagram</a>
            <a href="#" class="text-gray-400 hover:text-white mx-3 transition duration-300 ease-in-out">YouTube</a>
        </div>
        <p class="text-gray-400">&copy; 2025 Shattered & Sent. All rights reserved.</p>
    </footer>
</body>
</html>
