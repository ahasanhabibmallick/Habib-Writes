import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth.models import User
from blogs.models import Category, Blog, Tag
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds the database with professional blog content'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # 1. Create Author if not exists
        author, created = User.objects.get_or_create(
            username='ahasan',
            defaults={'email': 'ahasan@example.com', 'is_staff': True, 'is_superuser': True}
        )
        if created:
            author.set_password('admin123')
            author.save()
            self.stdout.write(self.style.SUCCESS(f'Created author: {author.username}'))

        # 2. Define Categories
        categories_data = [
            "Sports", "Politics", "Technology", "Business", "Science", "Health",
            "Education", "Web Development", "Python & Django", "Tech Tips",
            "Coding Life", "Writing & Ideas"
        ]

        category_objs = {}
        for cat_name in categories_data:
            cat, _ = Category.objects.get_or_create(category_name=cat_name)
            category_objs[cat_name] = cat

        self.stdout.write(self.style.SUCCESS(f'Categories verified: {len(category_objs)}'))

        # 3. Define Tags
        tags_data = [
            "AI", "Python", "Django", "JavaScript", "Fitness", "Economy", "Strategy",
            "Learning", "Productivity", "Future", "Data", "Science", "Development",
            "Editorial", "Mindset"
        ]
        tag_objs = []
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name, defaults={'slug': slugify(tag_name)})
            tag_objs.append(tag)

        # 4. Article Content Data (Simplified templates for seeding)
        articles = [
            # TECHNOLOGY
            {
                "category": "Technology",
                "title": "How Artificial Intelligence Is Changing Everyday Technology",
                "content": """<h2>The Invisible Revolution</h2>
                <p>Artificial Intelligence (AI) is no longer a concept limited to science fiction novels or high-tech laboratories. It has seamlessly woven itself into the fabric of our daily lives, often operating behind the scenes to enhance convenience, efficiency, and personalization.</p>
                <h3>Smart Personal Assistants</h3>
                <p>From Siri and Alexa to Google Assistant, AI-powered voices help us manage our schedules, play music, and control smart home devices. These systems use natural language processing (NLP) to understand context and intent, becoming more accurate with every interaction.</p>
                <h3>Predictive Personalization</h3>
                <p>Platforms like Netflix, Spotify, and Amazon use sophisticated machine learning algorithms to analyze your past behavior and suggest what you might enjoy next. This predictive personalization has redefined consumer expectations in the digital economy.</p>
                <h3>Conclusion</h3>
                <p>As AI continues to evolve, the line between human and machine interaction will further blur, leading to even more intuitive technologies that anticipate our needs before we even express them.</p>""",
                "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=800&q=80"
            },
            {
                "category": "Technology",
                "title": "The Evolution of Cloud Computing",
                "content": """<h2>From Mainframes to the Edge</h2>
                <p>Cloud computing has revolutionized how businesses and individuals store and process data. What started as centralized mainframe computing has evolved into a global network of distributed servers.</p>
                <h3>The Rise of SaaS</h3>
                <p>Software as a Service (SaaS) changed the software industry by moving applications from local installs to browser-based access. Companies like Salesforce and Google led this charge.</p>
                <h3>Serverless and Beyond</h3>
                <p>The latest trend, serverless computing, allows developers to build and run applications without managing infrastructure. This increases agility and reduces costs significantly.</p>
                <h3>Future Outlook</h3>
                <p>With the advent of 5G and edge computing, the cloud is moving closer to the user, promising near-instant latency for next-generation applications.</p>""",
                "image": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=800&q=80"
            },
            # PYTHON & DJANGO
            {
                "category": "Python & Django",
                "title": "Django Architecture Explained: MVT Pattern",
                "content": """<h2>Understanding Model-View-Template</h2>
                <p>Django follows a unique architectural pattern known as MVT (Model-View-Template). While similar to the traditional MVC (Model-View-Controller), it has distinct characteristics that make Django development efficient.</p>
                <h3>1. The Model</h3>
                <p>The Model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing.</p>
                <h3>2. The View</h3>
                <p>In Django, the View is the logic layer. It receives web requests and returns web responses. It acts as the bridge between the Model and the Template.</p>
                <h3>3. The Template</h3>
                <p>The Template is the presentation layer. It defines how the data should be rendered in the browser using Django Template Language (DTL).</p>
                <h3>Why MVT?</h3>
                <p>This separation of concerns allows developers to work on different parts of the application simultaneously without interfering with each other's work.</p>""",
                "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=800&q=80"
            },
            # WEB DEVELOPMENT
            {
                "category": "Web Development",
                "title": "Frontend vs Backend Development: Which One Should You Choose?",
                "content": """<h2>The Great Divide</h2>
                <p>Choosing a path in web development can be daunting. Understanding the difference between frontend and backend is the first step toward a successful career.</p>
                <h3>Frontend: The Visuals</h3>
                <p>Frontend developers deal with what users see and interact with. They use HTML, CSS, and JavaScript to build responsive and intuitive user interfaces.</p>
                <h3>Backend: The Logic</h3>
                <p>Backend developers focus on the server-side logic, databases, and APIs. They ensure the frontend has the data it needs to function correctly.</p>
                <h3>Fullstack: The Best of Both Worlds</h3>
                <p>A fullstack developer is comfortable working on both sides, making them highly versatile in small teams and startups.</p>""",
                "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80"
            },
            # HEALTH
            {
                "category": "Health",
                "title": "Understanding the Role of Sleep in Everyday Health",
                "content": """<h2>The Foundation of Wellbeing</h2>
                <p>Sleep is often the first thing sacrificed in our busy modern lives, yet it is as essential as nutrition and exercise for our health.</p>
                <h3>Cognitive Function</h3>
                <p>During sleep, the brain clears out toxins and consolidates memories. Lack of sleep leads to poor concentration and increased irritability.</p>
                <h3>Physical Recovery</h3>
                <p>Sleep is when the body repairs tissues, builds bone and muscle, and strengthens the immune system.</p>
                <h3>Healthy Habits</h3>
                <p>Consistency is key. Try to go to bed and wake up at the same time every day, even on weekends, to regulate your internal clock.</p>""",
                "image": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=800&q=80"
            },
            # BUSINESS
            {
                "category": "Business",
                "title": "Why Data Matters in Business Decision Making",
                "content": """<h2>In God We Trust, All Others Must Bring Data</h2>
                <p>In the digital age, intuition alone is no longer enough to run a successful business. Data-driven decision making (DDDM) has become the standard for industry leaders.</p>
                <h3>Risk Mitigation</h3>
                <p>Data allows companies to identify patterns and predict future trends, significantly reducing the risks associated with new ventures.</p>
                <h3>Efficiency Gains</h3>
                <p>By analyzing operational data, businesses can identify bottlenecks and optimize processes to save time and money.</p>
                <h3>Customer Insights</h3>
                <p>Understanding customer behavior through data helps in creating targeted marketing campaigns and improving product-market fit.</p>""",
                "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"
            },
            # SCIENCE
            {
                "category": "Science",
                "title": "How Scientific Research Actually Works",
                "content": """<h2>Beyond the Lab Coat</h2>
                <p>Science is not just a collection of facts; it is a rigorous process of inquiry and verification designed to understand the natural world.</p>
                <h3>The Scientific Method</h3>
                <p>It starts with an observation, followed by a hypothesis, experimentation, and finally, a conclusion that is peer-reviewed by other experts.</p>
                <h3>The Importance of Peer Review</h3>
                <p>Peer review ensures that research is credible, unbiased, and follows ethical standards before it is published in scientific journals.</p>""",
                "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=800&q=80"
            },
            # SPORTS
            {
                "category": "Sports",
                "title": "How Modern Sports Analytics Is Changing the Game",
                "content": """<h2>The Moneyball Effect</h2>
                <p>Data analytics has moved from the back office to the sidelines, influencing every decision from player recruitment to in-game strategy.</p>
                <h3>Player Performance Tracking</h3>
                <p>Wearable technology tracks every movement, helping coaches optimize training loads and prevent injuries.</p>
                <h3>Strategic Shifts</h3>
                <p>In basketball, analytics led to the rise of the three-point shot. In soccer, it redefined how teams value possession and pressing.</p>""",
                "image": "https://images.unsplash.com/photo-1504450758481-7338eba7524a?auto=format&fit=crop&w=800&q=80"
            }
        ]

        # Extend articles to reach ~50 by duplicating with slight variations or unique titles
        # For brevity in this script, I will generate variations programmatically
        topics = {
            "Sports": ["Evolution of Fitness", "Fan Experience Tech", "Psychology of Performance", "Business of Sports"],
            "Politics": ["Democratic Institutions", "Elections and Media", "Public Policy Creation", "Digital Age Communication", "International Relations"],
            "Technology": ["Cybersecurity Challenges", "Consumer Tech Future", "Software in Industry", "Sustainable Tech"],
            "Business": ["Digital Economy Models", "Entrepreneurship Rise", "Competitive Advantage", "Corporate Culture"],
            "Science": ["Data in Science", "Climate Science Studies", "Science of Tech", "Scientific Literacy"],
            "Health": ["Nutrition Basics", "Exercise Benefits", "Stress Management", "Healthy Habits"],
            "Education": ["Online Education Future", "Critical Thinking", "Study Habits", "EdTech Impact"],
            "Web Development": ["API Understanding", "Scalable Apps", "CSS Grid & Flexbox", "JavaScript Frameworks"],
            "Python & Django": ["Why Python?", "First Django App", "Django Best Practices", "Testing in Python"],
            "Tech Tips": ["Productivity Hacks", "Browser Tips", "Dev Tools", "Folder Organization"],
            "Coding Life": ["Consistency Tips", "Handling Frustration", "Sustainable Routines", "Learning Paths"],
            "Writing & Ideas": ["Writing Habits", "Clear Thinking", "Knowledge Systems", "Creativity & Tech"]
        }

        image_keywords = {
            "Sports": "sports", "Politics": "government", "Technology": "technology",
            "Business": "business", "Science": "science", "Health": "health",
            "Education": "education", "Web Development": "code", "Python & Django": "python",
            "Tech Tips": "productivity", "Coding Life": "developer", "Writing & Ideas": "writing"
        }

        # Clear existing seeded blogs if needed?
        # Blog.objects.all().delete()

        # Clear existing seeded blogs to fix broken images
        Blog.objects.filter(author=author).delete()
        self.stdout.write('Cleared old seeded articles...')

        for cat_name, title_list in topics.items():
            cat = category_objs[cat_name]
            keyword = image_keywords[cat_name]

            for i, title in enumerate(title_list):
                # Unique slug
                slug = slugify(title)

                # Use a reliable placeholder service with keywords
                image_url = f"https://loremflickr.com/800/600/{keyword}?lock={random.randint(1, 1000)}"

                blog = Blog.objects.create(
                    title=title,
                    slug=slug,
                    category=cat,
                    author=author,
                    featured_image=image_url,
                    short_description=f"Discover more about {title} in this comprehensive editorial guide focusing on modern trends and practical insights.",
                    blog_body=f"""<h2>Exploring {title}</h2>
                    <p>This article dives deep into the world of {cat_name}, specifically focusing on {title}. As we navigate the complexities of the modern world, understanding these core concepts becomes increasingly vital for professionals and enthusiasts alike.</p>
                    <h3>The Current Landscape</h3>
                    <p>In recent years, we have seen a significant shift in how {cat_name} is perceived and implemented. This transformation is driven by technological advancements and changing social dynamics.</p>
                    <h3>Key Considerations</h3>
                    <ul>
                        <li>Understanding the fundamental principles.</li>
                        <li>Adapting to new methodologies and tools.</li>
                        <li>Maintaining a focus on quality and ethics.</li>
                    </ul>
                    <h3>Conclusion</h3>
                    <p>Whether you are a beginner or a seasoned expert, keeping up with these trends is essential. Stay tuned for more insights in our {cat_name} series.</p>""",
                    status="Published",
                    is_featured=(i == 0),
                    seo_title=f"{title} | Habib Writes",
                    seo_description=f"A detailed exploration of {title} within the {cat_name} category. Learn more at Habib Writes.",
                    view_count=random.randint(100, 5000)
                )

                # Add random tags
                blog.tags.add(*random.sample(tag_objs, k=random.randint(2, 4)))
                self.stdout.write(f'Added article: {title}')

        # Add the hardcoded high-quality ones too
        for article_data in articles:
            cat = category_objs[article_data['category']]
            slug = slugify(article_data['title'])
            if not Blog.objects.filter(slug=slug).exists():
                blog = Blog.objects.create(
                    title=article_data['title'],
                    slug=slug,
                    category=cat,
                    author=author,
                    featured_image=article_data['image'],
                    short_description=article_data['content'][:200].replace('<h2>', '').replace('</h2>', ''),
                    blog_body=article_data['content'],
                    status="Published",
                    is_featured=True,
                    seo_title=f"{article_data['title']} | Habib Writes",
                    seo_description=f"Learn about {article_data['title']} at Habib Writes.",
                    view_count=random.randint(5000, 10000)
                )
                blog.tags.add(*random.sample(tag_objs, k=3))
                self.stdout.write(f'Added premium article: {article_data["title"]}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded professional blog content!'))
