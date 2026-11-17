"""Static content for the portfolio. Edit here; templates loop over it."""

SOCIAL_LINKS = [
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/munsiwalidalhassannizhu", "icon": "fa-linkedin"},
    {"label": "GitHub", "url": "https://github.com/walid3271", "icon": "fa-github"},
    {"label": "Hugging Face", "url": "https://huggingface.co/WalidAlHassan", "icon": "", "text": "HF"},
]

EXPERIENCE = [
    {
        "period": "Sep 2026 - Present",
        "role": "Senior AI Engineer",
        "company": "Omicon Group",
        "location": "Bashundhara R/A, Dhaka, Bangladesh · On-site",
        "points": [
            "Work with multi-agent AI systems.",
            "Build fully autonomous AI systems in which the agent communicates bidirectionally with both consumers and business personnel.",
        ],
    },
    {
        "period": "Aug 2026 - Present",
        "role": "AI Quality Analyst (Freelance)",
        "company": "RWS",
        "location": "Remote",
        "points": [
            "Audit the accuracy of voice LLM models.",
            "Analyse AI model responses across different languages.",
            "Review and analyse video generation results.",
        ],
    },
    {
        "period": "Jul 2025 - Aug 2026",
        "role": "Mid-Level AI Executive",
        "company": "HawkEyes Digital Monitoring Limited",
        "location": "Uttara, Dhaka, Bangladesh · On-site",
        "points": [
            "Owned AI projects end to end: image processing, model fine-tuning, accuracy measurement, API pipelines, performance analysis and production deployment.",
            "Built audio AI systems: text-to-speech (TTS), speech-to-text (STT), voice model fine-tuning, speech recognition and speaker diarization.",
            "Identified individual employees from multi-person audio recordings.",
            "Designed and built AI agents, including a calling AI agent.",
        ],
    },
    {
        "period": "Jul 2024 - Jun 2025",
        "role": "AI Engineer Executive",
        "company": "HawkEyes Digital Monitoring Limited",
        "location": "Uttara, Dhaka, Bangladesh · On-site",
        "points": [
            "Built vision AI response API pipelines and served model inference data to the backend team through REST APIs.",
            "Fine-tuned computer vision models and ran evaluations to track and improve accuracy.",
            "Developed real-time video streaming analytics: object tracking, distance measurement and speed analysis.",
            "Analysed project bugs and model responses to find root causes and improve reliability.",
        ],
    },
    {
        "period": "Feb 2024 - Jun 2024",
        "role": "Artificial Intelligence Engineer (Intern)",
        "company": "HawkEyes Digital Monitoring Limited",
        "location": "Uttara, Dhaka, Bangladesh",
        "points": [
            "Worked on image processing and data annotation.",
            "Trained computer vision models.",
        ],
    },
]

EDUCATION = [
    {"period": "2020 - 2024", "degree": "Bachelor of Computer Science and Engineering",
     "school": "Bangladesh University of Business and Technology (BUBT)",
     "place": "Dhaka, Bangladesh", "result": "CGPA - 3.97"},
    {"period": "2016 - 2018", "degree": "Higher Secondary Certificate",
     "school": "BAF Shaheen College Jashore",
     "place": "Jashore, Khulna, Bangladesh", "result": "GPA - 4.00"},
    {"period": "2014 - 2016", "degree": "Secondary School Certificate",
     "school": "Magura Government High School",
     "place": "Magura, Khulna, Bangladesh", "result": "GPA - 4.17"},
]

SKILLS = [
    {"title": "Core", "groups": [
        {"title": None, "items": ["Python", "SQL", "PostgreSQL", "MySQL", "NumPy", "Pandas"]},
    ]},
    {"title": "AI/ML", "groups": [
        {"title": "Frameworks & Tools", "items": ["PyTorch", "TensorFlow", "LangChain", "LangGraph", "LangSmith"]},
        {"title": "Computer Vision", "items": [
            "Image Classification", "Object Detection", "Segmentation", "Pose Estimation", "Object Tracking",
            "OCR", "Pattern Recognition", "Real-time Video Pipelines"]},
        {"title": "LLMs & AI Agents", "items": [
            "LLM Fine-tuning", "RAG", "AI Agents", "MCP", "PDF Analysis"]},
        {"title": "Speech & Audio", "items": [
            "Speech Recognition (STT)", "Text-to-Speech (TTS)", "Speaker Recognition", "Audio Diarization", "Speech Model Fine-tuning"]},
    ]},
    {"title": "Dev Stack", "groups": [
        {"title": None, "items": [
            "Django", "FastAPI", "Streamlit", "Docker", "Git", "CI/CD", "Linux",
            "Hugging Face Spaces", "Project Coordination"]},
    ]},
]

