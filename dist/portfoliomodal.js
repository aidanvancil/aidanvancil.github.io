// JavaScript
function generatePortfolioModal(images, title, description, id) {
    const imageHtml = Array.isArray(images)
    ? images.map(imageSrc => `<img class="img-fluid rounded mb-5" src="${imageSrc}" alt="..." />`).join('')
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
        description: 'Built this game in a 7-hour hackathon. This includes knocking down 9 dominoes. Obviously with a certain ruleset and scope, the player rolls two dice and uses their sum to notch the dominoes one at a time. In this project I illustrate my knowledge of package containers, directory strucutres, classes, inheritance, derived inheritance, proper syntax documentation, and fair code; as well as file organization. For more information on this project check it out and play here!',
        id: '1'
    },
    {
        images: [
            'assets/img/portfolio/dumbell.png',
        ],
        title: 'Exertion Predictor',
        description: 'WORK. IN. PROGRESS.',
        id: '2'
    },
    {
        images: [
            'assets/img/portfolio/matrix.png',
        ],
        title: 'Matrix Program: Modding Methods',
        description: 'WORK. IN. PROGRESS.',
        id: '3'
    },
    {
        images: [
            'assets/img/portfolio/chicago.png',
        ],
        title: 'Algorithm For Airbnb Housing In San Francisco',
        description: 'WORK. IN. PROGRESS.',
        id: '4'
    },
    {
        images: [
            'assets/img/portfolio/checkers.gif',
        ],
        title: 'Checkers / Local LAN Play ',
        description: 'Checkers is a classic board game for two players. One player has the dark pieces (RED); the other has the light pieces (GRAY). Players alternate turns. A move consists of moving a piece diagonally to an adjacent unoccupied square. If the adjacent square contains an opponent’s piece. For more documentation seek the following: play here!',
        id: '5'
    },
    {
        images: [
            'assets/img/portfolio/perfectfit.png',
        ],
        title: 'Finding A Perfect Fit - AI/ML',
        description: 'WORK. IN. PROGRESS.',
        id: '6'
    },
    {
        images: [
            'assets/img/portfolio/chessboard.png',
        ],
        title: 'Chess',
        description: 'WORK. IN. PROGRESS.',
        id: '7'
    },
    {
        images: [
            'assets/img/portfolio/sorting2.png',
            'assets/img/portfolio/sorting.gif',
            'assets/img/portfolio/sorting3.png',
            'assets/img/portfolio/sorting4.png'
        ],
        title: 'Sorting Algorithms Visualized',
        description: 'Through this, I got preparation for my next algorithm visualization program including the A* pathfinding algorithm for mazes and obstacles. Probablitiy and stats theory is also evident in this visualization. For more documentation view here!',
        id: '8'
    }
];

// Generate modals dynamically
const portfolioModals = modalData.map(data => generatePortfolioModal(data.images, data.title, data.description, data.id));

// Add the generated modals to the DOM
document.getElementById('portfolioModalsContainer').innerHTML = portfolioModals.join('');
