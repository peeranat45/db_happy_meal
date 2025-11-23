from model import Channels, Diseases, EatingLifestyleCategories, ExerciseTypes, Exercises, Foods, Ingredients, Locations, MealTypes, Occupations, SessionLocal, SocialPlatforms


MASTER_DATA_TABLE = [
    "diseases",  # Complete
    "eating_lifestyle_categories", # Complete
    "social_platforms", # Complete
    "meal_types",
    "locations",  # Complete
    "foods", # Complete
    "ingredients", # Complete
    "exercise_types", # Complete
    "meal_plan_types", # Complete
    "channels", 
]

TRANSACTION_DATA_TABLE = [
    
]

DISEASES = [
    {"name": "Dengue Fever", "description": "Viral infection spread by Aedes mosquitoes, common during rainy season"},
    {"name": "Influenza", "description": "Respiratory illness caused by influenza virus, seasonal outbreaks"},
    {"name": "Hypertension", "description": "High blood pressure, common among adults and elderly"},
    {"name": "Diabetes Mellitus", "description": "Chronic condition affecting blood sugar control"},
    {"name": "Thalassemia", "description": "Inherited blood disorder common in Southeast Asia"},
    {"name": "Food Poisoning", "description": "Illness from eating contaminated food or water"},
    {"name": "Hand, Foot and Mouth Disease", "description": "Viral infection common among young children"},
    {"name": "COVID-19", "description": "Respiratory disease caused by coronavirus, global pandemic since 2019"},
    {"name": "Allergic Rhinitis", "description": "Nasal allergy caused by dust or pollen exposure"},
    {"name": "Gastroenteritis", "description": "Stomach flu caused by bacterial or viral infection"},
    {"name": "Obesity", "description": "Condition of excess body fat that increases health risks"},
    {"name": "Gout", "description": "Arthritis caused by uric acid buildup in joints"},
    {"name": "Tuberculosis", "description": "Bacterial infection affecting the lungs"},
    {"name": "Liver Disease (Fatty Liver)", "description": "Accumulation of fat in liver cells, often from diet or alcohol"},
    {"name": "Migraine", "description": "Recurrent severe headaches with nausea or light sensitivity"},
    {"name": "Asthma", "description": "Chronic lung disease causing breathing difficulty"},
    {"name": "Kidney Disease", "description": "Damage to kidneys affecting waste filtration"},
    {"name": "Stroke", "description": "Sudden loss of brain function due to blood flow blockage"},
    {"name": "Hepatitis B", "description": "Viral infection that affects the liver"},
    {"name": "Malaria", "description": "Mosquito-borne disease causing fever and chills"},
]



SOCIAL_PLATFORM = [
    "Facebook"
    "Instagram",
    "Twitter",
    "LinkedIn",
    "YouTube",
    "TikTok",
    "Pinterest",
    "WhatsApp",
]


