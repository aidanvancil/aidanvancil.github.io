// JavaScript
function generatePortfolioModal(images, title, description, id, link, techs) {
    const imageHtml = Array.isArray(images)
    ? images.map(imageSrc => `<img class="img-fluid rounded mb-5" src="${imageSrc}" alt="..." />`).join('')
    : '';
    const techHtml = Array.isArray(techs) 
    ? techs.map(tech => `<li>${tech}<li/>`).join('')
    : '';

  return `
    <div class="portfolio-modal modal fade" tabindex="-1" aria-hidden="true" id="portfolioModal${id}" aria-labelledby="portfolioModal${id}">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header border-0">
            <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center pb-5">
            <div class="container">
              <div class="row justify-content-center">
                <div class="col-lg-8">
                  <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">${title}</h2>
                  <div class="divider-custom">
                    <div class="divider-custom-line"></div>
                  </div>
                  ${imageHtml}
                  <p class="mb-4">${description}</p>
                  <h2 class="">Technologies Used:</h2>
                    <ul style="list-style-type: none;" class="text-left">
                        ${techHtml}
                    </ul>
                  <p><a href="${link}"> Explore More?</a></p>
                  <button class="btn btn-primary" data-bs-dismiss="modal">
                    <i class="fas fa-xmark fa-fw"></i>
                    Close Window
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}


// Array of modal data
const modalData = [
    {
        images: [
            'assets/img/portfolio/shut_the_box.gif',
            'assets/img/portfolio/shut_the_box2.png',
        ],
        title: 'Shut The Box - Game',
        description: 'Built this game in a 7-hour hackathon. This includes knocking down 9 dominoes. Immerse yourself in the exciting game of Shut the Box, brought to life with our innovative implementation using Pygame and object-oriented programming. Experience the thrill of strategic dice rolling and decision-making as you aim to close all numbered tiles on the game board.\n\nPygame, a powerful Python library, serves as the foundation for creating an engaging and visually appealing user interface. The game board and tiles are meticulously designed to provide an immersive gaming experience.',
        id: '1',
        link: 'https://github.com/aidanvancil/shut-the-box',
        techs: [
            '- Pygame',
            '- Python',
            '- Object-Orientated Programming',
            '- Game Design',
            '- Git'
        ]
    },
    {
        images: [
            'assets/img/portfolio/checkers.gif',
        ],
        title: 'Checkers / Local LAN Play ',
        description: 'Experience the classic game of Checkers like never before with our innovative AI-powered Checkers game. This engaging and strategic game combines the traditional rules of Checkers with advanced predictive analysis techniques to offer a challenging and dynamic gameplay experience.',
        id: '2',
        link: 'https://github.com/aidanvancil/checkers-in-python',
        techs: [
            '- Pygame',
            '- Python',
            '- Object-Orientated Programming',
            '- Machine Learning',
            '- Figma',
            '- Git',
            '- Version Control'
        ]
    },
    {
        images: [
            'assets/img/portfolio/sorting2.png',
            'assets/img/portfolio/sorting.gif',
            'assets/img/portfolio/sorting3.png',
            'assets/img/portfolio/sorting4.png'
        ],
        title: 'Sorting Algorithms Visualized',
        description: 'In this project, we explore the fascinating world of sorting algorithms. We implement and analyze various sorting algorithms to understand their efficiency and performance characteristics. From the classic Bubble Sort to the efficient Merge Sort and Quick Sort, we dive into the realm of organizing data in ascending or descending order. Through this project, we aim to enhance our understanding of algorithmic complexity, data structures, and the importance of choosing the right sorting algorithm for different scenarios.',
        id: '3',
        link: 'https://github.com/aidanvancil/sorting-algorithms-visualized',
        techs: [
            '- Algorithms',
            '- Pygame',
            '- Python',
            '- Data Structures',
            '- Matplotlib',
            '- Git'
        ]
    },
    {
        images: [
            'assets/img/portfolio/IMG-3510.png',
            'assets/img/portfolio/IMG-3517.png',
            'assets/img/portfolio/IMG-3511.jpg',
            'assets/img/portfolio/IMG-3512.jpg',
            'assets/img/portfolio/IMG-3513.jpg',
            'assets/img/portfolio/IMG-3514.jpg',
            'assets/img/portfolio/IMG-3515.png',
        ],
        title: 'Channel',
        description: 'Welcome to Channel, a dynamic mobile social media platform that allows you to connect with others, create engaging posts, and customize your profile. Join today and express yourself, connect with like-minded individuals, and explore exciting content.',
        id: '4',
        link: 'https://github.com/aidanvancil/channel',
        techs: [
            '- User-authentication',
            '- Email-verification',
            '- UI/UX',
            '- Figma',
            '- React',
            '- Low-Code',
        ]
    },
    {
        images: [
            'assets/img/portfolio/candy.png',
            'assets/img/portfolio/candy1.png',
            'assets/img/portfolio/candy2.png',
            'assets/img/portfolio/candy3.png'
        ],
        title: 'Candy Statistic Analaysis: A FiveThirtyEight Dataset',
        description: 'Delve into the world of candy preferences with our exciting data science project using the FiveThirtyEight Candy Dataset. This project aims to uncover insights and patterns regarding preferences for various types of candies. By leveraging data analysis and statistical techniques, we explore factors that influence candy choices and aim to answer intriguing questions like the most popular candy, regional candy preferences, and correlations between candy attributes and consumer satisfaction. Using Python and popular data science libraries such as Pandas, NumPy, and Matplotlib, we delve into the dataset and its rich information. Through data cleaning, preprocessing, and visualization, we gain a comprehensive understanding of the candy preferences dataset. We apply exploratory data analysis techniques to identify trends, distributions, and relationships within the data.',
        id: '5',
        link: 'https://colab.research.google.com/drive/180a6TI4qjPQ6BFtzDX_q9i9Kh24qySFZ?usp=sharing',
        techs: [
            '- Data Science',
            '- Python',
            '- Matplotlib',
            '- Seaborn',
            '- Pandas',
            '- Numpy'
        ]
    },
    {
        images: [
            'assets/img/portfolio/hyper.png',
            'assets/img/portfolio/hyper1.png',
            'assets/img/portfolio/hyper2.png',
            'assets/img/portfolio/hyper3.png',
            'assets/img/portfolio/hyper4.png',
            'assets/img/portfolio/hyper5.png'
        ],
        title: 'Testing ML Models with Random Forest Classifier and Hyperparameters: F1 Score Evaluation',
        description: 'Using scikit-learn library, we leverage the power of Random Forest Classifier to build robust and accurate predictive models. We explore different hyperparameters, such as the number of trees, maximum depth, and feature selection techniques, to optimize the model and its performance. By systematically adjusting these hyperparameters, we aim to enhance the model and its ability to generalize and make accurate predictions on unseen data. The F1 score, which combines precision and recall, serves as our evaluation metric. It provides a comprehensive assessment of a models performance, particularly in situations where there is an imbalance between the classes or when false positives and false negatives have different consequences.',
        id: '6',
        link: 'https://colab.research.google.com/drive/1mpkrqRiUhNiKkGkBl6BAUXTBzaTAjemc?usp=sharing',
        techs: [
            '- Data Science',
            '- Python',
            '- Numpy',
            '- Scikit',
        ]
    },
    {
        images: [
            'assets/img/portfolio/model.png',
            'assets/img/portfolio/model1.png',
            'assets/img/portfolio/model2.png',
            'assets/img/portfolio/model3.png'
        ],
        title: 'Training ML Models: Tinder Clone',
        description: 'Using advanced machine learning techniques, we build a recommendation system that analyzes user profiles, preferences, and historical interactions. The model employs algorithms such as collaborative filtering, content-based filtering, or hybrid approaches to identify potential matches. By considering various factors, including hobbies, interests, location, and demographic information, our ML model strives to predict and suggest matches that are likely to be mutually interested in each other. To train our ML model, we gather a large dataset comprising user profiles and their interactions within the application. We apply data preprocessing techniques to clean and transform the data into a suitable format for training and evaluation. Feature engineering is employed to extract relevant information from user profiles and interactions, enhancing the model and its ability to capture meaningful patterns.',
        id: '7',
        link: 'https://colab.research.google.com/drive/1oaWVNU5m0FRoXjd6-ZgD5yH9xVqtUdZ9?usp=sharing',
        techs: [
            '- Data Science',
            '- Python',
            '- Numpy',
            '- Scikit',
        ]
    },
    {
        images: [
            'assets/img/portfolio/wetour1.png'
        ],
        title: 'WeTour: Tourism App',
        description: 'The website allows you to find tour guides in different cities and even become a tour guide yourself! You can make your preferences for your trip and express yourself with our profiles. You can even get notifications about your trip and access all these features by creating an account.',
        id: '8',
        link: 'https://devpost.com/software/wetour-ygu012',
        techs: [
            '- Cohere',
            '- Django',
            '- Github',
            '- HTML5',
            '- RESTful APIs',
            '- TailwindCSS',
            '- Twillio',
            '- Google Maps',
            '- Mapquest'
        ]
    },
    {
        images: [
            'assets/img/portfolio/mezzo.png',
            'assets/img/portfolio/mezzo1.png',
            'assets/img/portfolio/mezzo2.png'
        ],
        title: 'Mezzo: Musical + Social Platform',
        description: 'Mezzo is a twist on a typical musical application that helps users connect with both their friends and favorite artists. With Mezzo, you can discover new music and connect with like-minded people who share your musical interests. This application was created from a collaborative team of three within a 3-month timespan.',
        id: '9',
        link: 'https://github.com/NikhilSharma1234/Mezzo',
        techs: [
            '- Express.js',
            '- React',
            '- Node.js',
            '- MongoDB',
            '- TTD',
            '- Github',
            '- Version Control',
            '- RESTful APIs',
        ]
    },
    {
        images: [
            'assets/img/portfolio/arduino.png',
        ],
        title: 'C++/C Swamp Cooler',
        description: 'The core of the project involves using an Arduino microcontroller to control various components, including a water pump, fan, and environmental sensors. The microcontroller regulates the flow of water to wet a porous cooling pad or medium, which is then exposed to a fan-driven airflow. As the air passes through the wet medium, it evaporates the water, resulting in a cooling effect that lowers the temperature of the surrounding air. The Arduino microcontroller plays a crucial role in automating the swamp cooler system. It monitors environmental conditions such as temperature and humidity using sensors and adjusts the water flow and fan speed accordingly to optimize cooling performance. The microcontroller can be programmed and customized to incorporate additional features such as timers, remote control functionality, or integration with smart home systems.',
        id: '10',
        link: 'https://github.com/aidanvancil/arduino_swamp_cooler',
        techs: [
            '- C++',
            '- C',
            '- Arduino',
            '- Hardware Engineering',
            '- Github',
            '- Version Control',
            '- Electrical Engineering'
        ]
    },
    {
        images: [
            'assets/img/portfolio/maskr1.png',
            'assets/img/portfolio/maskr2.png',
            'assets/img/portfolio/maskr3.png',
            'assets/img/portfolio/maskr4.png'
        ],
        title: 'maskr, Generative AI Tool',
        description: 'Maskr leverages the cutting-edge capabilities of the OpenAI API to provide users with a seamless and intuitive image editing experience. The app offers a diverse set of editing features, including background removal, object manipulation, style transfer, and intelligent image generation. Using advanced machine learning algorithms, maskr enables users to effortlessly remove or replace backgrounds in photos. Whether you want to isolate the subject, place them in a different setting, or create artistic compositions, maskr and its background removal tool offers precision and flexibility.',
        id: '11',
        link: 'https://github.com/aidanvancil/maskr',
        techs: [
            '- Django',
            '- RESTful APIs',
            '- Generative AI',
            '- Computer Vision',
            '- Github',
            '- Version Control',
        ]
    },
    {
        images: [
            'assets/img/portfolio/syn1.png'
        ],
        title: 'Synonymy, Semantic Guessing Game',
        description: 'Web-based game that has users guess the daily secret word based on how semantically close their other guesses are. This game relies on a hot/cold aspect to help users make a reliable choice.',
        id: '12',
        link: 'https://github.com/aidanvancil/Synonymy',
        techs: [
            '- Django',
            '- Word2Vec',
            '- OpenAI API',
            '- Gensim',
            '- NLP',
            '- Figma',
            '- TailwindCSS',
            '- Javascript'
        ]
    }
];

// Generate modals dynamically
const portfolioModals = modalData.map(data => generatePortfolioModal(data.images, data.title, data.description, data.id, data.link, data.techs));

// Add the generated modals to the DOM
document.getElementById('portfolioModalsContainer').innerHTML = portfolioModals.join('');
