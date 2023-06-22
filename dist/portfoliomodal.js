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
    }
];

// Generate modals dynamically
const portfolioModals = modalData.map(data => generatePortfolioModal(data.images, data.title, data.description, data.id, data.link, data.techs));

// Add the generated modals to the DOM
document.getElementById('portfolioModalsContainer').innerHTML = portfolioModals.join('');