INGREDIENTS = [
    {"name": "Chicken", "description": "Lean protein commonly used in many dishes."},
    {"name": "Cooked Rice", "description": "A staple grain and primary carbohydrate source."},
    {"name": "Cucumber", "description": "A hydrating vegetable with a mild, refreshing taste."},
    {"name": "Sauce", "description": "A flavored liquid used to enhance taste."},
    {"name": "Green Papaya", "description": "Unripe papaya used for salads and savory dishes."},
    {"name": "Tomato", "description": "A juicy red fruit used in salads, sauces, and soups."},
    {"name": "Fish Sauce", "description": "A salty fermented seasoning used in Southeast Asian cuisine."},
    {"name": "Peanuts", "description": "Crunchy legumes often used as toppings or snacks."},
    {"name": "Pizza Dough", "description": "A yeast-based dough used as the base for pizza."},
    {"name": "Tomato Sauce", "description": "A cooked sauce made from tomatoes."},
    {"name": "Mozzarella Cheese", "description": "A soft, mild cheese commonly used on pizza."},
    {"name": "Sushi Rice", "description": "Short-grain rice seasoned with vinegar for sushi."},
    {"name": "Raw Salmon", "description": "Fresh salmon typically used in sushi and sashimi."},
    {"name": "Rice Noodles", "description": "Thin noodles made from rice flour, common in Asian dishes."},
    {"name": "Shrimp", "description": "A small, flavorful seafood ingredient."},
    {"name": "Bean Sprouts", "description": "Crunchy sprouts used in stir-fries and salads."},
    {"name": "Tofu", "description": "A protein-rich soy product with a soft texture."},
    {"name": "Shrimp", "description": "A tender shellfish used in soups and stir-fries."},
    {"name": "Mushroom", "description": "An earthy, savory fungus used in soups and stir-fries."},
    {"name": "Tom Yum Paste", "description": "A spicy Thai seasoning paste for Tom Yum soup."},
    {"name": "Beef Tenderloin", "description": "A premium, tender cut of beef."},
    {"name": "Butter", "description": "A rich dairy fat used for cooking and flavoring."},
    {"name": "Potato", "description": "A starchy root vegetable used in many dishes."},
    {"name": "Chicken Breast", "description": "Lean white meat rich in protein."},
    {"name": "Coconut Milk", "description": "Creamy liquid extracted from coconut flesh."},
    {"name": "Green Curry Paste", "description": "A spicy Thai curry paste made from herbs and chilies."},
    {"name": "Thai Eggplant", "description": "Small round eggplants used in Thai curries."},
    {"name": "Flour", "description": "A powder made from grains used in baking and cooking."},
    {"name": "Butter", "description": "Creamy dairy fat used in pastries and cooking."},
    {"name": "Beef Patty", "description": "Ground beef shaped into a patty for burgers."},
    {"name": "Burger Bun", "description": "A soft bread roll used for burgers."},
    {"name": "Cheese Slice", "description": "Processed cheese slice for sandwiches and burgers."},
    {"name": "Lettuce", "description": "Leafy green vegetable used in salads and burgers."},
    {"name": "Cooked Rice", "description": "Steamed white rice used as a base for meals."},
    {"name": "Pork", "description": "A versatile meat used in stir-fries and soups."},
    {"name": "Egg", "description": "A protein-rich ingredient used in many recipes."},
    {"name": "Vegetables", "description": "Mixed assorted vegetables."},
    {"name": "Romaine Lettuce", "description": "Crisp lettuce commonly used in salads."},
    {"name": "Caesar Dressing", "description": "Creamy dressing made with cheese and anchovies."},
    {"name": "Croutons", "description": "Crunchy toasted bread cubes used in salads."},
    {"name": "Parmesan Cheese", "description": "A hard, salty Italian cheese."},
    {"name": "Ground Beef", "description": "Minced beef used in pasta and casseroles."},
    {"name": "Pasta Sheets", "description": "Flat sheets of pasta used for lasagna."},
    {"name": "Tomato Sauce", "description": "A rich sauce made from tomatoes."},
    {"name": "Bechamel Sauce", "description": "A creamy white sauce made from butter, flour, and milk."},
    {"name": "Sticky Rice", "description": "Glutinous rice used in desserts and traditional dishes."},
    {"name": "Mango", "description": "A sweet tropical fruit."},
    {"name": "Coconut Milk", "description": "Rich coconut extract used in desserts and curries."},
    {"name": "Potato", "description": "A common root vegetable used in fried or mashed dishes."},
    {"name": "Vegetable Oil", "description": "Cooking oil extracted from plants."},
    {"name": "Chicken Thigh", "description": "Flavorful dark meat portion of chicken."},
    {"name": "Coating (Flour/Spice)", "description": "Seasoned flour mixture used for frying."},
    {"name": "Ramen Noodles", "description": "Thin wheat noodles used in ramen soup."},
    {"name": "Pork Broth", "description": "Savory broth made from simmered pork bones."},
    {"name": "Chashu Pork", "description": "Slow-braised pork used as ramen topping."},
    {"name": "Boiled Egg", "description": "Egg cooked in boiling water."},
    {"name": "Cream", "description": "Thick dairy product used in desserts."},
    {"name": "Milk", "description": "Nutrient-rich dairy beverage."},
    {"name": "Sugar", "description": "Sweet granulated sweetener."},
    {"name": "Wide Rice Noodles", "description": "Flat rice noodles used in stir-fried dishes."},
    {"name": "Pork", "description": "Common meat used in Asian dishes."},
    {"name": "Chinese Broccoli", "description": "Leafy green with thick stems used in stir-fries."},
    {"name": "Soy Sauce", "description": "A salty fermented soy seasoning."},
    {"name": "Spaghetti", "description": "Long, thin Italian pasta."},
    {"name": "Guanciale (Bacon)", "description": "Cured pork jowl used in Italian cuisine."},
    {"name": "Egg Yolk", "description": "Yellow center of the egg used in sauces and pasta."},
    {"name": "Pecorino Cheese", "description": "Salty Italian sheep’s milk cheese."},
    {"name": "Apple", "description": "A crisp, sweet fruit."},
    {"name": "Banana", "description": "A soft, sweet tropical fruit rich in potassium."},
    {"name": "Orange", "description": "A citrus fruit rich in vitamin C."},
    {"name": "Grapes", "description": "Small sweet fruit often eaten fresh."},
    {"name": "Strawberries", "description": "Sweet red berries often used in desserts."},
    {"name": "Plain Yogurt", "description": "Fermented milk product with a tangy taste."},
    {"name": "Almonds", "description": "Crunchy nuts rich in healthy fats."},
    {"name": "Egg", "description": "A versatile protein-rich ingredient."},
    {"name": "Whole Wheat Bread", "description": "Bread made from whole grain wheat."},
    {"name": "Dark Chocolate", "description": "Chocolate with a high cocoa content and rich flavor."}
]

