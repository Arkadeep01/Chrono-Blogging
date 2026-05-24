"""
Seed definitions: 5 demo authors, 8 categories, 30 blog posts.
All demo accounts use the domain @demo.curiouschronicle.app
"""

SEED_EMAIL_DOMAIN = "demo.curiouschronicle.app"
DEFAULT_SEED_PASSWORD = "Demo@12345"

SEED_USERS = [
    {
        "username": "alexchen",
        "email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "full_name": "Alex Chen",
        "profile": {
            "bio": "Software engineer writing about web development, AI, and the tools shaping modern work.",
            "country": "United States",
            "author": True,
        },
    },
    {
        "username": "maya_rivera",
        "email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "full_name": "Maya Rivera",
        "profile": {
            "bio": "Travel writer and photographer documenting cities, culture, and slow journeys off the beaten path.",
            "country": "Spain",
            "author": True,
        },
    },
    {
        "username": "james_okonkwo",
        "email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "full_name": "James Okonkwo",
        "profile": {
            "bio": "Home cook and food storyteller exploring recipes, spices, and the history behind every plate.",
            "country": "Nigeria",
            "author": True,
        },
    },
    {
        "username": "priya_sharma",
        "email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "full_name": "Priya Sharma",
        "profile": {
            "bio": "Wellness coach sharing practical habits for sleep, movement, and balance in a busy world.",
            "country": "India",
            "author": True,
        },
    },
    {
        "username": "sam_foster",
        "email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "full_name": "Sam Foster",
        "profile": {
            "bio": "Science communicator making research approachable—from climate and space to everyday curiosity.",
            "country": "United Kingdom",
            "author": True,
        },
    },
]

SEED_CATEGORIES = [
    {"title": "Technology", "slug": "technology"},
    {"title": "Travel", "slug": "travel"},
    {"title": "Food & Dining", "slug": "food-dining"},
    {"title": "Lifestyle", "slug": "lifestyle"},
    {"title": "Science", "slug": "science"},
    {"title": "Health & Wellness", "slug": "health-wellness"},
    {"title": "Culture", "slug": "culture"},
    {"title": "Business", "slug": "business"},
]