# category: cv | nlp  (used by the filter buttons)
PROJECTS = [
    {
        "title": "Face Detection Using URL", "category": "cv",
        "image": "PORTFOLIO/Face-Detection-Using-URL.webp",
        "stack": ["PyTorch", "YOLOv8", "FastAPI"],
        "summary": "FastAPI service that takes one or more image URLs and returns the recognised person, confidence and bounding-box coordinates.",
        "description": "A custom model integrated into a FastAPI application that processes image URLs to deliver detailed recognition data. Users submit one or more image URLs and the API responds with the detected individual's name, prediction accuracy and precise image coordinates, built on PyTorch and YOLOv8.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/Face-Detection-Using-URL")],
    },
    {
        "title": "Floor Plan Object & Direction Identification", "category": "cv",
        "image": "PORTFOLIO/Floor-Object-Rooms-and-Bed-direction-Identification-according-to-angle.webp",
        "stack": ["PyTorch", "Ultralytics", "OpenCV", "pandas"],
        "summary": "Detects objects and rooms on floor plans and checks their orientation against Vastu angles.",
        "description": "An AI solution that analyses floor plans based on the orientation and location of objects: it detects items such as a sofa, and determines the current and optimal location of rooms like the kitchen. Built with PyTorch, Ultralytics, OpenCV and pandas.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/Floor-Object-Rooms-and-Bed-direction-Identification-according-to-Vastu-angle")],
    },
    {
        "title": "Face Recognition Authentication", "category": "cv",
        "image": "PORTFOLIO/GMP_Face_Recognation.webp",
        "stack": ["PyTorch", "Dlib", "FastAPI"],
        "summary": "Face-based login API that verifies an image URL against the registered face of a user ID and returns JSON.",
        "description": "A facial recognition system for secure login. It accepts an image URL and a user ID, verifies the image against the registered facial data for that ID and returns a JSON response indicating whether the user is valid. Built with PyTorch, Dlib and FastAPI.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/GMP_Face_Authentication")],
    },
    {
        "title": "Bolt Direction Detection", "category": "cv",
        "image": "PORTFOLIO/Find-Direction-Of-A-Bolt.webp",
        "stack": ["YOLOv8", "OBB", "PyTorch", "FastAPI"],
        "summary": "Finds the centre, angle and head position of bolts using two YOLOv8 models (detection + oriented boxes).",
        "description": "A computer vision system that accurately determines the angle, centre point and head position of bolts on various surfaces. Two YOLOv8 models, one for object detection and one for oriented bounding boxes, are served through a FastAPI endpoint that returns structured JSON.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/Find-Direction-Of-A-Bolt")],
    },
    {
        "title": "Virtual Control", "category": "cv",
        "image": "PORTFOLIO/Virtual-Mouse.webp",
        "stack": ["MediaPipe", "OpenCV", "Python"],
        "summary": "Touchless mouse and volume control through real-time hand and finger gestures.",
        "description": "A gesture-based control system that lets users move the mouse pointer and adjust volume using only hand and finger gestures, using MediaPipe for real-time hand tracking and OpenCV for image processing.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/Virtual-Mouse")],
    },
    {
        "title": "Conveyor Belt Screw Count", "category": "cv",
        "image": "PORTFOLIO/screw.webp",
        "stack": ["Ultralytics YOLO", "PyTorch", "Tkinter"],
        "summary": "Desktop app that classifies screws as good or damaged, tracks them and counts each class in real time.",
        "description": "A desktop application that detects whether screws are damaged or in good condition, with real-time tracking and individual counting of both classes. Uses Ultralytics YOLO and PyTorch for detection and classification, and Tkinter for the interface.",
        "links": [("Get App", "https://huggingface.co/WalidAlHassan/SCREW-APP"),
                  ("Repository", "https://huggingface.co/WalidAlHassan/Conveyor-Belt-Screw-Count")],
    },
    {
        "title": "LLaMA ChatBot", "category": "nlp",
        "image": "PORTFOLIO/LLAMA.webp",
        "stack": ["LLaMA", "Streamlit", "NLP"],
        "summary": "Conversational chatbot powered by Meta's LLaMA model with a Streamlit interface.",
        "description": "An interactive chatbot built on Meta's LLaMA model with a Streamlit front end, designed to hold context-aware conversations.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/ChatBot")],
    },
    {
        "title": "Gemini ChatBot", "category": "nlp",
        "image": "PORTFOLIO/Gemini.webp",
        "stack": ["Gemini Pro API", "Streamlit"],
        "summary": "Chatbot using the Gemini Pro API, deployed live on Streamlit Community Cloud.",
        "description": "An AI chatbot built on the Gemini Pro model API with a Streamlit interface, deployed to a Streamlit server so anyone can try it.",
        "links": [("Live Demo", "https://chatbot-with-gemini.streamlit.app/"),
                  ("Repository", "https://huggingface.co/WalidAlHassan/ChatBot-Gemini")],
    },
    {
        "title": "Romero RAG ChatBot", "category": "nlp",
        "image": "PORTFOLIO/Romero-ChatBot.webp",
        "stack": ["RAG", "FAISS", "LLM", "Web Scraping"],
        "summary": "Retrieval-Augmented Generation chatbot over scraped web data, indexed in a FAISS vector store.",
        "description": "A Retrieval-Augmented Generation chatbot: data is gathered by web scraping, split into 10,000-word chunks with a 1,000-word overlap, embedded and stored in a FAISS vector store. On each query the most relevant chunks are retrieved and an LLM generates the answer.",
        "links": [("Repository", "https://huggingface.co/WalidAlHassan/Romero-ChatBot")],
    },
]