EXERCISES_TYPE = [
    {"name": "Running", "description": "A cardiovascular exercise that improves heart and lung function."},
    {"name": "Cycling", "description": "A low-impact endurance exercise focusing on leg strength and stamina."},
    {"name": "Swimming", "description": "A full-body workout that enhances strength, endurance, and flexibility."},
    {"name": "Yoga", "description": "Combines stretching, breathing, and meditation to improve balance and calmness."},
    {"name": "Pilates", "description": "Focuses on core strength, flexibility, and posture alignment."},
    {"name": "Weight Training", "description": "Uses resistance to build muscle mass and overall strength."},
    {"name": "HIIT", "description": "High-intensity interval training with short bursts of intense exercise and rest."},
    {"name": "Walking", "description": "A simple low-impact activity that promotes general health and fitness."},
    {"name": "Jump Rope", "description": "A cardio exercise that improves coordination and burns calories."},
    {"name": "Boxing", "description": "Combines strength, speed, and endurance with self-defense skills."},
    {"name": "CrossFit", "description": "A varied, high-intensity fitness program combining strength and conditioning."},
    {"name": "Stretching", "description": "Improves flexibility and reduces muscle tension and soreness."},
    {"name": "Rowing", "description": "A full-body endurance exercise targeting both upper and lower muscles."},
    {"name": "Dance Fitness", "description": "Fun and rhythmic movement to music for cardio and coordination."},
    {"name": "Zumba", "description": "A dance workout inspired by Latin music and aerobic movements."},
    {"name": "Aerobics", "description": "Continuous rhythmic activity that strengthens the cardiovascular system."},
    {"name": "Climbing", "description": "Builds strength and agility through rock or wall climbing."},
    {"name": "Hiking", "description": "Long walks in nature for endurance and mental relaxation."},
    {"name": "Tai Chi", "description": "Slow, controlled movements that promote balance and mindfulness."},
    {"name": "Martial Arts", "description": "Disciplined training for strength, flexibility, and self-defense."},
    {"name": "Bodyweight Training", "description": "Exercises using one’s own body weight for resistance."},
    {"name": "Skating", "description": "Improves balance, leg strength, and coordination on skates."},
    {"name": "Skiing", "description": "A winter sport that enhances balance, coordination, and leg power."},
    {"name": "Surfing", "description": "Riding ocean waves to improve balance and core strength."},
    {"name": "Jumping Jacks", "description": "A basic cardio move for full-body warm-up and fat burning."},
    {"name": "Burpees", "description": "A full-body exercise combining a squat, push-up, and jump."},
    {"name": "Plank", "description": "An isometric core exercise that strengthens the abs and back."},
    {"name": "Mountain Climbers", "description": "A dynamic exercise mimicking climbing motion to train the core."},
    {"name": "Lunges", "description": "Strengthens legs and glutes while improving balance."},
    {"name": "Squats", "description": "Targets the lower body muscles including thighs and glutes."}
]

LOCATION_TYPE = {
    "meals" : [
        "Restaurant",
        "Home",
        "Cafe",
        "Street Food",
        "Food Court",
        "School Canteen",
        "Office Canteen",
        "Market",
        "Convenience Store",
        "Fast Food",
        "Buffet",
        "Bar / Pub",
    ],
    "exercise" : {
        "Gym",
        "Home Workout",
        "Park",
        "Running Track",
        "Stadium",
        "Swimming Pool",
        "Sports Center",
        "Cycling Route",
        "Mountain Trail",
        "Beach",
        "Fitness Class Studio",
    }
}

LOCATION = [
  {"name": "Sunny Bistro", "location_type": "meals", "lat": 13.678912, "long": 100.712345},
  {"name": "Fit Gym", "location_type": "exercise", "lat": 13.734567, "long": 100.805432},
  {"name": "Green Garden Cafe", "location_type": "meals", "lat": 13.690123, "long": 100.734567},
  {"name": "Central Park", "location_type": "exercise", "lat": 13.712345, "long": 100.756789},
  {"name": "Mama's Kitchen", "location_type": "meals", "lat": 13.699876, "long": 100.789012},
  {"name": "Riverside Running Track", "location_type": "exercise", "lat": 13.721234, "long": 100.745678},
  {"name": "Street Eats", "location_type": "meals", "lat": 13.685432, "long": 100.723456},
  {"name": "National Stadium", "location_type": "exercise", "lat": 13.712987, "long": 100.764321},
  {"name": "Food Court Plaza", "location_type": "meals", "lat": 13.692345, "long": 100.732198},
  {"name": "Blue Wave Swimming Pool", "location_type": "exercise", "lat": 13.718234, "long": 100.753456},
  {"name": "School Canteen A", "location_type": "meals", "lat": 13.688901, "long": 100.721234},
  {"name": "Elite Sports Center", "location_type": "exercise", "lat": 13.720123, "long": 100.760987},
  {"name": "Office Canteen B", "location_type": "meals", "lat": 13.691234, "long": 100.735678},
  {"name": "City Cycling Route", "location_type": "exercise", "lat": 13.713456, "long": 100.748901},
  {"name": "City Market", "location_type": "meals", "lat": 13.687654, "long": 100.729876},
  {"name": "Mountain Trail Path", "location_type": "exercise", "lat": 13.722345, "long": 100.752345},
  {"name": "QuickStop Convenience", "location_type": "meals", "lat": 13.689876, "long": 100.734123},
  {"name": "Sunny Beach", "location_type": "exercise", "lat": 13.725678, "long": 100.749876},
  {"name": "Burger Town", "location_type": "meals", "lat": 13.690987, "long": 100.738901},
  {"name": "Zen Fitness Studio", "location_type": "exercise", "lat": 13.724123, "long": 100.755432},
  {"name": "Buffet Palace", "location_type": "meals", "lat": 13.692876, "long": 100.742345},
  {"name": "Home Workout Zone", "location_type": "exercise", "lat": 13.723456, "long": 100.757654},
  {"name": "The Local Bar", "location_type": "meals", "lat": 13.694123, "long": 100.744567},
  {"name": "Fit Gym", "location_type": "exercise", "lat": 13.725432, "long": 100.759123},
  {"name": "Mama's Kitchen", "location_type": "meals", "lat": 13.695678, "long": 100.746789},
  {"name": "Central Park", "location_type": "exercise", "lat": 13.726789, "long": 100.760987},
  {"name": "Street Eats", "location_type": "meals", "lat": 13.696543, "long": 100.748901},
  {"name": "Riverside Running Track", "location_type": "exercise", "lat": 13.727654, "long": 100.762345},
  {"name": "Food Court Plaza", "location_type": "meals", "lat": 13.697123, "long": 100.751234},
  {"name": "National Stadium", "location_type": "exercise", "lat": 13.728123, "long": 100.763456},
  {"name": "School Canteen A", "location_type": "meals", "lat": 13.698432, "long": 100.752345},
  {"name": "Blue Wave Swimming Pool", "location_type": "exercise", "lat": 13.729876, "long": 100.764567},
  {"name": "Office Canteen B", "location_type": "meals", "lat": 13.699876, "long": 100.753456},
  {"name": "Elite Sports Center", "location_type": "exercise", "lat": 13.731234, "long": 100.765432},
  {"name": "City Market", "location_type": "meals", "lat": 13.700123, "long": 100.754321},
  {"name": "City Cycling Route", "location_type": "exercise", "lat": 13.732345, "long": 100.766543},
  {"name": "QuickStop Convenience", "location_type": "meals", "lat": 13.701234, "long": 100.755432},
  {"name": "Mountain Trail Path", "location_type": "exercise", "lat": 13.733456, "long": 100.767654},
  {"name": "Burger Town", "location_type": "meals", "lat": 13.702345, "long": 100.756543},
  {"name": "Sunny Beach", "location_type": "exercise", "lat": 13.734567, "long": 100.768765}
]