# Each post: author email, category slug, title, HTML description, tags, views
SEED_POSTS = [
    # Alex Chen — 6 posts
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "technology",
        "title": "The Future of AI in Everyday Life",
        "description": (
            "<p>Artificial intelligence is no longer confined to research labs. From email drafts to "
            "photo editing, AI tools are becoming quiet assistants in daily workflows.</p>"
            "<p>The most useful applications today focus on augmentation rather than replacement—helping "
            "people write faster, summarize meetings, and spot patterns in data they would miss alone.</p>"
            "<p>As these tools mature, the important questions shift toward transparency, consent, and "
            "who benefits when decisions are automated.</p>"
        ),
        "tags": "ai, technology, future",
        "views": 1240,
    },
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "technology",
        "title": "Building Scalable APIs with Django REST Framework",
        "description": (
            "<p>Django REST Framework remains a practical choice for teams that want batteries-included "
            "auth, serializers, and pagination without reinventing the wheel.</p>"
            "<p>Start with clear serializers, consistent pagination, and versioned endpoints. Add caching "
            "only after you measure real bottlenecks—not because a blog post told you to.</p>"
            "<p>Good API design is mostly about predictable naming, helpful errors, and documentation "
            "your frontend teammates will actually read.</p>"
        ),
        "tags": "django, api, backend",
        "views": 890,
    },
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "technology",
        "title": "Why Type Safety Matters in Modern Web Apps",
        "description": (
            "<p>TypeScript and similar tools catch an entire class of bugs before they reach production. "
            "That alone can justify the learning curve for growing teams.</p>"
            "<p>Types also serve as living documentation: when a component’s props change, the compiler "
            "points to every place that needs updating.</p>"
            "<p>The goal is not perfection—it is fewer surprises when you refactor six months later.</p>"
        ),
        "tags": "typescript, javascript, web",
        "views": 756,
    },
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "Quantum Computing Explained Without the Hype",
        "description": (
            "<p>Quantum computers leverage superposition and entanglement to explore many solutions at once "
            "for specific problem classes—not to replace your laptop.</p>"
            "<p>Today’s devices are noisy and small, but they are already useful for simulation and "
            "optimization research in chemistry and logistics.</p>"
            "<p>Understanding the limits is as important as celebrating the breakthroughs.</p>"
        ),
        "tags": "quantum, science, computing",
        "views": 2103,
    },
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "business",
        "title": "Remote Work Tools That Actually Stick",
        "description": (
            "<p>Teams often collect a dozen apps and still struggle with alignment. The best stacks are "
            "small: one place for tasks, one for docs, one for async video updates.</p>"
            "<p>Adoption beats features. Choose tools people will open every morning without a reminder "
            "from management.</p>"
            "<p>Review your stack quarterly and remove anything that duplicates another workflow.</p>"
        ),
        "tags": "remote work, productivity, business",
        "views": 645,
    },
    {
        "author_email": f"alexchen@{SEED_EMAIL_DOMAIN}",
        "category_slug": "culture",
        "title": "Open Source Communities That Shaped the Web",
        "description": (
            "<p>Linux, Python, React, and countless libraries exist because volunteers and companies "
            "invested in shared infrastructure.</p>"
            "<p>Healthy communities balance welcoming newcomers with maintaining quality through "
            "clear contribution guides and respectful review culture.</p>"
            "<p>If you benefit from open source daily, consider contributing documentation, tests, "
            "or sponsorship—not only code.</p>"
        ),
        "tags": "open source, community, web",
        "views": 1122,
    },
    # Maya Rivera — 6 posts
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "travel",
        "title": "Hidden Gems in Lisbon You Should Not Miss",
        "description": (
            "<p>Beyond the famous viewpoints, Lisbon rewards slow wandering through Alfama’s alleys "
            "and the tile-covered streets of Mouraria.</p>"
            "<p>Try a late lunch at a family-run tasca, ride tram 28 early before crowds arrive, and "
            "end the day with music in a small fado house.</p>"
            "<p>Pack comfortable shoes—the city’s hills are part of the charm.</p>"
        ),
        "tags": "lisbon, portugal, europe",
        "views": 1876,
    },
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "travel",
        "title": "Backpacking Southeast Asia on a Thoughtful Budget",
        "description": (
            "<p>Affordable travel does not mean skipping experiences—it means choosing where your money "
            "creates the most memory per dollar.</p>"
            "<p>Mix overnight buses with occasional private rooms, eat street food with busy lines, and "
            "book activities directly with local operators when safe.</p>"
            "<p>Travel insurance and a basic medical kit are non-negotiable parts of the budget.</p>"
        ),
        "tags": "backpacking, asia, budget travel",
        "views": 2340,
    },
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "travel",
        "title": "Sustainable Tourism: Traveling With Purpose",
        "description": (
            "<p>Overtourism strains neighborhoods and ecosystems. Sustainable travel starts with length "
            "of stay, respect for local norms, and support for community-led initiatives.</p>"
            "<p>Choose accommodations that pay fair wages, reduce plastic, and source food locally when "
            "possible.</p>"
            "<p>Leave places better than you found them—sometimes that is as simple as tipping fairly "
            "and learning a few phrases in the local language.</p>"
        ),
        "tags": "sustainable travel, ecotourism",
        "views": 980,
    },
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "food-dining",
        "title": "Street Food Adventures in Mexico City",
        "description": (
            "<p>Mexico City’s street food scene is a masterclass in flavor: tacos al pastor, tlacoyos, "
            "and fresh aguas frescas on nearly every corner.</p>"
            "<p>Follow busy stalls, watch how ingredients are handled, and start with cooked dishes if "
            "your stomach is still adjusting.</p>"
            "<p>Food here is culture—take time to chat with vendors when the lunch rush slows down.</p>"
        ),
        "tags": "mexico city, street food, tacos",
        "views": 1654,
    },
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "lifestyle",
        "title": "How Travel Photography Changed My Perspective",
        "description": (
            "<p>Carrying a camera slowed me down in the best way. I began noticing light, gestures, and "
            "small details tourists often rush past.</p>"
            "<p>You do not need expensive gear—a phone and patience will teach composition faster than "
            "any filter pack.</p>"
            "<p>The best travel photos tell a story about people, not only landmarks.</p>"
        ),
        "tags": "photography, travel, creativity",
        "views": 720,
    },
    {
        "author_email": f"maya.rivera@{SEED_EMAIL_DOMAIN}",
        "category_slug": "culture",
        "title": "Festivals Around the World Worth Planning For",
        "description": (
            "<p>From Diwali lights to Carnival rhythms, festivals reveal how communities celebrate "
            "history, faith, and seasonal change.</p>"
            "<p>Book accommodation early, research dress codes, and participate respectfully rather than "
            "treating ceremonies as photo backdrops.</p>"
            "<p>Some of my favorite memories came from volunteering at local events—not from VIP tickets.</p>"
        ),
        "tags": "festivals, culture, events",
        "views": 1433,
    },
    # James Okonkwo — 6 posts
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "food-dining",
        "title": "Perfecting Homemade Sourdough Bread",
        "description": (
            "<p>Sourdough is part science, part ritual. A healthy starter and consistent feeding schedule "
            "matter more than fancy equipment.</p>"
            "<p>Autolyse, gentle folds, and patience during bulk fermentation transform simple flour "
            "into complex flavor.</p>"
            "<p>Your first loaves may be flat—keep notes on timing and temperature until you find your "
            "kitchen’s rhythm.</p>"
        ),
        "tags": "sourdough, baking, bread",
        "views": 1987,
    },
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "food-dining",
        "title": "Plant-Based Meals That Feel Satisfying",
        "description": (
            "<p>Great plant-based cooking leans on texture, acid, and umami—not only replacing meat "
            "with substitutes.</p>"
            "<p>Roast vegetables until caramelized, use beans and lentils for body, and finish dishes "
            "with herbs, citrus, and good olive oil.</p>"
            "<p>Build a pantry of spices and you will never feel like you are eating the same bowl twice.</p>"
        ),
        "tags": "plant-based, recipes, healthy eating",
        "views": 1105,
    },
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "food-dining",
        "title": "Spice Blends Every Home Cook Should Know",
        "description": (
            "<p>Blends like berbere, garam masala, and Cajun seasoning are shortcuts to depth—if you "
            "toast whole spices before grinding, even better.</p>"
            "<p>Store blends in airtight jars away from heat and label them with the month you mixed them.</p>"
            "<p>Start with small batches until you learn which combinations your household reaches for weekly.</p>"
        ),
        "tags": "spices, cooking tips, pantry",
        "views": 876,
    },
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "lifestyle",
        "title": "Hosting a Dinner Party for Six Without Stress",
        "description": (
            "<p>Choose one main dish you can prep ahead, one fresh element to assemble at the table, and "
            "a dessert you can buy if needed—guests remember conversation more than perfection.</p>"
            "<p>Set the table before guests arrive and accept help in the kitchen when offered.</p>"
            "<p>A simple playlist and good lighting do more for atmosphere than a complicated menu.</p>"
        ),
        "tags": "entertaining, dinner party, hosting",
        "views": 534,
    },
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "The Science Behind a Great Cup of Coffee",
        "description": (
            "<p>Extraction is the story: water temperature, grind size, and contact time determine whether "
            "your cup tastes bright or bitter.</p>"
            "<p>Freshly roasted beans and burr grinding beat expensive machines with stale grounds.</p>"
            "<p>Experiment with one variable at a time until you can taste the difference a two-degree "
            "change makes.</p>"
        ),
        "tags": "coffee, science, brewing",
        "views": 1542,
    },
    {
        "author_email": f"james.okonkwo@{SEED_EMAIL_DOMAIN}",
        "category_slug": "culture",
        "title": "West African Jollof: A Family Recipe Story",
        "description": (
            "<p>Every family defends their jollof recipe—and that friendly debate is part of the dish’s "
            "identity across the region.</p>"
            "<p>Tomato base, smoky pepper, and parboiled rice cooked in one pot create the flavors I "
            "associate with celebrations at home.</p>"
            "<p>Share your version respectfully; food traditions grow when we cook together and listen.</p>"
        ),
        "tags": "jollof, west africa, recipes",
        "views": 2890,
    },
    # Priya Sharma — 6 posts
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "health-wellness",
        "title": "Morning Routines That Boost Energy Naturally",
        "description": (
            "<p>You do not need a two-hour ritual. Ten minutes of daylight, hydration, and gentle movement "
            "can reset your nervous system before email takes over.</p>"
            "<p>Consistency beats intensity—pick three habits you can repeat on busy days.</p>"
            "<p>Track sleep first; no morning routine fixes chronic exhaustion from late screens.</p>"
        ),
        "tags": "morning routine, energy, habits",
        "views": 1765,
    },
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "health-wellness",
        "title": "Mindful Breathing for Busy Professionals",
        "description": (
            "<p>Box breathing and extended exhales activate the parasympathetic response in minutes—useful "
            "before presentations or difficult conversations.</p>"
            "<p>Practice when calm so the technique is familiar when stress arrives.</p>"
            "<p>Even sixty seconds of intentional breathing can lower heart rate and sharpen focus.</p>"
        ),
        "tags": "mindfulness, breathing, stress",
        "views": 923,
    },
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "lifestyle",
        "title": "Yoga for Desk Workers: A 15-Minute Flow",
        "description": (
            "<p>Hours at a desk tighten hips and shoulders. This short flow opens the chest, lengthens "
            "the spine, and wakes up the legs without needing a mat studio.</p>"
            "<p>Move slowly and never force range of motion—discomfort is information.</p>"
            "<p>Pair movement with micro-breaks every hour for the best results.</p>"
        ),
        "tags": "yoga, desk job, stretching",
        "views": 1340,
    },
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "Sleep Hygiene Tips Backed by Research",
        "description": (
            "<p>Regular bedtimes, cooler rooms, and reduced blue light before sleep consistently improve "
            "rest quality in studies.</p>"
            "<p>Caffeine’s half-life means afternoon coffee still affects some people at midnight.</p>"
            "<p>If insomnia persists for weeks, talk to a clinician—habits help but they are not a cure-all.</p>"
        ),
        "tags": "sleep, health, science",
        "views": 2456,
    },
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "food-dining",
        "title": "Meal Prep for a Healthy Work Week",
        "description": (
            "<p>Batch roast vegetables, cook a grain, and prepare two proteins on Sunday. Mix and match "
            "bowls in five minutes each morning.</p>"
            "<p>Glass containers make leftovers visible so nothing hides in the fridge until Friday.</p>"
            "<p>Include something you genuinely enjoy—sustainability requires pleasure, not punishment.</p>"
        ),
        "tags": "meal prep, nutrition, planning",
        "views": 1089,
    },
    {
        "author_email": f"priya.sharma@{SEED_EMAIL_DOMAIN}",
        "category_slug": "lifestyle",
        "title": "Digital Detox Weekends That Actually Work",
        "description": (
            "<p>Going cold turkey rarely lasts. Try phone-free mornings, app limits, and a dedicated drawer "
            "for devices during meals.</p>"
            "<p>Replace scrolling with one analog activity you miss—reading, walking, or cooking with friends.</p>"
            "<p>Notice what you reach for when bored; that awareness is the real habit shift.</p>"
        ),
        "tags": "digital detox, balance, mental health",
        "views": 812,
    },
    # Sam Foster — 6 posts
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "CRISPR and the Future of Medicine",
        "description": (
            "<p>Gene editing tools are moving from lab benches toward carefully monitored therapies for "
            "genetic diseases once considered untreatable.</p>"
            "<p>Ethical oversight, equitable access, and long-term safety studies must keep pace with "
            "technical capability.</p>"
            "<p>Understanding CRISPR basics helps citizens participate in informed debates about its use.</p>"
        ),
        "tags": "crispr, genetics, medicine",
        "views": 3012,
    },
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "Reading Climate Data Without Getting Lost",
        "description": (
            "<p>Global temperature anomalies, sea-level trends, and ice-sheet measurements come from "
            "independent datasets that largely agree on direction even when models differ on pace.</p>"
            "<p>Look for peer-reviewed sources, check units, and beware charts that cherry-pick years.</p>"
            "<p>Science literacy is a skill—ask how data was collected, not only what headline fits your view.</p>"
        ),
        "tags": "climate, data, environment",
        "views": 2210,
    },
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "Mars Missions: Where We Are Now",
        "description": (
            "<p>Rovers continue to map geology and search for signs of ancient habitability while orbiters "
            "relay communications and monitor weather.</p>"
            "<p>Sample-return plans and international cooperation will define the next decade of exploration.</p>"
            "<p>Human missions remain engineering and funding challenges—but each robotic success teaches "
            "systems we will need later.</p>"
        ),
        "tags": "mars, space, nasa",
        "views": 2678,
    },
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "culture",
        "title": "Teaching Kids to Love Science at Home",
        "description": (
            "<p>Kitchen chemistry, backyard astronomy, and simple experiments build curiosity without "
            "expensive kits.</p>"
            "<p>Let children ask “why” and search for answers together—mistakes are part of the method.</p>"
            "<p>Representation matters: share stories of scientists from diverse backgrounds and eras.</p>"
        ),
        "tags": "education, kids, science",
        "views": 945,
    },
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "technology",
        "title": "How Neural Networks Learn (Without the Jargon)",
        "description": (
            "<p>Neural networks adjust millions of weights by comparing predictions to correct answers, "
            "slowly reducing error through training data.</p>"
            "<p>They excel at pattern recognition—images, language, audio—but still struggle with "
            "causal reasoning and rare edge cases.</p>"
            "<p>Knowing limits helps you evaluate when AI is appropriate for a real-world problem.</p>"
        ),
        "tags": "machine learning, ai, education",
        "views": 1890,
    },
    {
        "author_email": f"sam.foster@{SEED_EMAIL_DOMAIN}",
        "category_slug": "science",
        "title": "The Physics of Rainbows and Sunsets",
        "description": (
            "<p>Rainbows appear when sunlight refracts and reflects inside water droplets at angles that "
            "separate wavelengths into vivid arcs.</p>"
            "<p>Sunset reds happen because blue light scatters out of the longer path through the atmosphere.</p>"
            "<p>Physics turns ordinary skies into reminders that beauty often has an elegant explanation.</p>"
        ),
        "tags": "physics, nature, optics",
        "views": 1567,
    },
]

# Image filenames in media/seed/post/ — same order as SEED_POSTS above
SEED_POST_IMAGE_FILES = [
    "ai-future.avif",
    "drf-api.avif",
    "typescript.avif",
    "quantum.avif",
    "remote-work.avif",
    "open-source.avif",
    "lisbon.avif",
    "southeast-asia.avif",
    "sustainable-tourismsustainable-tourism.avif",  # rename file to sustainable-tourism.avif when convenient
    "mexico-street-food.avif",
    "travel-photography.avif",
    "world-festivals.avif",
    "sourdough.avif",
    "plant-based.avif",
    "spice-blends.avif",
    "dinner-party.avif",
    "coffee-science.avif",
    "jollof.avif",
    "morning-routine.avif",
    "mindful-breathing.avif",
    "yoga-desk.avif",
    "sleep-hygiene.avif",
    "meal-prep.avif",
    "digital-detox.avif",
    "crispr.avif",
    "climate-data.jpg",
    "mars.avif",
    "kids-science.avif",
    "neural-networks.avif",
    "rainbows.avif",
]
