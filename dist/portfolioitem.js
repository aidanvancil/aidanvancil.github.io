// Define your portfolio item data in JSON format
var portfolioItems = [
    {
        keywords: ["math", "dice", "random", "rng", "fun", "game", "domino", "shut", "the", "box", "roll"],
        modalTarget: "#portfolioModal1",
        imageSrc: "assets/img/portfolio/shut_the_box.gif"
    },
    {
        keywords: ["dumbells", "exertion", "prediction", "AI", "ML", "AI/ML", "guessing", "math"],
        modalTarget: "#portfolioModal2",
        imageSrc: "assets/img/portfolio/dumbell.png"
    },
    {
        keywords: ["matrix", "matrice", "linear algebra", "math", "science", "graph", "absolute error"],
        modalTarget: "#portfolioModal3",
        imageSrc: "assets/img/portfolio/matrix.png"
    },
    {
        keywords: ["location", "landmark", "housing", "airbnb", "prediction", "science", "dataframe", "AI", "ML", "AI/ML"],
        modalTarget: "#portfolioModal4",
        imageSrc: "assets/img/portfolio/chicago.png"
    },
    {
        keywords: ["board", "multiplayer", "two-player", "LAN", "local"],
        modalTarget: "#portfolioModal5",
        imageSrc: "assets/img/portfolio/checkers.gif"
    },
    {
        keywords: ["fitting", "marks", "math", "bias", "variance", "AI", "ML", "AI/ML", "error"],
        modalTarget: "#portfolioModal6",
        imageSrc: "assets/img/portfolio/perfectfit.png"
    },
    {
        keywords: ["chess", "board", "two-player", "multiplayer", "AI/ML", "AI", "ML"],
        modalTarget: "#portfolioModal7",
        imageSrc: "assets/img/portfolio/chessboard.png"
    },
    {
      keywords: ["matrix", "matrice", "linear algebra", "math", "science", "graph", "absolute error"],
      modalTarget: "#portfolioModal8",
      imageSrc: "assets/img/portfolio/matrix.png"
    },
    {
      keywords: ["sorting", "algorithm", "data", "visualization", "science"],
      modalTarget: "#portfolioModal9",
      imageSrc: "assets/img/portfolio/sorting.gif"
    }
  ];
  
  // Function to generate the portfolio items dynamically
  function generatePortfolioItems() {
    var portfolioContainer = document.getElementById("portfolioContainer");
  
    // Loop through the portfolioItems array and generate HTML for each item
    for (var i = 0; i < portfolioItems.length; i++) {
      var item = portfolioItems[i];
  
      // Create the portfolio item HTML
      var portfolioItem = document.createElement("div");
      portfolioItem.className = "col-md-6 col-lg-4 mb-5 modals";
      portfolioItem.innerHTML = item.keywords.join(" ");
  
      // Create the inner elements for the portfolio item
      var portfolioItemInner = document.createElement("div");
      portfolioItemInner.className = "portfolio-item mx-auto";
      portfolioItemInner.setAttribute("data-bs-toggle", "modal");
      portfolioItemInner.setAttribute("data-bs-target", item.modalTarget);
  
      var portfolioItemCaption = document.createElement("div");
      portfolioItemCaption.className = "portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100";
  
      var portfolioItemCaptionContent = document.createElement("div");
      portfolioItemCaptionContent.className = "portfolio-item-caption-content text-center text-white";
      portfolioItemCaptionContent.innerHTML = '<i class="fas fa-plus fa-3x"></i>';
  
      var portfolioItemImage = document.createElement("img");
      portfolioItemImage.className = "img-fluid";
      portfolioItemImage.src = item.imageSrc;
      portfolioItemImage.alt = "...";
  
      // Append the inner elements to the portfolio item
      portfolioItemCaption.appendChild(portfolioItemCaptionContent);
      portfolioItemInner.appendChild(portfolioItemCaption);
      portfolioItemInner.appendChild(portfolioItemImage);
      portfolioItem.appendChild(portfolioItemInner);
  
      // Append the portfolio item to the container
      portfolioContainer.appendChild(portfolioItem);
    }
  }
  
  // Call the function to generate the portfolio items
  generatePortfolioItems();
  