EXERCISE_LOCATION_MAPPING = {
    "Running": ["Park", "Running Track", "Beach", "Mountain Trail", "Stadium"],
    "Cycling": ["Cycling Route", "Park", "Mountain Trail", "Stadium", "Beach"],
    "Swimming": ["Swimming Pool", "Beach", "Sports Center"],
    "Yoga": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Pilates": ["Home Workout", "Gym", "Fitness Class Studio"],
    "Weight Training": ["Gym", "Home Workout", "Sports Center"],
    "HIIT": ["Gym", "Home Workout", "Park", "Fitness Class Studio"],
    "Walking": ["Park", "Running Track", "Beach", "Stadium", "Mountain Trail"],
    "Jump Rope": ["Home Workout", "Gym", "Park", "Stadium"],
    "Boxing": ["Gym", "Fitness Class Studio", "Sports Center"],
    "CrossFit": ["Gym", "Sports Center", "Fitness Class Studio"],
    "Stretching": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Rowing": ["Swimming Pool", "Beach", "Sports Center"],
    "Dance Fitness": ["Fitness Class Studio", "Gym", "Home Workout"],
    "Zumba": ["Fitness Class Studio", "Gym", "Home Workout"],
    "Aerobics": ["Fitness Class Studio", "Gym", "Home Workout"],
    "Climbing": ["Mountain Trail", "Gym", "Sports Center"],
    "Hiking": ["Mountain Trail", "Park", "Beach"],
    "Tai Chi": ["Park", "Home Workout"],
    "Martial Arts": ["Gym", "Sports Center", "Fitness Class Studio"],
    "Bodyweight Training": ["Home Workout", "Gym", "Park"],
    "Skating": ["Stadium", "Park", "Beach"],
    "Skiing": ["Mountain Trail", "Stadium"],
    "Surfing": ["Beach"],
    "Jumping Jacks": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Burpees": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Plank": ["Home Workout", "Gym", "Fitness Class Studio"],
    "Mountain Climbers": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Lunges": ["Home Workout", "Gym", "Park", "Fitness Class Studio"],
    "Squats": ["Home Workout", "Gym", "Park", "Fitness Class Studio"]
}

LIFESTYLE_CATEGORIES = [
  "Vegan"
  "Keto",
  "Intermittent Fasting",
  "Plant-Based",
  "Gluten-Free",
  "Paleo",
  "Pescatarian",
]


OCCUPATIONS = [
    "Software Engineer",
    "Data Scientist",
    "Teacher",
    "Doctor",
    "Nurse",
    "Accountant",
    "Civil Engineer",
    "Mechanical Engineer",
    "Electrical Engineer",
    "Lawyer",
    "Pharmacist",
    "Architect",
    "Graphic Designer",
    "UX/UI Designer",
    "Marketing Specialist",
    "Sales Manager",
    "Project Manager",
    "HR Manager",
    "Financial Analyst",
    "Consultant",
    "Chef",
    "Journalist",
    "Photographer",
    "Pilot",
    "Flight Attendant",
    "Research Scientist",
    "Web Developer",
    "Content Writer",
    "Translator",
    "Electrician",
    "Plumber",
    "Carpenter",
    "Musician",
    "Actor",
    "Dancer",
    "Fitness Trainer",
    "Personal Trainer",
    "Entrepreneur",
    "Business Owner",
    "Politician",
    "Student",
    "Retired",
    "Freelancer",
    "Bartender",
    "Waiter / Waitress",
    "Driver",
    "Taxi Driver",
    "Delivery Rider",
    "Mechanic",
    "Technician",
    "Security Guard",
    "Police Officer",
    "Firefighter",
    "Farmer",
    "Gardener",
    "Research Assistant",
    "Laboratory Technician",
    "Social Worker",
    "Nanny",
    "Veterinarian",
    "Interior Designer",
    "Fashion Designer",
    "Event Planner",
]

CHANNELS = [
    {"id": 1, "name": "Homemade", "description": "Meals prepared and consumed at home."},
    {"id": 2, "name": "Restaurant", "description": "Meals consumed at a dining establishment."},
    {"id": 3, "name": "Food Delivery", "description": "Meals delivered from a third-party service or directly from the restaurant."},
    {"id": 4, "name": "Takeaway", "description": "Meals picked up from an establishment and consumed elsewhere."},
    {"id": 5, "name": "Drive-thru", "description": "Meals ordered and received from a vehicle."},
    {"id": 6, "name": "Café / Bakery", "description": "Light meals, coffee, or pastries from a café."},
    {"id": 7, "name": "Meal Kit", "description": "Pre-portioned ingredients delivered for home preparation."}
]

FOOD_CATEGORIES = [
  "Main Course"
  "Appetizer",
  "Soup",
  "Dessert",
  "Salad",
  "Beverage"
]

MEAL_TYPE = [
   "Breakfast", 
   "Brunch", 
   "Lunch", 
   "Supper", 
   "Snacks",
   "Dinner"
]


FOODS = [
    {"name": "Grilled Chicken Breast", "category": "Main Course", "carb": 0, "protein": 31, "fat": 3.6, "sodium": 70, "sugar": 0, "kcal": 165, "created_by": None},
    {"name": "Caesar Salad", "category": "Salad", "carb": 10, "protein": 5, "fat": 8, "sodium": 300, "sugar": 2, "kcal": 150, "created_by": None},
    {"name": "Tom Yum Soup", "category": "Soup", "carb": 6, "protein": 3, "fat": 2, "sodium": 800, "sugar": 1, "kcal": 50, "created_by": None},
    {"name": "Spaghetti Bolognese", "category": "Main Course", "carb": 40, "protein": 15, "fat": 10, "sodium": 400, "sugar": 6, "kcal": 350, "created_by": None},
    {"name": "Chocolate Cake", "category": "Dessert", "carb": 50, "protein": 6, "fat": 20, "sodium": 200, "sugar": 35, "kcal": 400, "created_by": None},
    {"name": "Mango Smoothie", "category": "Beverage", "carb": 35, "protein": 2, "fat": 1, "sodium": 15, "sugar": 30, "kcal": 180, "created_by": None},
    {"name": "Fried Spring Rolls", "category": "Appetizer", "carb": 25, "protein": 5, "fat": 10, "sodium": 350, "sugar": 2, "kcal": 200, "created_by": None},
    {"name": "Vegetable Stir Fry", "category": "Main Course", "carb": 20, "protein": 4, "fat": 5, "sodium": 250, "sugar": 5, "kcal": 150, "created_by": None},
    {"name": "Beef Burger", "category": "Main Course", "carb": 30, "protein": 20, "fat": 15, "sodium": 600, "sugar": 5, "kcal": 400, "created_by": None},
    {"name": "Greek Yogurt with Honey", "category": "Dessert", "carb": 15, "protein": 10, "fat": 0, "sodium": 50, "sugar": 12, "kcal": 120, "created_by": None},
    {"name": "Tomato Soup", "category": "Soup", "carb": 8, "protein": 2, "fat": 2, "sodium": 350, "sugar": 6, "kcal": 70, "created_by": None},
    {"name": "Iced Lemon Tea", "category": "Beverage", "carb": 12, "protein": 0, "fat": 0, "sodium": 5, "sugar": 12, "kcal": 50, "created_by": None},
    {"name": "Bruschetta", "category": "Appetizer", "carb": 18, "protein": 4, "fat": 5, "sodium": 200, "sugar": 2, "kcal": 120, "created_by": None},
    {"name": "Fruit Salad", "category": "Salad", "carb": 25, "protein": 1, "fat": 0, "sodium": 10, "sugar": 20, "kcal": 100, "created_by": None},
    {"name": "Pancakes with Syrup", "category": "Breakfast", "carb": 45, "protein": 6, "fat": 8, "sodium": 200, "sugar": 25, "kcal": 300, "created_by": None},
    {"name": "Omelette", "category": "Breakfast", "carb": 2, "protein": 12, "fat": 10, "sodium": 250, "sugar": 1, "kcal": 140, "created_by": None},
    {"name": "Grilled Salmon", "category": "Main Course", "carb": 0, "protein": 25, "fat": 13, "sodium": 70, "sugar": 0, "kcal": 220, "created_by": None},
    {"name": "Cheeseburger", "category": "Main Course", "carb": 32, "protein": 22, "fat": 18, "sodium": 700, "sugar": 6, "kcal": 450, "created_by": None},
    {"name": "Chicken Noodle Soup", "category": "Soup", "carb": 12, "protein": 8, "fat": 3, "sodium": 550, "sugar": 2, "kcal": 120, "created_by": None},
    {"name": "Chocolate Chip Cookies", "category": "Dessert", "carb": 22, "protein": 2, "fat": 12, "sodium": 150, "sugar": 15, "kcal": 200, "created_by": None},
    {"name": "Green Smoothie", "category": "Beverage", "carb": 20, "protein": 2, "fat": 0, "sodium": 10, "sugar": 12, "kcal": 90, "created_by": None},
    {"name": "Mozzarella Sticks", "category": "Appetizer", "carb": 15, "protein": 7, "fat": 12, "sodium": 400, "sugar": 1, "kcal": 200, "created_by": None},
    {"name": "Quinoa Salad", "category": "Salad", "carb": 25, "protein": 6, "fat": 5, "sodium": 150, "sugar": 3, "kcal": 180, "created_by": None},
    {"name": "French Toast", "category": "Breakfast", "carb": 30, "protein": 8, "fat": 10, "sodium": 220, "sugar": 15, "kcal": 250, "created_by": None},
    {"name": "Shrimp Fried Rice", "category": "Main Course", "carb": 45, "protein": 12, "fat": 8, "sodium": 500, "sugar": 4, "kcal": 320, "created_by": None},
    {"name": "Avocado Toast", "category": "Appetizer", "carb": 20, "protein": 5, "fat": 12, "sodium": 200, "sugar": 1, "kcal": 220, "created_by": None},
    {"name": "Lentil Soup", "category": "Soup", "carb": 18, "protein": 9, "fat": 3, "sodium": 400, "sugar": 2, "kcal": 130, "created_by": None},
    {"name": "Apple Pie", "category": "Dessert", "carb": 40, "protein": 2, "fat": 15, "sodium": 150, "sugar": 25, "kcal": 300, "created_by": None},
    {"name": "Berry Smoothie", "category": "Beverage", "carb": 25, "protein": 1, "fat": 0, "sodium": 5, "sugar": 20, "kcal": 100, "created_by": None},
    {"name": "Chicken Wings", "category": "Appetizer", "carb": 0, "protein": 20, "fat": 15, "sodium": 600, "sugar": 0, "kcal": 250, "created_by": None},
    {"name": "Greek Salad", "category": "Salad", "carb": 8, "protein": 4, "fat": 10, "sodium": 300, "sugar": 2, "kcal": 140, "created_by": None},
    {"name": "Bagel with Cream Cheese", "category": "Breakfast", "carb": 45, "protein": 10, "fat": 8, "sodium": 400, "sugar": 5, "kcal": 300, "created_by": None},
    {"name": "Beef Tacos", "category": "Main Course", "carb": 25, "protein": 15, "fat": 12, "sodium": 500, "sugar": 3, "kcal": 300, "created_by": None},
    {"name": "Spring Vegetable Soup", "category": "Soup", "carb": 10, "protein": 2, "fat": 1, "sodium": 200, "sugar": 3, "kcal": 60, "created_by": None},
    {"name": "Cheesecake", "category": "Dessert", "carb": 25, "protein": 6, "fat": 15, "sodium": 200, "sugar": 20, "kcal": 350, "created_by": None},
    {"name": "Mojito Mocktail", "category": "Beverage", "carb": 12, "protein": 0, "fat": 0, "sodium": 5, "sugar": 10, "kcal": 60, "created_by": None},
    {"name": "Stuffed Mushrooms", "category": "Appetizer", "carb": 5, "protein": 4, "fat": 7, "sodium": 180, "sugar": 1, "kcal": 80, "created_by": None},
    {"name": "Kale Salad", "category": "Salad", "carb": 10, "protein": 3, "fat": 6, "sodium": 150, "sugar": 2, "kcal": 90, "created_by": None},
    {"name": "Waffles with Syrup", "category": "Breakfast", "carb": 40, "protein": 8, "fat": 12, "sodium": 200, "sugar": 20, "kcal": 300, "created_by": None},
    {"name": "Teriyaki Chicken", "category": "Main Course", "carb": 12, "protein": 25, "fat": 8, "sodium": 600, "sugar": 10, "kcal": 250, "created_by": None},
    {"name": "Caprese Salad", "category": "Salad", "carb": 5, "protein": 6, "fat": 7, "sodium": 150, "sugar": 2, "kcal": 120, "created_by": None},
    {"name": "French Fries", "category": "Appetizer", "carb": 35, "protein": 4, "fat": 15, "sodium": 400, "sugar": 0, "kcal": 350, "created_by": None},
    {"name": "Pumpkin Soup", "category": "Soup", "carb": 10, "protein": 2, "fat": 4, "sodium": 300, "sugar": 5, "kcal": 90, "created_by": None},
    {"name": "Brownie", "category": "Dessert", "carb": 30, "protein": 3, "fat": 12, "sodium": 150, "sugar": 20, "kcal": 250, "created_by": None},
    {"name": "Iced Coffee", "category": "Beverage", "carb": 12, "protein": 1, "fat": 0, "sodium": 10, "sugar": 12, "kcal": 70, "created_by": None},
    {"name": "Garlic Bread", "category": "Appetizer", "carb": 20, "protein": 3, "fat": 5, "sodium": 250, "sugar": 1, "kcal": 120, "created_by": None},
    {"name": "Spinach Salad", "category": "Salad", "carb": 6, "protein": 2, "fat": 3, "sodium": 120, "sugar": 1, "kcal": 50, "created_by": None},
    {"name": "Breakfast Burrito", "category": "Breakfast", "carb": 30, "protein": 15, "fat": 10, "sodium": 400, "sugar": 2, "kcal": 300, "created_by": None},
    {"name": "Grilled Steak", "category": "Main Course", "carb": 0, "protein": 28, "fat": 18, "sodium": 70, "sugar": 0, "kcal": 280, "created_by": None},
    {"name": "Tomato Bruschetta", "category": "Appetizer", "carb": 18, "protein": 4, "fat": 5, "sodium": 200, "sugar": 2, "kcal": 120, "created_by": None},
    {"name": "Minestrone Soup", "category": "Soup", "carb": 12, "protein": 3, "fat": 2, "sodium": 300, "sugar": 3, "kcal": 80, "created_by": None},
    {"name": "Creme Brulee", "category": "Dessert", "carb": 20, "protein": 4, "fat": 15, "sodium": 100, "sugar": 18, "kcal": 250, "created_by": None},
    {"name": "Strawberry Smoothie", "category": "Beverage", "carb": 25, "protein": 1, "fat": 0, "sodium": 5, "sugar": 20, "kcal": 100, "created_by": None},
    {"name": "Edamame", "category": "Appetizer", "carb": 9, "protein": 8, "fat": 4, "sodium": 120, "sugar": 2, "kcal": 120, "created_by": None},
    {"name": "Asian Slaw", "category": "Salad", "carb": 10, "protein": 2, "fat": 3, "sodium": 150, "sugar": 4, "kcal": 80, "created_by": None},
    {"name": "Breakfast Sandwich", "category": "Breakfast", "carb": 28, "protein": 14, "fat": 8, "sodium": 350, "sugar": 4, "kcal": 280, "created_by": None},
    {"name": "Pasta Alfredo", "category": "Main Course", "carb": 40, "protein": 12, "fat": 20, "sodium": 500, "sugar": 3, "kcal": 400, "created_by": None},
    {"name": "Caprese Skewers", "category": "Appetizer", "carb": 5, "protein": 4, "fat": 5, "sodium": 100, "sugar": 2, "kcal": 70, "created_by": None},
    {"name": "Vegetable Soup", "category": "Soup", "carb": 10, "protein": 2, "fat": 1, "sodium": 250, "sugar": 3, "kcal": 60, "created_by": None},
    {"name": "Chocolate Pudding", "category": "Dessert", "carb": 30, "protein": 3, "fat": 10, "sodium": 100, "sugar": 25, "kcal": 200, "created_by": None},
    {"name": "Green Tea", "category": "Beverage", "carb": 0, "protein": 0, "fat": 0, "sodium": 0, "sugar": 0, "kcal": 0, "created_by": None},
    {"name": "Stuffed Bell Peppers", "category": "Main Course", "carb": 15, "protein": 10, "fat": 8, "sodium": 300, "sugar": 4, "kcal": 200, "created_by": None},
    {"name": "Garlic Parmesan Wings", "category": "Appetizer", "carb": 0, "protein": 20, "fat": 15, "sodium": 600, "sugar": 0, "kcal": 250, "created_by": None},
    {"name": "Coleslaw", "category": "Salad", "carb": 10, "protein": 2, "fat": 5, "sodium": 200, "sugar": 5, "kcal": 120, "created_by": None},
    {"name": "Egg Muffin", "category": "Breakfast", "carb": 25, "protein": 12, "fat": 10, "sodium": 300,}
]



def insert_occupations():
    db: Session = SessionLocal()
    try:
        # Get existing occupation names from database
        existing = db.query(Occupations.name).all()
        existing_names = {row[0] for row in existing}

        # Find occupations not yet in database
        to_insert = [occ for occ in OCCUPATIONS if occ not in existing_names]

        # Insert only new ones
        for occ in to_insert:
            db.add(Occupations(name=occ))

        db.commit()

        print(f"Inserted {len(to_insert)} new occupations.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()


def insert_diseases():
    db: Session = SessionLocal()
    try:
        # Get existing disease names from DB
        existing = db.query(Diseases.name).all()
        existing_names = {row[0] for row in existing}

        # Filter diseases not in DB
        to_insert = [
            disease for disease in DISEASES
            if disease["name"] not in existing_names
        ]

        # Insert only those that are missing
        for d in to_insert:
            db.add(Diseases(name=d["name"], description=d.get("description")))

        db.commit()

        print(f"Inserted {len(to_insert)} new diseases.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert_channels():
    db: Session = SessionLocal()
    try:
        # Get existing channel names from the database
        existing = db.query(Channels.name).all()
        existing_names = {row[0] for row in existing}

        # Filter channels that are not yet in DB
        to_insert = [ch for ch in CHANNELS if ch["name"] not in existing_names]

        # Insert only missing channels
        for ch in to_insert:
            db.add(Channels(name=ch["name"], description=ch.get("description")))

        db.commit()
        print(f"Inserted {len(to_insert)} new channels.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert_lifestyle_categories():
    db: Session = SessionLocal()
    try:
        # Fetch existing names from DB
        existing = db.query(EatingLifestyleCategories.name).all()
        existing_names = {row[0] for row in existing}

        # Filter categories not already in DB
        to_insert = [name for name in LIFESTYLE_CATEGORIES if name not in existing_names]

        # Insert new categories
        for name in to_insert:
            db.add(EatingLifestyleCategories(name=name, description=None))  # Optional: add description if you want

        db.commit()
        print(f"Inserted {len(to_insert)} new lifestyle categories.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert_exercise_types():
    db: Session = SessionLocal()
    try:
        # Get existing exercise names from DB
        existing = db.query(ExerciseTypes.name).all()
        existing_names = {row[0] for row in existing}

        # Filter only new exercises
        to_insert = [ex for ex in EXERCISES_TYPE if ex["name"] not in existing_names]

        # Insert new exercises
        for ex in to_insert:
            db.add(ExerciseTypes(name=ex["name"], description=ex.get("description")))

        db.commit()
        print(f"Inserted {len(to_insert)} new exercise types.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert_ingredients():
    db: Session = SessionLocal()
    try:
        # Get existing ingredient names from DB
        existing = db.query(Ingredients.name).all()
        existing_names = {row[0] for row in existing}

        # Filter only new ingredients
        to_insert = [ing for ing in INGREDIENTS if ing["name"] not in existing_names]

        # Insert missing ingredients
        for ing in to_insert:
            db.add(Ingredients(name=ing["name"], description=ing.get("description")))

        db.commit()
        print(f"Inserted {len(to_insert)} new ingredients.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()


def insert_locations():
    db: Session = SessionLocal()
    try:
        # Get existing locations from DB (using name + location_type)
        existing = db.query(Locations.name, Locations.location_type).all()
        existing_set = {(row[0], row[1]) for row in existing}

        # Filter only new locations
        to_insert = [
            loc for loc in LOCATION
            if (loc["name"], loc["location_type"]) not in existing_set
        ]

        # Insert missing locations
        for loc in to_insert:
            db.add(Locations(
                name=loc["name"],
                location_type=loc["location_type"],
                lat=loc["lat"],
                long=loc["long"]
            ))

        db.commit()
        print(f"Inserted {len(to_insert)} new locations.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert_social_platforms():
    db: Session = SessionLocal()
    try:
        # Get existing platform names from DB
        existing = db.query(SocialPlatforms.name).all()
        existing_names = {row[0] for row in existing}

        # Filter only new platforms
        to_insert = [platform for platform in SOCIAL_PLATFORM if platform not in existing_names]

        # Insert missing platforms
        for platform in to_insert:
            db.add(SocialPlatforms(name=platform))

        db.commit()
        print(f"Inserted {len(to_insert)} new social platforms.")
    except Exception as e:
        db.rollback()
        print("Error inserting social platforms:", e)
    finally:
        db.close()

def insert_meal_types():
    db: Session = SessionLocal()
    try:
        # Get existing meal type names from DB
        existing = db.query(MealTypes.name).all()
        existing_names = {row[0] for row in existing}

        # Filter only new meal types
        to_insert = [meal for meal in MEAL_TYPE if meal not in existing_names]

        # Insert missing meal types
        for meal in to_insert:
            db.add(MealTypes(name=meal))

        db.commit()
        print(f"Inserted {len(to_insert)} new meal types.")
    except Exception as e:
        db.rollback()
        print("Error inserting meal types:", e)
    finally:
        db.close()

from sqlalchemy.orm import Session

def insert_foods():
    db: Session = SessionLocal()
    try:
        # Get existing food names from DB
        existing = db.query(Foods.name).all()
        existing_names = {row[0] for row in existing}

        # Filter only new foods
        to_insert = [food for food in FOODS if food["name"] not in existing_names]

        # Insert missing foods
        for food in to_insert:
            db.add(Foods(
                name=food["name"],
                category=food.get("category", "Main Course"),
                carb=food.get("carb", 0.0),
                protein=food.get("protein", 0.0),
                fat=food.get("fat", 0.0),
                sodium=food.get("sodium", 0.0),
                sugar=food.get("sugar", 0.0),
                kcal=food.get("kcal", 0.0),
                created_by=food.get("created_by")  # Can be None
            ))

        db.commit()
        print(f"Inserted {len(to_insert)} new foods.")
    except Exception as e:
        db.rollback()
        print("Error inserting foods:", e)
    finally:
        db.close()





if __name__ == "__main__":
    insert_occupations()
    insert_diseases()
    insert_channels()
    insert_lifestyle_categories()
    insert_exercise_types()
    insert_ingredients()
    insert_locations()
    insert_social_platforms()
    insert_meal_types()
    insert_foods()




